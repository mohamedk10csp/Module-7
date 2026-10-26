
def process_numbers(numbers):
    """
Process numbers by doubling even values and tripling odd values.

Args:
    numbers (list): The numbers to process.

Returns:
    list: The processed numbers.
"""
    # Apply the original calculation based on whether each number is even.
    return [
        number * 2 if number % 2 == 0 else number * 3
        for number in numbers
    ]

def process_strings(strings):
    """
Convert strings longer than five characters to uppercase and others to lowercase.

Args:
    strings (list): The strings to process.

Returns:
    str: The processed strings.
"""
    # Keep the original length-based capitalization rule.
    return " ".join(
        [word.upper() if len(word) > 5 else word.lower()
         for word in strings]
    )


def main():
    """Run the number and string processing functions."""
    numbers = [1, 2, 3, 4, 5, 6, 7]
    strings = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(numbers)
    processed_strings = process_strings(strings)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()


