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


# Testing function
def test_palindrome():
    """Function to test various palindrome cases"""
    
    test_cases = [
        "radar",           # Palindrome with odd number of characters
        "Radar",           # Palindrome with different case
        "noon",            # Palindrome with even number of characters
        "A man a plan a canal Panama",  # Palindrome with spaces
        "race car",        # Palindrome with space
        "Was it a car or a cat I saw",  # Complex palindrome
        "hello",           # Not a palindrome
        "python",          # Not a palindrome
        "a",               # Palindrome with one character
        "aa",              # Palindrome with two identical characters
        "ab",              # Not a palindrome with two different characters
        "Madam",           # Palindrome with different case
        "Level",           # Palindrome
        "civic",           # Palindrome
        "Mr Owl ate my metal worm",  # Palindrome with spaces
        ""                 # Empty string (considered a palindrome)
    ]
    
    print("=" * 60)
    print("PALINDROME CHECKER USING DEQUE")
    print("=" * 60)
    
    for test_string in test_cases:
        result = is_palindrome(test_string)
        status = "✓ PALINDROME" if result else "✗ NOT A PALINDROME"
        display_string = f"'{test_string}'" if test_string else "'(empty string)'"
        print(f"\n{display_string}")
        print(f"  {status}")
    
    print("\n" + "=" * 60)


# Interactive version
def interactive_palindrome_checker():
    """Interactive program to check palindromes"""
    
    print("\n" + "=" * 60)
    print("   INTERACTIVE PALINDROME CHECKER")
    print("=" * 60)
    print("\nEnter a string to check (or 'exit' to quit)")
    
    while True:
        user_input = input("\nYour string: ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("\n✓ Program terminated")
            break
        
        if not user_input.strip():
            print("⚠ Empty string detected. By definition, it is a PALINDROME!")
            continue
        
        result = is_palindrome(user_input)
        
        if result:
            print(f"✓ '{user_input}' is a PALINDROME!")
        else:
            print(f"✗ '{user_input}' is NOT a palindrome")
        
        # Show processing details
        cleaned = ''.join(user_input.split()).lower()
        print(f"   (Processed string: '{cleaned}')")


# Main function
def main():
    # Run tests
    test_palindrome()


if __name__ == "__main__":
    main()
