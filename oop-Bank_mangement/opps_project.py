while(True):
    import json
    import random
    import string
    from pathlib import Path
    class Bank:
        database="data.json"
        data=[]
        try:
            if Path(database).exists():
                with open(database) as fs:
                    data=json.load(fs)
                    # data=json.load(fs.read())
            else:
                print("File does not Exists")
        except Exception as err:
            print(f"An error occurred as {err}")
        @staticmethod
        def __update():
            with open(Bank.database,"w") as fs:
                fs.write(json.dumps(Bank.data))
        # @classmethod
        # def update(cls):
        #     with open(cls.database,"w") as fs:
        #         fs.write(json.dumps(Bank.data))
        @classmethod
        def __acct_generate(cls):
            alpha=random.choices(string.ascii_letters, k=3)
            num=random.choices(string.digits, k=3)
            spl_chr=random.choices("!@#$%^&*",k=1)
            id=alpha+num+spl_chr
            random.shuffle(id)
            return "".join(id)


        def creates_acct(self):
            info={
                "Name": input("Tell your Name:- "),
                "Age": int(input("Tell your Age:- ")),
                "Email":input("Tell your Email:- "),
                "Pin":int(input("Tell your Pin:- ")),
                "AcctNo":Bank.__acct_generate(),
                "Balance":0
            }
            if info["Age"]<18 or len(str(info["Pin"]))!=4:
                print("Sorry you cannot create Account")
            else:
                print("Account has been Creted Successfully")
                for i in info:
                    print(f"{i} : {info[i]}")
                print("Please note down your Account Number")
                Bank.data.append(info)
                Bank.__update()
        def deposit_mny(self):
            accNum=input("Please tell your Acct No.:- ")
            pinNum=int(input("Please tell your Pin No.:- "))
            # print(Bank.data)
            userdata=[i for i in Bank.data if i["AcctNo"]==accNum and i["Pin"]==pinNum]
            if userdata==False:
                print("Sorry No data Found")
            else:
                amount=int(input("How much you wnat to deposit:- "))
                if amount>10000 or amount<0:
                    print("Sorry the amount is too much, you can deposit below 10000 or above 0 ")
                else:
                    # print(Bank.data)  
                    userdata[0]["Balance"]+=amount
                    # print(userdata)
                    Bank.__update()
                    print("your money is Deposited Successfully")
        def withdraw_mny(self):
            accNum=input("Please tell your Acct No.:- ")
            pinNum=int(input("Please tell your Pin No.:- "))
            # print(Bank.data)
            userdata=[i for i in Bank.data if i["AcctNo"]==accNum and i["Pin"]==pinNum]
            if userdata==False:
                print("Sorry No data Found")
            else:
                amount=int(input("How much you wnat to withdraw:- "))
                if amount>10000 or amount<0 or userdata[0]["Balance"]<amount:
                    print("Sorry the amount is too much, you can withdraw below 10000 or above 0 ")
                else:
                    # print(Bank.data)  
                    userdata[0]["Balance"]-=amount
                    # print(userdata)
                    Bank.__update()
                    print("Your money is withdrew Successfully")
        def details_acct(self):
            accNum=input("Please tell your Acct No.:- ")
            pinNum=int(input("Please tell your Pin No.:- "))
            userdata=[i for i in Bank.data if i["AcctNo"]==accNum and i["Pin"]==pinNum]
            if userdata==False:
                print("Sorry No data Found")
            else:
                print("Your Account Details are: \n\n")
                for i in userdata[0]:
                    print(f"{i} : {userdata[0][i]}")
                    # 8W1Dw8#
        def update_acct(self):#name,email,pin
            accNum=input("Please tell your Acct No.:- ")
            pinNum=int(input("Please tell your Pin No.:- "))
            userdata=[i for i in Bank.data if i["AcctNo"]==accNum and i["Pin"]==pinNum]
            if userdata==False:
                print("Sorry No data Found")
            else:
                print("Your cannot change the age, acccount number, balance")
                print("Fill the details for change or leave it empty if no change")
                newdata={
                        "Name": input("Tell your new Name or Enter to skip:- "),
                        "Email":input("Tell your new Email or Enter to skip:- "),
                        "Pin":input("Tell your new Pin or Enter to skip:- ")        #imp
                        }
                if newdata["Name"]=="":
                    newdata["Name"]=userdata[0]["Name"]
                if newdata["Email"]=="":
                    newdata["Email"]=userdata[0]["Email"]
                if newdata["Pin"]=="":
                    newdata["Pin"]=userdata[0]["Pin"]

                newdata["Age"]=userdata[0]["Age"]
                newdata["AcctNo"]=userdata[0]["AcctNo"]
                newdata["Balance"]=userdata[0]["Balance"]
                if type(newdata["Pin"])==str:
                    newdata["Pin"]=int(newdata["Pin"])  
                # pin = input("Tell your new Pin or Enter to skip:- ")
                # if pin == "":
                #     newdata["Pin"] = userdata[0]["Pin"]
                # elif pin.isdigit() and len(pin) == 4:
                #     newdata["Pin"] = int(pin)
                # else:
                #     print("Invalid PIN")
                #     return
                
                for i in newdata:
                    if newdata[i]==userdata[0][i]:
                        continue
                    else:
                        userdata[0][i]=newdata[i]
                Bank.__update()
                print("Details Updated Successfully")
        def delete_acct(self):
            accNum=input("Please tell your Acct No.:- ")
            pinNum=int(input("Please tell your Pin No.:- "))
            userdata=[i for i in Bank.data if i["AcctNo"]==accNum and i["Pin"]==pinNum]
            if userdata==False:
                print("Sorry No data Found")
            else:
                check=input("Press y for Delete:- ")
                if check=="y":
                    index=Bank.data.index(userdata[0])
                    Bank.data.pop(index)
                    print("Account Deleted Successfully")
                    Bank.__update()
    user=Bank()
    print("press 1 for Creating Account")
    print("perss 2 for Depositing the money in the bank")
    print("press 3 for withdrawing the money in the bank")
    print("press 4 for Account Details")
    print("press 5 for updating your Account")
    print("press 6 for Deleting your Account")
    check=int(input("Select an OPtion:- "))
    if check==1:
        user.creates_acct()
        # print(user.data)
    elif check==2:
        user.deposit_mny()
    elif check==3:
        user.withdraw_mny()
    elif check==4:
        user.details_acct()
    elif check==5:
        user.update_acct()
    elif check==6:
        user.delete_acct()
    else:
        print("Invalid Choose")
    response=input("\nDO you want to do again:- ")
    print("\n")
    if response=="n":
        break