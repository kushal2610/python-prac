pet = input("Species of your pet: ").lower()
age = int(input(f"Age of your {pet}?"))

if pet == "dog" and age < 2:
    print("Your pet needs puppy dog food")
elif pet == 'cat' and age >5:
    print('Your cat needs Senior cat food ')
else:
    print("I have no idea!")