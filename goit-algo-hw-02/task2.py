from collections import deque


def is_palindrome(input_string):
    """
    Checks if a string is a palindrome using deque.

    Args:
        input_string: String to check

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase
    cleaned_string = ''.join(input_string.split()).lower()

    # Create a deque and add all characters
    char_deque = deque(cleaned_string)

    # Compare characters from both ends
    while len(char_deque) > 1:
        # Remove and compare characters from both ends
        front_char = char_deque.popleft()  # Character from the front
        back_char = char_deque.pop()       # Character from the back

        if front_char != back_char:
            return False

    # If all characters matched, the string is a palindrome
    return True


# Main program starts here
print("=" * 60)
print("   INTERACTIVE PALINDROME CHECKER")
print("=" * 60)
print("\nEnter a string to check (or type 'exit' to quit)")
print("-" * 60)

while True:
    user_input = input("\nYour string: ")

    # Check if user wants to exit
    if user_input.lower() in ['exit', 'quit', 'q']:
        print("\n✓ Program terminated. Goodbye!")
        break

    # Handle empty string
    if not user_input.strip():
        print("⚠ Empty string detected. By definition, it is a PALINDROME!")
        continue

    # Check if palindrome
    result = is_palindrome(user_input)

    if result:
        print(f"✓ '{user_input}' is a PALINDROME!")
    else:
        print(f"✗ '{user_input}' is NOT a palindrome")

    # Show processing details
    cleaned = ''.join(user_input.split()).lower()
    print(f"   (Processed string: '{cleaned}')")
