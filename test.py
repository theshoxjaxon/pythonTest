"""
x = int(input("Please enter a number to check: "))
if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print("This number is", x)


"""

# ! Task 2

# num = int(input("Please enter a number: "))

# if(num % 2 == 0):
#     print("The number is even")
# else:
#     print("The number is odd")


# ! Task 3
# sum = 0

# for num in range(1, 10):
#     sum = num + sum

# print(sum)


# ! Task 4
# import random
# guessNum = random.randrange(0, 10)
# guess = int(input("Guess a number between 0 and 10: "))

# while guess != guessNum:
#     if guess < guessNum:
#         print("Your guess is too low")
#     else:
#         print("Your guess is too high")

#     # Prompt for another guess
#     guess = int(input("Guess a number between 0 and 10: "))

# # The loop ends when the guess is correct
# print("You found it! The number was", guessNum)

# ? How to do , after a  while loop, to print the number that was guessed
# x = float(input("Please enter a number: "))
# y = float(input("Please enter another number: "))

# z = x + y
# z = round(x + y)
# print("The sum of the two numbers is", f"{z:,}")


# def main():
#     print("Hello World")
#     print("This is a new line")

# main()


# Ex 1.

# for x in range(7, 78):
#     if(x % 15 == 0):
#         print(x)

# x = str(input("Please enter your name"))

# # Reverse the string and convert it to uppercase
# print(x[::-1].upper())


# x = str(input("Please enter your name"))
# print(''.join(reversed(x)).capitalize())


# x = str(input("Please enter your name"))
# print(x[::-1].cp() + x[1:-1] + x[-1].capitalize())


# name = input("Please enter your name")

# rn = name[:: -1].capitalize()
# print(name[1:-1] + rn)
# def main():
#     x = get_in()
#     print(" You entered:", x)


# def get_in():
#     while True:
#         try:
#             return int(input(" Please enter a number: "))
#         except ValueError:
#             pass


# main()

# while True:
#     try:
#         x = int(input(" Please enter a number: "))
#         y = int(input("Please enter a divided number: "))
#         result = x / y
#     except (ZeroDivisionError, ValueError):
#         print("Are you sure about that ?")
#     else:
#         break
# print("the answer is", result)


# import random
# userInput = int(  input("Please enter a number between 1 and 10: "))
# x =  random.randint(1, 10)
# while  userInput != x:
#     if userInput < x:
#         print("Your number is too low")
#     else:
#         print("Your number is too high")
#     userInput = int(  input("Please enter a number between 1 and 10: "))
# print(x)

# import sys
# if len(sys.argv) < 2:
#     sys.exit("Too few  arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("hello my name is", sys.argv[1])


# def plusOne(digit):
#     for i in  range(len(digit)-1, -1, -1):
#         if digit[i] == 9:
#             digit[i] = 0
#         else:
#             digit[i] += 1
#             return digit
#     return [1] + digit


# print(plusOne([1,2,3]))  # Output: [1,2,4]
# print(plusOne([4,3,2,1]))  # Output: [4,3,2,2]
# print(plusOne([9]))  # Output: [1,0]


thisList = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
for item in range(len(thisList)):
    print(thisList[item])  # Output: Apple, Banana, Cherry, Date, Elderberry
