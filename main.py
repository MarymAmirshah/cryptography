import random
import numpy as np


def is_prime(x: int) -> bool:
    """Check if a number is prime."""
    if x < 2:
        return False
    elif x == 2:
        return True
    for i in range(2, int(np.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def share_secret():
    """Share a secret using Shamir's Secret Sharing Scheme."""
    print("----SECRET SHARING----")

    # Input the number of shares (n) and the threshold (t)
    while True:
        try:
            n = int(input("Enter the number of shares (n): "))
            t = int(input("Enter the threshold (t): "))
            if n >= t:
                break
            else:
                print("n should be greater than or equal to t.")
        except ValueError:
            print("Please enter valid integers.")

    # Input the secret (S) and a prime number (p)
    while True:
        try:
            S = int(input("Enter the secret (S): "))
            while True:
                p = int(input("Enter a prime number (p) greater than S: "))
                if is_prime(p) and p > S:
                    break
                else:
                    print("Please enter a prime number greater than S.")
            break
        except ValueError:
            print("Please enter valid integers.")

    # Generate random coefficients for the polynomial
    a = np.zeros(t)
    a[0] = S
    for i in range(1, t):
        a[i] = random.randint(-10, 10)

    # Generate shares
    x = np.arange(1, n + 1)
    y = np.zeros(n)
    for i in range(n):
        y[i] = sum(a[j] * pow(x[i], j) for j in range(t)) % p

    # Print the shares
    print("\nGenerated shares (x, y):")
    for i in range(n):
        print(f"({int(x[i])}, {int(y[i])})")


def mod_inverse(a: int, p: int) -> int:
    """Calculate the modular inverse of a under modulo p."""
    for i in range(1, p):
        if (a * i) % p == 1:
            return i
    return 1


def get_secret():
    """Reveal the secret using Shamir's Secret Sharing Scheme."""
    print("----SECRET REVEALING----")

    # Input the threshold (t)
    while True:
        try:
            t = int(input("Enter the threshold (t): "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Input the prime number (p)
    while True:
        try:
            p = int(input("Enter a prime number (p): "))
            if is_prime(p):
                break
            else:
                print("Please enter a valid prime number.")
        except ValueError:
            print("Please enter a valid integer.")

    # Input the shares (x, y)
    x = np.zeros(t)
    y = np.zeros(t)
    for i in range(t):
        while True:
            try:
                x[i] = int(input(f"Enter x[{i + 1}]: "))
                y[i] = int(input(f"Enter y[{i + 1}]: "))
                break
            except ValueError:
                print("Please enter valid integers.")

    # Reconstruct the secret using Lagrange Interpolation
    S = 0
    for i in range(t):
        numerator = 1
        denominator = 1
        for j in range(t):
            if i != j:
                numerator = (numerator * -x[j]) % p
                denominator = (denominator * (x[i] - x[j])) % p
        S = (S + y[i] * numerator * mod_inverse(denominator, p)) % p

    # Print the reconstructed secret
    print(f"\nReconstructed secret: S = {int(S)}")


def main():
    """Main function to choose between sharing and revealing a secret."""
    while True:
        print("\nChoose an option:")
        print("1. Share a secret")
        print("2. Reveal a secret")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            share_secret()
        elif choice == '2':
            get_secret()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
