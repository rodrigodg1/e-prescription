#NuCypher Module
from umbral import SecretKey, Signer
from umbral import encrypt, decrypt_original
from umbral import generate_kfrags
from umbral import reencrypt
from umbral import decrypt_reencrypted






class Privacy:
    def __init__(self):
        pass

    def create_delegator_keys(self): 
        self.delegator_secret_key = SecretKey.random()
        self.delegator_public_key = self.delegator_secret_key.public_key()
    
        self.delegator_signing_key = SecretKey.random()
        self.delegator_signer = Signer(self.delegator_signing_key)
        self.delegator_verifying_key = self.delegator_signing_key.public_key()
        
        return self.delegator_secret_key,self.delegator_public_key,self.delegator_signing_key,self.delegator_signer, self.delegator_verifying_key
        
    def create_delegatee_keys(self):
        self.delegatee_secret_key = SecretKey.random()
        self.delegatee_public_key = self.delegatee_secret_key.public_key()
        
        return self.delegatee_secret_key,self.delegatee_public_key
    
    
    def encryption(self,data,public_key):
        plaintext = data
        capsule, ciphertext = encrypt(public_key, plaintext)
        
        return capsule,ciphertext

            
    def decrypt(self,capsule,ciphertext,secret_key):
        cleartext = decrypt_original(secret_key, capsule, ciphertext)
        
        return cleartext
    