word="learning"
with open("practice.txt","r") as f:
#     #f.write("Hi everyone\n We are learning File I/O \n using Java.\n I like programming in Java.")
#      data=f.read()

# new_data =data.replace("Java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#      f.write(new_data)


    data = f.read()
    if(word in data):
            print("found")
    else:
            print("not found")
