/*
 * Copyright 2020 - MATTR Limited
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *     http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
const fs = require("fs");
//var process = require('process')



import {
  Bls12381G2KeyPair,
  BbsBlsSignature2020,
  BbsBlsSignatureProof2020,
  deriveProof
} from "@mattrglobal/jsonld-signatures-bbs";
import { extendContextLoader, sign, verify, purposes } from "jsonld-signatures";

import inputDocument from "./data/inputDocument.json";
import keyPairOptions from "./data/keyPair.json";
import exampleControllerDoc from "./data/controllerDocument.json";
import bbsContext from "./data/bbs.json";
import revealDocument from "./data/deriveProofFrame.json";
import citizenVocab from "./data/citizenVocab.json";
import credentialContext from "./data/credentialsContext.json";

/* eslint-disable-next-line @type-eslint/no-explicit-any */
const documents: any = {
  "did:example:489398593#test": keyPairOptions,
  "did:example:489398593": exampleControllerDoc,
  "https://w3id.org/security/bbs/v1": bbsContext,
  "https://w3id.org/citizenship/v1": citizenVocab,
  "https://www.w3.org/2018/credentials/v1": credentialContext
};

/* eslint-disable-next-line @type-eslint/no-explicit-any */
const customDocLoader = (url: string): any => {
  const context = documents[url];

  if (context) {
    return {
      contextUrl: null, // this is for a context via a link header
      document: context, // this is the actual document that was loaded
      documentUrl: url // this is the actual context URL after redirects
    };
  }

  console.log(
    `Attempted to remote load context : '${url}', please cache instead`
  );
  throw new Error(
    `Attempted to remote load context : '${url}', please cache instead`
  );
};

//Extended document load that uses local contexts
/* eslint-disable-next-line @type-eslint/no-explicit-any */
const documentLoader: any = extendContextLoader(customDocLoader);

const main = async (): Promise<void> => {
  //Import the example key pair
  const keyPair = await new Bls12381G2KeyPair(keyPairOptions);

  //console.log("Input document");
  //console.log(JSON.stringify(inputDocument, null, 2));

  //Sign the input document
  const start_sign_doctor = performance.now();
  const signedDocument = await sign(inputDocument, {
    suite: new BbsBlsSignature2020({ key: keyPair }),
    purpose: new purposes.AssertionProofPurpose(),
    documentLoader
  });
  const duration_sign_doctor = performance.now() - start_sign_doctor;

  console.log("Time to doctor sign prescription: ",duration_sign_doctor)
  fs.appendFileSync("time_sign_doctor.txt", duration_sign_doctor.toString())
  fs.appendFileSync("time_sign_doctor.txt","\n")
  
  //console.log("Input document with proof");
  //console.log(JSON.stringify(signedDocument, null, 2));


  //Sign the input document
  const start_sign_patient = performance.now();
  const multiSignedDocument = await sign(signedDocument, {
    suite: new BbsBlsSignature2020({ key: keyPair }),
    purpose: new purposes.AssertionProofPurpose(),
    documentLoader
  });
  const duration_sign_patient = performance.now() - start_sign_patient;

  console.log("Time to patient sign prescription: ",duration_sign_patient)
  fs.appendFileSync("time_sign_patient.txt", duration_sign_patient.toString())
  fs.appendFileSync("time_sign_patient.txt", "\n")
  //console.log("Input document with multiple proofs");
  //console.log(JSON.stringify(multiSignedDocument, null, 2));

  //Verify the proof

  /*
  const verified = await verify(multiSignedDocument, {
    suite: new BbsBlsSignature2020(),
    purpose: new purposes.AssertionProofPurpose(),
    documentLoader
  });
*/

  //console.log("Verify the signed proof");
  //console.log(JSON.stringify(verified, null, 2));

  //Derive a proof
  const start_time_produce_reveal_items = performance.now();
  const derivedProof = await deriveProof(multiSignedDocument, revealDocument, {
    suite: new BbsBlsSignatureProof2020(),
    documentLoader
  });
  const duration_produce_reveal_items= performance.now() - start_time_produce_reveal_items;

  console.log("Time to produce new transacation items with allowed items: ",duration_produce_reveal_items)
  fs.appendFileSync("time_produce_reveal_items.txt", duration_produce_reveal_items.toString())
  fs.appendFileSync("time_produce_reveal_items.txt", "\n")

  

  console.log("Derived Proof Result");
  console.log(JSON.stringify(derivedProof, null, 2));

  //Verify the derived proof
  const start_verify = performance.now();
  const derivedProofVerified = await verify(derivedProof, {
    suite: new BbsBlsSignatureProof2020(),
    purpose: new purposes.AssertionProofPurpose(),
    documentLoader
  });
  const duration_verify = performance.now() - start_verify;

  console.log("Time to verify transaction with allowd items: ",duration_verify)
  fs.appendFileSync("time_verify_reveal_items.txt", duration_verify.toString())
  fs.appendFileSync("time_verify_reveal_items.txt", "\n")

  console.log("Derived Proof Verification result");
  console.log(JSON.stringify(derivedProofVerified, null, 2));
};

main();
