import shutil, os
from pathlib import Path
#run in terminal as ADMIN
#create a script to copy and move sysmon log - done
#then parse out the last 100 entries - todo - probably note going to happen
#user input on file paths- done
    # can make file paths but when creating a dircetory it makes a file - done


user_input = input("""\nthis is the automated sysmon log grabber and parser
                       Do you want to copy the sysmon log to the default location or 
                       your own?
                       1) Default location - C:\\temp\SysmonLogs
                       2) Custom location - Type in the full file path EX: C:\\path\path \n""")

file = 'C:\\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx'
direcktory = 'C:\\temp\SysmonLogs'

def default(file, direcktory):
    
    os.mkdir(direcktory)
    filepath = shutil.copy(file, direcktory)
    print(f'Logs are located in -- {filepath}') #copy and print file path

   
def user_option(file):
    user_filepath = input()
    os.mkdir(user_filepath)
    filepath2 = shutil.copy(file, user_filepath)
    print(f'Logs are located in -- {filepath2}') #copy and print file path


    
if user_input == '1':
    default(file, direcktory)
else:
    user_option(file)




 #----When trying to use this if else to check if the file path was there it would just create a file with the log in it
    # path = Path(direcktory) #check if new directory for file is there
    # if path.is_file() == False:
    #     print(f'File path -- {direcktory} -- exists, copying log to this location')
    # else:
    #     os.mkdir(direcktory)
    #     print(f'Created file path -- {direcktory}')  
