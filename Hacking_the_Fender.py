# Hacking the fender code academy

# Importing csv to the script

import csv

# Creating a list of comprimised users

comprimised_users = []

# Opening up the file with peoples passwords in a python friendly format and pass it for now

# Parse the temporary file into an non temporary variable

# Print the rows with both the usernames and passwords, then the usernames seperately

# Append the Usernames to the comprimised_users variable

with open("passwords.csv") as password_file:
  #pass
  password_csv = csv.DictReader(password_file)
  #password_row = ""
  for row in password_csv:
    #password_row += row
    #print(row)
    #print(row["Username"])
    comprimised_users.append(row["Username"])

# Create a .txt file with all the comprimised_users

with open("comprimised_users.txt", "w") as compromised_user_file:
  for user in comprimised_users:
    #comprimised_user_file += username
    compromised_user_file.write(user)

# Opening the JSON module

import json

# Create a json file to send to the boss

# Write out the json file

with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "Message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

# Change the password to slash null's signiture

with open("new_passwords.csv", "w") as new_password_obj:
  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_password_obj.write(slash_null_sig)


# Printing commands

print(comprimised_users)