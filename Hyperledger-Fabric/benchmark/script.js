"use strict";
const FabricCAServices = require("fabric-ca-client");
const {
  FileSystemWallet,
  Gateway,
  X509WalletMixin,
} = require("fabric-network");
const fs = require("fs");
const path = require("path");
const readlineSync = require("readline-sync");

const orgName = "Org1";
const connectionProfilePath = path.resolve(
  __dirname,
  "..",
  "connections",
  `connection-${orgName}.json`
);
const MSP = "Org1MSP";
const channel = "mychannel";
const conn = "connection-Org1.json";
const contractNames = ["Doctor", "Pharmacy"];

async function enrollAdmin() {
  try {
    console.info("Enrolling admin...");

    const connectionProfilePathJSON = fs.readFileSync(
      connectionProfilePath,
      "utf8"
    );

    const caInfo = JSON.parse(connectionProfilePathJSON).certificateAuthorities[
      `${orgName}CA`
    ];

    const ca = new FabricCAServices(
      caInfo.url,
      { verify: false },
      caInfo.caName
    );

    const wallet = new FileSystemWallet(
      path.join(process.cwd(), `../wallet/wallet-${orgName}`)
    );

    const adminExists = await wallet.exists("admin");
    if (adminExists) {
      console.error("Admin already exists");
      return;
    }

    const enrollment = await ca.enroll({
      enrollmentID: "admin",
      enrollmentSecret: "adminpw",
    });

    await wallet.import(
      "admin",
      X509WalletMixin.createIdentity(
        MSP,
        enrollment.certificate,
        enrollment.key.toBytes()
      )
    );

    console.info("Admin enrolled successfully!");
  } catch (e) {
    console.error(`Failed to enroll admin user "admin": ${e}`);
    process.exit(1);
  }
}

async function registerUser(user) {
  try {
    console.info("Registering user " + user + "...");

    const connectionProfilePath = path.resolve(
      __dirname,
      "..",
      "connections",
      `connection-${orgName}.json`
    );
    const walletPath = path.join(process.cwd(), `../wallet/wallet-${orgName}`);
    const wallet = new FileSystemWallet(walletPath);

    const userExists = await wallet.exists(user);

    if (userExists) {
      console.error(`User ${user} already exists`);
      return false;
    }

    const adminExists = await wallet.exists("admin");

    if (!adminExists) {
      console.error("Admin not found");
      return false;
    }

    const gateway = new Gateway();
    await gateway.connect(connectionProfilePath, {
      wallet,
      identity: "admin",
      discovery: { enabled: true, asLocalhost: true },
    });

    const ca = gateway.getClient().getCertificateAuthority();
    const adminIdentity = gateway.getCurrentIdentity();

    const secret = await ca.register(
      { enrollmentID: user, role: "client" },
      adminIdentity
    );
    const enrollment = await ca.enroll({
      enrollmentID: user,
      enrollmentSecret: secret,
    });
    const userIdentity = X509WalletMixin.createIdentity(
      MSP,
      enrollment.certificate,
      enrollment.key.toBytes()
    );

    await wallet.import(user, userIdentity);

    console.info("User " + user + " registered successfully!");
  } catch (e) {
    console.error(`Failed to register user "${user}": ${e}`);
    process.exit(1);
  }
}

async function getContract(contractName, user) {
  console.info("Getting contract " + contractName + "...");

  const wallet = new FileSystemWallet(
    path.join(process.cwd(), `../wallet/wallet-${orgName}`)
  );

  const userExists = await wallet.exists(user);

  if (!userExists) {
    console.error(`User "${user}" does not exist in the wallet`);
    return;
  }

  const gateway = new Gateway();
  await gateway.connect(path.resolve(__dirname, "..", "connections", conn), {
    wallet,
    identity: user,
    discovery: {
      enabled: true,
      asLocalhost: true,
    },
  });

  const network = await gateway.getNetwork(channel);

  console.info("Got contract " + contractName + " successfully!");

  return network.getContract(contractName);
}

(async () => {
  await enrollAdmin();
  await registerUser("benchmarkUser");

  console.info("=====================");
  console.info("TRANSACTION BENCHMARK");
  console.info("=====================");
  const index = readlineSync.keyInSelect(
    contractNames,
    "What contract will be benchmarked?"
  );

  if (index === -1) {
    process.exit(0);
  }

  const contractName = contractNames[index];

  const contract = await getContract(contractName, "benchmarkUser");
  const numberOfTransactions = readlineSync.questionInt(
    "How many transactions will be made?\n"
  );

  if (numberOfTransactions <= 0) {
    process.exit(0);
  }

  console.time("sendTransactions");
  for (let i = 0; i < numberOfTransactions; i++) {
    console.time("sendTransaction" + i);
    if (contractName === "Doctor") {
      await contract.submitTransaction(
        "send",
        "token" + i,
        "patientAddress" + i,
        "doctorAddress" + i,
        "medications" + i,
        "diagnostics" + i
      );
    } else {
      await contract.submitTransaction(
        "send",
        "token" + i,
        "patientAddress" + i,
        "pharmacyAddress" + i,
        "medicationSold" + i
      );
    }
    console.info("Time to execute SEND transaction " + i + ": ");
    console.timeEnd("sendTransaction" + i);
  }

  console.info(
    "\nTime to execute " + numberOfTransactions + " SEND transaction(s): \n"
  );
  console.timeEnd("sendTransactions");

  console.time("queryTransactions");
  for (let i = 0; i < numberOfTransactions; i++) {
    console.time("queryTransaction" + i);
    await contract.evaluateTransaction("query", "patientAddress" + i);
    console.info("Time to execute QUERY transaction " + i + ": ");
    console.timeEnd("queryTransaction" + i);
  }
  console.info(
    "\nTime to execute " + numberOfTransactions + " QUERY transaction(s): \n"
  );
  console.timeEnd("queryTransactions");

  readlineSync.keyInPause("Hit any key to exit...");
  process.exit(0);
})();
