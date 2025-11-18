first = input ("Please type in the first number:")
num = int(first)
second = input ("Please type another number:")
num = int(second)
if first > second:
    print("The greater number was",first)
elif first < second:
    print("The greater number was",second)
else:
    print("Error")
