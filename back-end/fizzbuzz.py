#Divide by 3 = fizz
#Divide 5 = buzz
#Both = fizzbuzz
value = input("This program will evalue numbers from 1 to x. What you would like x to be? Please only put in a numerical value. \n")
rangeOne = 6;

print("\n")
va1ue = int(value) + 1
for x in range(1, rangeOne):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz!")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)