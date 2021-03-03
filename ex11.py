def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1},arg2:{arg2}")
    
def print_two_again(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")
    
def print_1(arg1):
    print(f"arg1:{arg1}")
    
def print_nothing():
    print("I got nothing...")
    
print_two('Seeder', 1)
print_two_again('Harrison', 23)
print_1(900)
print_nothing()