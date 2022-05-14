import os

#Validate whether directory exists
path_name = input('Where did you want to save your file? ')

isdir = os.path.isdir(path_name)
while isdir != True:
    print("This path does not exist.")
    path_name = input("Where did you want to save it? ")
    isdir = os.path.isdir(path_name)

#Break while loop
print(path_name + ': does exist.')


#Create file in the system
file_name = input('\nWhat did you want to call your file? ')

file = str(file_name) + '.txt'

isExist = os.path.exists(path_name + '/' + file)
if isExist is True:
    print("This file name already exists.")
    file_name = input("Choose a new file name. ")
    file = str(file_name) + '.txt'

print(file + ' is created.')
NewFile = open(file, 'w')
NewFile.write("Contact Information: \n\n")
NewFile.close

#Move created file to specified directory
original_source = os.getcwd()
file_source = original_source + '/' + file
destination = path_name + '/' + file
os.rename(file_source, destination)

isExist = os.path.exists(path_name + '/' + file)

if isExist:
    print("File created successfully.")
else:
    print("No such file exists.")
print('-------------------------\n')

#Function to display output to user
def output():
    print("\nYou've sucessfully updated the following file: " + file)
    print("Here is the information you stored...")
    print('\nName: ' + user_name.title())
    print('Address: ' + home_address.title())
    print('Phone Number: ' + phone_number)

#Collect input from user
user_name = input('Enter your name: ')
home_address = input('Enter your address: ')
phone_number = input('Enter your phone number: ')

#Open file and write new info
f = open(destination, "a")
f.write(user_name)
f.write(", ")
f.write(home_address)
f.write(", ")
f.write(phone_number)
f.close()

#Call function to display output
output()