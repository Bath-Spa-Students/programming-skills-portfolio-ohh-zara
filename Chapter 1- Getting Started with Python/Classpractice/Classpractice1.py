#Class activity
#Make an Identification Card for a user.

#Start by making a welcome messgae.
print('''\n\nWelcome! I am here too make ur own identification card 
For that ill ask some questions''')


#Next ask the user for some data.

#First we will ask the user for the Name so I took variable "Name" and used input so user can enter there name.
#We will do the same for every other question too
print("\nFirstly, What shall you go by")
Name = input("Enter name: ")
print("Such a nice name,", Name, "!")


print("\nNext ill need your age")
Age = input("Enter age:")
print("Your age is", Age)

print("\nWhat is something you'd like to do in ur free time?")
Hobby = input("Enter any hobbies: ")
print("Your" , Hobby , "seems super fun," , Name, "!")

print("\nLast question!")
print("Whats one memory you remember")
Memory = input("Enter memory you remember:")
print("'", Memory,  "'is one memory too remember,", Name)

print("\nThank you,", Name, "for all this information")
print("\n\nIf you wanna confrim this information press 1 if not press 0")

#Here i just added an Else if staement just so if the user wants too conrifm there information
user_input = input("Do you want to continue? (1/0): ")
if user_input.lower() == "1":
    print("\n\nSo,",Name, "Your age is", Age, "\nYour hobby is", Hobby, "\nAnd the last meomry you remember was", Memory)
    print("Thank you for your time!...", Name)
else:
    print("\n\nThank you for your time!...", Name)

print("\n\nHope you enjoyed!!")




