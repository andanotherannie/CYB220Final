import hashlib

#This will be the password made by user
password = 'blue'

#This is to get the hash of the password made wherein hash_string is the password
def encrypt_string(hash_string):
   sha_signature = \
      hashlib.sha256(hash_string.encode()).hexdigest()
   return sha_signature
sha_signature = encrypt_string(password)

#Test to see password and its hash
'''print(password)
print(sha_signature)'''

voe = input("Would you like to see your passwords or add new ones? Please type view, add, or cancel.")

#If password is correct, show read version of text. If not, told to try again.
if voe == "view":
   input("Please enter password:")
   if sha_signature == encrypt_string(password):
      file = open("passwordfile.txt", "r")
      print(file.read())
   else:
      print("Incorrect password. Please try again.")

# If password is correct, show write version of text and allow user to add text. If not, told to try again.
elif voe == "add":
   if sha_signature == encrypt_string(password):
      file = input("passwordfile.txt")
      with open("passwordfile.txt", "w") as file:
         file.write(input())
         file.close()
   else:
      print("Incorrect password. Please try again.")

#If user chooses cancel, code quits.
elif voe == "cancel":
      quit()

#If user does not choose between view or add, told to try again.
else:
   voe = input("Please type view, add, or cancel.")
