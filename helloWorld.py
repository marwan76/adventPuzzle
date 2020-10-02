# This program prints Hello, world!

msg = "hello world"

msgArray = msg.split()

#using enumerate 
for i, val in enumerate(msgArray):
    print(i, ",",val)

