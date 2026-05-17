
from pathlib import Path        
# from pathlib import Path as path # changing the class name   
import os
# import os as next                   # changing the class name
def read_file_and_folder():
    path=Path('')
    items=list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items} ")  



def create_file():
    try:
        read_file_and_folder()
        name=input("Please tell your File name: ")
        p=Path(name)
        if not p.exists() and p.is_file:          #imp
        # p.exists()  ✅p.is_file ✅        not p.is_file()❌
            with open(p,"w") as fs:     #w and a is best and useful than X
                choose=int(input("you want to write(0/1): "))
                if choose==1:
                    data=input("What you want to write: ")
                    fs.write(data)
                else:
                    pass
            print(F"File Created successfully")
                    
        else:
            print("This file already Exist")
    except Exception as err:
        print(f"An error occured as {err}")
def read_file():
    try:
        read_file_and_folder()
        name=input("Which file you want to read: ")
        p=Path(name)
        if p.exists() and p.is_file:          #imp
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
            print("File Readed successfully")
        else:
            print("File does not Exist")
    except Exception as err:
        print(f"An error Occured as {err}")
def update_file():
    try:
        read_file_and_folder()
        name=input("Tell which file you want to Update: ")
        p=Path(name)
        if p.exists() and p.is_file:          #imp
            print("Click 1 for changing the name of your file: ")
            print("Click 2 for overwriting the data of your file: ")
            print("Click 3 for appending some content in your file: ")
            choose=int(input("Click your Response: "))
            if choose==1:
                name2=input("Tell your New name: ")
                p2=Path(name2)
                if not p2.exists():
                    p.rename(p2)
                else:
                    print("File with new name already exists")
            if choose ==2:
                with open(p,'w') as fs:
                    data=input("Tell what do you want to write, this is overwrite the data: ")
                    fs.write(data)
            if choose==3:
                with open(p,'a') as fs:
                    data=input("Tell what do you want to write, this is overwrite the data: ")
                    fs.write(" " +data)
            print("File update successfully")
        else:
            print("File does not Exist")
    except Exception as err:
        print(f"An error occurred as {err}")
def delete_file():
    try:
        read_file_and_folder()
        name=input("Which File you want to delete: ")
        p=Path(name)
        # p=Path('')        #X
        if p.exists() and p.is_file:
            os.remove(p)
            print("File remove Succesfully")
        else:
            print("File does not Exist")
    except Exception as err:
        print(f"An error occured as {err}")
print("Press 1 for Creating a File")
print("Press 2 for Reading a File")
print("Press 3 for Updating a File")
print("Press 4 for Deletion a File")
choose=int(input("Please tell your respose: "))
if choose==1:
    create_file()
elif choose==2:
    read_file()
elif choose==3:
    update_file()
elif choose==4:
    delete_file()
else:
    print("Invalid Option")

