def is_prime(n):
    """Check if a given number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def binary_to_decimal(binary):
    """Convert a binary string to a decimal number."""
    return int(binary, 2)

def prime_detector_circuit(binary_input):
    """
    Simulate a circuit to detect if the binary input is a prime number.
    Input: 7-bit binary string (for numbers between 10 and 99).
    Output: 1 if prime, 0 if not prime.
    """
    decimal_number = binary_to_decimal(binary_input)

    # Check if the number is within two-digit range (10 to 99)
    if 10 <= decimal_number <= 99:
        # Check if the number is prime
        if is_prime(decimal_number):
            return 1  # Prime
        else:
            return 0  # Not Prime
    else:
        return 0  # Out of range or not valid

# Example Usage
binary_inputs = ["0001011", "0011001", "0101011", "1100001"]  # Binary for 11, 25, 43, 97

for binary in binary_inputs:
    output = prime_detector_circuit(binary)
    print(f"Input (Binary): {binary}, Output: {output}")
