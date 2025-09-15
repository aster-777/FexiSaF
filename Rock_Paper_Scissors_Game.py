####### Rock_Paper_Scissors
print("__________Rock_Paper_Scissors_________")
### User Name
user_name = input("Enter your User_name: ")
print(f"______WELCOME {user_name}______")
print("***********************************")

### Option generator
options = ["Rock", "Paper", "Scissors"]
for i in [0,1,2]:
    computer_option= options[i]

#print(computer_option)


### For the User
users_option = input(f"Choose one of the options {options}:  ")
print("****************************************")
users_option = users_option.lower()
#print(users_option)

### For the computer
computers_option = computer_option.lower()
#print(computers_option)

### Comparing options
if users_option == computers_option:
    print(f"Computer: {computers_option} : User: {users_option}")
    print("WE HAVE A DRAW!!!")
elif users_option=="rock" and computers_option=="scissors":
    print(f"Computer: {computers_option} : User: {users_option}")
    print(f"{user_name} WON!!!")
elif users_option=="scissors" and computers_option=="paper":
    print(f"Computer: {computers_option} : User: {users_option}")
    print(f"{user_name} WON!!!")
elif users_option=="paper" and computers_option=="rock":
    print(f"Computer: {computers_option} : User: {users_option}")
    print(f"{user_name} WON!!!")
else:
    print(f"Computer: {computers_option} : User: {users_option}")
    print("COMPUTER WON")





