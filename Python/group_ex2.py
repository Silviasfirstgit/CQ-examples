no1 = int(input("please give a first number "))
no2 = int(input("please give a second number "))
no3 = int(input("please give a third number "))
no4 = int(input("please give a fourth number "))
no5 = int(input("please give a fifth number "))
no6 = int(input("please give a sixth number "))

print("Which mathematical operation do you want to run? ")
print("Choose 1 for +")
print("Choose 2 for -")
print("Choose 3 for *")
print("Choose 4 for /")

choice = int(input("Your choice: "))

if choice == 1:
    result1 = no1 + no2
    print(f"{result1} is the result of the addition")

elif choice == 2:
    result2 = no1 - no2
    print(f"{result2} is the result of the substraction")

elif choice == 3:
    result3 = no1 * no2
    print(f"{result3} is the result of the multiplication")

elif choice == 4:
    result4 = no1 / no2
    print(f"{result4} is the result of the division")

else:
    print("I said a NUMBER BETWEEN 1 and 4")
