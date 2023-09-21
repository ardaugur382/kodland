import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


parola_uzunlugu = int(input("şifreniz ne kadar uzun olsun"))

parola= ""

for i in range(parola_uzunlugu):
    parola += random.choice(chars)


print(parola)    
