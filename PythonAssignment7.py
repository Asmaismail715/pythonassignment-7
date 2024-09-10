def is_prime(num):
    """Check if the number is prime or not"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    name = input("Enter your name: ")
    num1 = int(input("Enter your first favorite number: "))
    num2 = int(input("Enter your second favorite number: "))
    num3 = int(input("Enter your third favorite number: "))

    numbers = [num1, num2, num3]

    even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

    print(f"\nHello, {name}! Your favorite numbers are:")

    for num, info in even_odd_info:
        print(f"The number {num} is {info}.")

    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num**2})")

    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number.")

if __name__ == "__main__":
    main()
