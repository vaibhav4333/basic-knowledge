age = int(input("enter your age :"))

while age>18 and age<25:
   print("you are eligible for the program")
   age=int(input("enter your age : "))
print(f"you are {age} years old")




food = input("enter your fav food (q for quit) : ")

while not food == "q":
    print(f"your fav food is{food}")
    food = input("enter your fav food (q for quit) : ")
print("bye")

