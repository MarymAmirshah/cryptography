import random


def generate_shares(S, t, n, p):
    # Generate a random polynomial of degree t-1 with S as the constant term
    coefficients = [S] + [random.randint(0, p - 1) for _ in range(t - 1)]

    # Function to evaluate polynomial at a given x
    def eval_polynomial(x):
        result = 0
        for i, coeff in enumerate(coefficients):
            result = (result + coeff * pow(x, i, p)) % p
        return result

    # Generate n shares (x, y)
    shares = [(i, eval_polynomial(i)) for i in range(1, n + 1)]

    return shares


# Example usage
S = 1234  # Secret
t = 3  # Threshold
n = 5  # Number of shares
p = 7919  # Prime number larger than S

shares = generate_shares(S, t, n, p)
print("Shares (x, y):")
for share in shares:
    print(share)


def reconstruct_secret(shares, t, p):
    # Function to compute Lagrange basis polynomial
    def lagrange_basis(j, x):
        basis = 1
        for m in range(t):
            if m != j:
                numerator = (x - shares[m][0]) % p
                denominator = (shares[j][0] - shares[m][0]) % p
                inv_denominator = pow(denominator, -1, p)  # Modular multiplicative inverse
                basis = (basis * numerator * inv_denominator) % p
        return basis

    # Reconstruct the secret using Lagrange interpolation
    secret = 0
    for j in range(t):
        y_j = shares[j][1]
        secret = (secret + y_j * lagrange_basis(j, 0)) % p

    return secret


# Example usage
t = 3
n = 5
p = 7919
shares = [(1, 2345), (2, 6789), (3, 5678)]  # Example shares (x, y)

reconstructed_secret = reconstruct_secret(shares, t, p)
print("Reconstructed Secret:", reconstructed_secret)
