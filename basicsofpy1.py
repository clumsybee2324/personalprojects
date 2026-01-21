weight=int(input("Enter your weight: "))
weigth_type=input("Enter your weight type: ")
if weigth_type.lower()=='l':
    new_weight=weight*9//20
    print(f"You are {new_weight} kilograms")
elif weigth_type.lower()=="k":
    new_weight=weight*20//9
    print(f"You are {new_weight} lbs")
else:
    print("Please enter accurate value! ")
