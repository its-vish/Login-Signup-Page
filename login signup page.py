import json
print("**🚾 𝐰𝐞𝐥𝐜𝐨𝐦𝐞..𝐥𝐨𝐠𝐢𝐧 𝐬𝐢𝐠𝐧𝐮𝐩 𝐩𝐚𝐠𝐞 🚾*")
user=input("📂 𝔴𝔥𝔞𝔱 𝔶𝔬𝔲 𝔴𝔞𝔫𝔱 𝔰𝔦𝔤𝔫 𝔲𝔭 𝔬𝔯 𝔩𝔬𝔤𝔦𝔫 𝔞𝔠𝔠𝔬𝔲𝔫𝔱 📂?...= ")
if user=="sign":
    name=input("𝖊𝖓𝖙𝖊𝖗 𝖙𝖍𝖊 𝖓𝖆𝖒𝖊....")
    last_name=input("𝖊𝖓𝖙𝖊𝖗 𝖞𝖔𝖚𝖗 𝖑𝖆𝖘𝖙 𝖓𝖆𝖒𝖊....")
    email=input("enter your email ID.....")
    password=input("𝖊𝖓𝖙𝖊𝖗 𝖞𝖔𝖚𝖗 𝖕𝖆𝖘𝖘𝖜𝖔𝖗𝖉..... ")
    confirm_password=input("𝖊𝖓𝖙𝖊𝖗 𝖞𝖔𝖚𝖗 𝖕𝖆𝖘𝖘𝖜𝖔𝖗𝖉 again.... ")
    if "@" in email and "." or "1-9" in email:
        print("𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥")
        if "@" in password or "#" in password:
            if password==confirm_password:
                print("*✅𝕬𝖈𝖈𝖔𝖚𝖓𝖙 𝖍𝖆𝖘 𝖈𝖗𝖊𝖆𝖙𝖊𝖉 𝖘𝖚𝖈𝖈𝖊𝖘𝖋𝖚𝖑𝖑𝖞*👍,𝖍𝖚𝖗𝖊𝖊𝖊")
                a=open("log.txt","a")
                new_file=a.write("name :- ")
                new_file=a.write(name)
                new_file=a.write("\n")

                new_file=a.write("last_name :-")
                new_file=a.write(last_name)
                new_file=a.write("\n")

                new_file=a.write("password :-")
                new_file=a.write(password)
                new_file=a.write("\n")

                new_file=a.write("Email ID :-")
                new_file=a.write(email)
                new_file=a.write("\n")
                print( )
                a.close()
                print( )
                js=json.dumps(new_file)
                print(js)
                # print((js))

            else:
                print("𝔶𝔬𝔲𝔯 𝔭𝔞𝔰𝔰𝔴𝔬𝔯𝔡 𝔦𝔰 𝔴𝔯𝔬𝔫𝔤❌ ")
        else:
            print("𝐢𝐧 𝐩𝐚𝐬𝐬𝐰𝐨𝐫𝐝 𝐧𝐨 𝐬𝐩𝐞𝐜𝐢𝐚𝐥 𝐜𝐡𝐫𝐚𝐜𝐭𝐨𝐫𝐬❗")
    else:
        print("encorrect email")
elif user=="login":
    name1=input("enter your name : ")
    file=open("log.txt","r")
    new_file1=file.read()
    if name1 in new_file1:
        password1=input("enter your password :")
        if password1 in new_file1:
            print("*✅𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥👍*")
            email1=input("enter your email id:")
            if email1 in new_file1:
                print("*✅login 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥 👍*")
                print()
                j=json.dumps(new_file1)
                print(j)
                print(type(j))
            else:
                print("email is 🆆🆁🅾🅽🅶❌ ")
        else:
            print("password is 🆆🆁🅾🅽🅶❌ ")
    else:
         print("user name is 🆆🆁🅾🅽🅶❌")