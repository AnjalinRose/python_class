credentials={"alice":"alice123","bob":"bob123"}
username=input("enter username: ")
password=input("enter password: ")
if username in credentials :
    org_pass=credentials[username]
    if org_pass==password:
        print("login success")
    else:
        print("falied")
else:
    print("no such user")
    