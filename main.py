x=int(input('How many letters do you need in your password'))
y=int(input('How many symbols do you need in your password'))
z=int(input('How many numbers do you need in your password'))
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
k=[]
for i in range(0,x):
  k.append(random.choice(letters))
for j in range(0,y):
  k.append(random.choice(numbers))
for l in range(0,z):
  k.append(random.choice(symbols))


random.shuffle(k)

password=''
for m in range(x+y+z):
  password+=k[m]
print(password)
