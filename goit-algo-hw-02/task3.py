def check_delimiters(input_string):
    """
    Checks if delimiters (parentheses, brackets, braces) in a string are balanced.
    Uses a stack to track open delimiters.

    Args:
        input_string: String to check

    Returns:
        tuple: (is_balanced: bool, message: str)
    """
    # Stack to store open delimiters
    stack = []

    # Mapping of closing to opening delimiters
    matching_delimiters = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # Set of opening delimiters
    opening_delimiters = {'(', '[', '{'}

    # Process each character in the string
    for char in input_string:
        # If it's an opening delimiter, push to stack
        if char in opening_delimiters:
            stack.append(char)

        # If it's a closing delimiter
        elif char in matching_delimiters:
            # Check if stack is empty (no matching opening delimiter)
            if not stack:
                return False, "Asymmetric"

            # Pop from stack and check if it matches
            top = stack.pop()
            if top != matching_delimiters[char]:
                return False, "Asymmetric"

    # If stack is empty, all delimiters are balanced
    if not stack:
        return True, "Symmetric"
    else:
        return False, "Asymmetric"


def test_delimiter_checker():
    """Test function with various test cases"""

    test_cases = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }",
        "()",
        "()[]{}",
        "([{}])",
        "((()))",
        "({[]})",
        "({))",
        "(((",
        "}))",
        "",
        "abc",
        "a(b)c[d]e{f}",
        "[(])",
        "{[()()]}",
        "{{[[(())]]}}"
    ]

    print("=" * 70)
    print("   DELIMITER BALANCE CHECKER (USING STACK)")
    print("=" * 70)
    print("\nChecking if delimiters are symmetric...\n")
    print("-" * 70)

    for test in test_cases:
        is_balanced, message = check_delimiters(test)
        status = "✓" if is_balanced else "✗"
        print(f"{status} {test}: {message}")

    print("-" * 70)


def interactive_delimiter_checker():
    """Interactive program to check delimiter balance"""

    print("\n" + "=" * 70)
    print("   INTERACTIVE DELIMITER BALANCE CHECKER")
    print("=" * 70)
    print("\nEnter an expression to check (or type 'exit' to quit)")
    print("Supported delimiters: ( ) [ ] { }")
    print("-" * 70)

    while True:
        user_input = input("\nYour expression: ")

        # Check if user wants to exit
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("\n✓ Program terminated. Goodbye!")
            break

        # Handle empty string
        if not user_input.strip():
            print("⚠ Empty string. No delimiters to check. (Considered Symmetric)")
            continue

        # Check delimiter balance
        is_balanced, message = check_delimiters(user_input)

        if is_balanced:
            print(f"✓ {user_input}: {message}")
        else:
            print(f"✗ {user_input}: {message}")


# Main program
print("=" * 70)
print("RUNNING AUTOMATED TESTS FIRST")
print("=" * 70)

# Run automated tests
test_delimiter_checker()

# Run interactive mode
print("\n\n")
interactive_delimiter_checker()
