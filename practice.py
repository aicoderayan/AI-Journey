# count = 0
# while count < 10:
#     count = count + 1
#     if count == 5:
#         continue
#     print(count)  

# number = 0 
# while number < 10:
#     number = number + 1
#     if number % 2 == 0:
#         continue
#     print(number)

# while True:
#  number =int(input("Enter the number: "))
#  if number < 0:
#   continue
#  if number == 0:
#   break
#  if number > 0:
#   print(number)

# while True:
#     number =int(input("Enter the number: "))
#     if number < 0:
#         continue
#     if number == 0:
#         break
#     if number > 0:
#         print(number)
username =(input("Enter the username: "))

if username == "Rehman":
    password =input("Enter the password: ")
    if password == "Rehman123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")        

