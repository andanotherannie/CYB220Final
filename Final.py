import hashlib
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

# opening the key
with open('filekey.key', 'rb') as filekey:
   key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open('passwordfile.txt', 'rb') as file:
   original = file.read()

# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open('passwordfile.txt', 'wb') as encrypted_file:
   encrypted_file.write(encrypted)


# This will be the password made by user
password = 'blue'

# This is to get the hash of the password made wherein hash_string is the password
def encrypt_string(hash_string):
   sha_signature = \
      hashlib.sha256(hash_string.encode()).hexdigest()
   return sha_signature
sha_signature = encrypt_string(password)

# Test to see password and its hash
'''print(password)
print(sha_signature)'''

voe = input("Would you like to see your passwords or add new ones? Please type view, add, or cancel.")

# If password is correct, show read version of text. If not, told to try again.
if voe == "view":
   input("Please enter password:")
   if sha_signature == encrypt_string(password):
      # using the key
      fernet = Fernet(key)
      # opening the encrypted file
      with open('passwordfile.txt', 'rb') as enc_file:
         encrypted = enc_file.read()
      # decrypting the file
      decrypted = fernet.decrypt(encrypted)
      # opening the file in read mode and writing the decrypted data
      with open('passwordfile.txt', 'rb') as dec_file:
         dec_file.write(decrypted)
   en = input("Please enter 1 to quit and encrypt your file.")
   if en == '1':
      # opening the key
      with open('filekey.key', 'rb') as filekey:
         key = filekey.read()

      # using the generated key
      fernet = Fernet(key)

      # opening the original file to encrypt
      with open('passwordfile.txt', 'rb') as file:
         original = file.read()

      # encrypting the file
      encrypted = fernet.encrypt(original)

      # opening the file in write mode and
      # writing the encrypted data
      with open('passwordfile.txt', 'wb') as encrypted_file:
         encrypted_file.write(encrypted)
      '''file = open("passwordfile.txt", "r")
      print(file.read())'''
   else:
      print("Incorrect password. Please try again.")

# If password is correct, show write version of text and allow user to add text. If not, told to try again.
elif voe == "add":
   if sha_signature == encrypt_string(password):
      # using the key
      fernet = Fernet(key)
      # opening the encrypted file
      with open('passwordfile.txt', 'rb') as enc_file:
         encrypted = enc_file.read()
      # decrypting the file
      decrypted = fernet.decrypt(encrypted)
      # opening the file in read mode and writing the decrypted data
      with open('passwordfile.txt', 'wb') as dec_file:
         dec_file.write(decrypted)
      en = input("Please enter 1 to quit and encrypt your file.")
      if en == '1':
      # opening the key
         with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

      # using the generated key
         fernet = Fernet(key)

      # opening the original file to encrypt
         with open('passwordfile.txt', 'rb') as file:
            original = file.read()

      # encrypting the file
      encrypted = fernet.encrypt(original)

      #opening the file in write mode and
      # writing the encrypted data
      with open('passwordfile.txt', 'wb') as encrypted_file:
         encrypted_file.write(encrypted)
      '''file = input("passwordfile.txt")
         with open("passwordfile.txt", "w") as file:
         file.write(input())
         file.close()'''
   else:
      print("Incorrect password. Please try again.")

# If user chooses cancel, code quits.
elif voe == "cancel":
      quit()

# If user does not choose between view or add, told to try again.
else:
   voe = input("Please type view, add, or cancel.")

