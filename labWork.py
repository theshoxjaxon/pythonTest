# ! Python First Lab
import math


def main():
    while True:
        x = float(input("Please enter a value for x: "))

        a = x + 3
        b = math.sqrt(2 * (x**3))
        print(f"Intermediate result a = {a}")
        print(f"Intermediate result b = {b}")

        if a < b:
            Y = a + b + (2 * a * b)
            print(f"Y (calculated using the first expression): {Y}")
        else:
            if b - 1 < 0:
                print(
                    "Oops! Computation not possible: can't take sqrt of negative number."
                )
            else:
                Y = math.sqrt(a * (b - 1))
                print(f"Y (calculated using the second expression): {Y}")

        repeat = (
            input("Do you want to repeat this calculation? (yes/no): ").strip().lower()
        )
        if repeat != "yes":
            break


if __name__ == "__main__":
    main()
