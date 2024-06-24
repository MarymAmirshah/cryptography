#import random
import random

from sympy import mod_inverse

def generate_polynomial(secret, threshold, prime):
    coefficients = [secret] + [random.randint(0, prime - 1) for _ in range(threshold - 1)]
    return coefficients

def evaluate_polynomial(coefficients, x, prime):
    result = 0
    for i, coefficient in enumerate(coefficients):
        result = (result + coefficient * pow(x, i, prime)) % prime
    return result

def generate_shares(secret, threshold, num_shares, prime):
    coefficients = generate_polynomial(secret, threshold, prime)
    shares = [(x, evaluate_polynomial(coefficients, x, prime)) for x in range(1, num_shares + 1)]
    return shares

def lagrange_interpolation(x, x_s, y_s, prime):
    def basis(j):
        b = 1
        for m in range(len(x_s)):
            if m != j:
                b = b * (x - x_s[m]) * mod_inverse(x_s[j] - x_s[m], prime) % prime
        return b

    result = 0
    for j in range(len(x_s)):
        result = (prime + result + y_s[j] * basis(j)) % prime
    return result

def reconstruct_secret(shares, prime):
    x_s, y_s = zip(*shares)
    return lagrange_interpolation(0, x_s, y_s, prime)

# Input parameters
S = int(input("Enter the secret: "))
t = int(input("Enter the threshold number of shares (t): "))
n = int(input("Enter the total number of shares (n): "))
p = int(input("Enter a prime number (p): "))

# Generate and display shares
shares = generate_shares(S, t, n, p)
print("\nGenerated Shares:")
for share in shares:
    print(share)

# Example of reconstructing the secret from any t shares
# Here we take the first t shares for reconstruction, but in practice any t shares can be used
subset_of_shares = shares[:t]
reconstructed_secret = reconstruct_secret(subset_of_shares, p)

print(f"\nReconstructed Secret: {reconstructed_secret}")

# Verify the reconstruction
if S == reconstructed_secret:
    print("Secret reconstruction successful!")
else:
    print("Secret reconstruction failed.")
