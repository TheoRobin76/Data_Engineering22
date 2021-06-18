import os

working_directory = os.getcwd()

def return_user_id():
    print(os.getuid())

def operating_system_information():
    print(os.uname())

