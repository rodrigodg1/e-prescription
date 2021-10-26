#open evaluation transaction time
"""
a_file = open("/home/rodrigo/Desktop/programa-para-avaliacao/cosmwasm-examples/contracts/escrow/target/wasm32-unknown-unknown/release/results_transaction_oysternet.txt", "r")
lines = a_file.readlines()

a_file.close()

#new file for format output
new_file = open("time_transaction_formated.txt", "w")

for line in lines:
    #remove line starting with gas
    if not line.startswith("gas"):
        new_file.write(line)


new_file.close()


a_file = open("time_transaction_formated.txt", "r")
lines = a_file.readlines()
a_file.close()

new_file = open("time_transaction_formated.txt", "w")
for line in lines:
        #remove line starting with ""
        if line.strip() != "":
            new_file.write(line)
        
new_file.close()



"""
    
