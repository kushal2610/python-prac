def kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

kwargs(name = "Kushal", surname = "Joshi")