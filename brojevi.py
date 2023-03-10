numbers = list(range(1, 31))  # stvaramo listu od 1 do 30

for num in numbers:
    if num % 3 == 0:  # provjeravamo je li broj djeljiv s 3
        print(num, "je djeljiv sa 3")
    if num % 6 == 0:  # provjeravamo je li broj djeljiv s 6
        print(num, "je djeljiv sa 6")
    if num % 9 == 0:  # provjeravamo je li broj djeljiv s 9
        print(num, "je djeljiv sa 9")

numbers = list(range(1, 31))  # stvaramo listu od 1 do 30

for num in numbers:
    if num % 3 == 0 and num % 6 == 0 and num % 9 == 0:  
        # provjeravamo je li broj djeljiv s 3, 6 i 9
        print(num, "je djeljiv sa 3, 6 i 9")
    elif num % 3 == 0 and num % 6 == 0:  
        # provjeravamo je li broj djeljiv s 3 i 6, ali ne s 9
        print(num, "je djeljiv sa 3 i 6")
    elif num % 3 == 0:  
        # provjeravamo je li broj djeljiv samo s 3
        print(num, "je djeljiv sa 3")
