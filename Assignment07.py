# ------------------------------------------------- #
# Title: Assignment07
# Description: A simple example of storing data in a binary file and the try/except function
# ChangeLog: (Who, When, What)
# Emmanuel Ihejirika,6.3.2023,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
file_name = 'AppData.dat'


def get_user_data():
    intId = int(input('Enter an ID:'))
    strName = str(input('Enter a name: '))
    lstcustomer = [intId, strName]
    print(lstcustomer)
    return lstcustomer
# Processing -------------------------------------- #
def save_data_to_file(file_name, lstcustomer):
    with open(file_name, 'ab') as file:
        pickle.dump(lstcustomer, file)
    print(file)
        
    pass  # TODO: Add code here

def read_data_from_file(file):
    with open('AppData.dat', 'rb') as file:
        objFiledata = pickle.load(file)
        print(objFiledata)
    pass  # TODO: Add code here

while True:
    try: 
        print('Hello, welcome to the file saver')
        choice = int(input('''Make a choice:
        1. Get user data
        2. save data from file
        3. read data from the file
        4. Close the program 
        '''))
        if choice == 1:
            get_user_data()
        elif choice == 2:
            lstcustomer = get_user_data() #not sure why code bugs out when this line isnt here
            save_data_to_file(file_name, lstcustomer)
        elif choice == 3: 
            read_data_from_file(file_name)
        elif choice == 4:
            break
    except ValueError:
        print('INVALID CHOICE! Enter 1, 2 or 3!')
    

# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
#
#
#
# TODO: store the list object into a binary file
#
#
#
# TODO: Read the data from the file into a new list object and display the contents
#
#
#