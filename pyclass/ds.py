#DICTIONARIES
#marks={"Alice":30 , "Bob":10}
#alice_marks = marks["Alice"]
#print(alice_marks)

credentials={"username" : "Anjali",  "password": "Anjali123" }
username=input("Enter your username: ")
password=input("Enter you password: ")
if username==credentials["username"] and password==credentials["password"]:
    print("login success")
else:
    print("login unsuccessful")
