import random

letters = ['a','b','c','d','e','f','g','h','i','j']
nums = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&']

passmaker = [letters,nums,symbols]

user_l = int(input("How Many Letters Do You want in your Password ?"))
user_n = int(input("How Many numbers Do You want in your Password ?"))
user_s = int(input("How Many symbols Do You want in your Password ?"))

length = user_l + user_n + user_s

password = ""

for i in range(0,length):
    choice = random.choice(passmaker)
    if choice == letters and user_l != 0:
        password += random.choice(letters)
        user_l -= 1
    elif choice == nums and user_n != 0:
        password += random.choice(nums)
        user_n -= 1
    elif choice == symbols and user_s != 0:
        password += random.choice(symbols)
        user_s -= 1

print("Bharat")
print(f"Your Password is {password}")
print("Hello world")
