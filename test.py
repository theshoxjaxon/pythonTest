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


def main():
    print("Hello World")
    print("This is a new line")

main()