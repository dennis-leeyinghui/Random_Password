import random

character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890"
print_char = ""
start = True
    
def get_random_no():
    random_number = random.randrange(0,72)
    return random_number

while start:
    
    for a in range(random.randrange(6,8)):
        print_char += (character[get_random_no()])
        get_random_no()
        
    print (print_char)    
    print_char = ""
    
    ask_stay = input("Do you want to start again? Y/N  ")

    if ask_stay in ("N", "n", "NO"):
        print ("BYE BYE")
        start = False
    
#print (random_password)