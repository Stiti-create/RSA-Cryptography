import math
import random

text = input()
numerical = 0
for c in text:
    numerical=numerical*10 + (ord(c)-96)
    

p = int(input())
q = int(input())
n = p*q

phi = (p-1)*(q-1)

for i in range(2,phi):
    if (math.gcd(phi,i))==1:
        e = i
        break

for k in range(1,100):
    if(((k*phi)+1)%e==0):
        d = ((k*phi)+1)//e
        break
        
encrypt = (numerical**e)%n
print(encrypt)
decrypted = (encrypt**d)%n
print(decrypted)
decrypt = decrypted
decrypt_text = ""
while (decrypt>0):
    g = decrypt%10
    decrypt_text=chr(int(g+96))+decrypt_text
    decrypt = decrypt//10
    print(decrypt)
    
    

print("The given text is: ", end="")
print(text, end="\n")
print("The encrypted data is: ", end="")
print(encrypt, end="\n")
print("The decrypted data is: ", end="")
print(decrypted, end="\n")
print("The decrypted text is: ", end="")
print(decrypt_text, end="\n")


