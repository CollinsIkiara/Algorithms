# Luhn Algorithm

# The Luhn algorithm is a simple checksum formula used to validate various identification numbers, such as credit card numbers. It works by doubling every second digit from the right, and if the result is greater than 9, subtracting 9 from it. Then, the sum of all digits is calculated, and if the total modulo 10 is equal to 0, the number is considered valid.
def verify_card_number(card_number):
    # Remove dashes and spaces
    card_number = card_number.replace('-', '').replace(' ', '')
 
    # Luhn algorithm
    digits = [int(d) for d in card_number]
    # Double every second digit from the right (starting at index -2)
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
 
    total = sum(digits)
    return 'VALID!' if total % 10 == 0 else 'INVALID!'
 
 
# Test cases
test_cases = [
    ('453914889',           'VALID!'),
    ('4111-1111-1111-1111', 'VALID!'),
    ('1234 5678 9012 3456', 'INVALID!'),
]

print(test_cases)

## Output:
# [('453914889', 'VALID!'), ('4111-1111-1111-1111', 'VALID!'), ('1234 5678 9012 3456', 'INVALID!')]