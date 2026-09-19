print("Welcome to the Data collector App!\n")

#here we collect the information from user 
name=input("Enter your Name: ")
age=int(input("Enter your Age: "))
height=float(input("Enter your Height in CM: "))
fav_num=int(input("Enter your Favourite Number: "))

#here we calculate in which year the user is born from the age 

birth_year=2026-age 

#here is the address variable to store the memory addres and type of the variable
name_addr=id(name)
age_addr=id(age)
height_addr=id(height)
fav_num_addr=id(fav_num)

name_type=type(name)
age_type=type(age)
height_type=type(height)
fav_num_type=type(fav_num)

#now we print the information collected from user 

print(f"\nThank you for providing the information! {name}")
print("The information given by you is:\n")


print(f"Name: {name} (Memory Address:{name_addr},Type:{name_type})")
print(f"Age: {age} (Memory Address:{age_addr},Type:{age_type})")
print(f"Height: {height} (Memory Address:{height_addr},Type:{height_type})")
print(f"Favorite Number: {fav_num} (Memory Address:{fav_num_addr},Type:{fav_num_type})")
print(f"Your Birth Year is:{birth_year} ! (based on your age:{age})")


print("\nThank you! For using the Data collector App!")