def hanoi_towers(n, source='A', auxiliary='B', destination='C', state=None, step_counter=None):
    """
    Recursive function to solve the Tower of Hanoi problem.

    Args:
        n: number of disks to move
        source: source rod
        auxiliary: auxiliary rod
        destination: destination rod
        state: dictionary storing the current state of the rods
        step_counter: step counter (list for pass-by-reference)
    """
    if n > 0:
        # Step 1: Move n-1 disks from source to auxiliary rod
        hanoi_towers(n - 1, source, destination, auxiliary, state, step_counter)

        # Step 2: Move the largest remaining disk from source to destination
        if state is not None:
            disk = state[source].pop()
            state[destination].append(disk)
            step_counter[0] += 1

            print(f"Move disk from {source} to {destination}: {disk}")
            print(f"Intermediate state: {state}")
        else:
            print(f"Move disk from {source} to {destination}")

        # Step 3: Move n-1 disks from auxiliary rod to destination
        hanoi_towers(n - 1, auxiliary, source, destination, state, step_counter)


def solve_hanoi(n):
    """
    Main function to solve the Tower of Hanoi problem.

    Args:
        n: number of disks
    """
    # Initialize the state of rods
    state = {
        'A': list(range(n, 0, -1)),  # [n, n-1, ..., 2, 1]
        'B': [],
        'C': []
    }

    # Step counter
    step_counter = [0]

    print(f"Initial state: {state}")

    # Call the recursive function
    hanoi_towers(n, 'A', 'B', 'C', state, step_counter)

    print(f"Final state: {state}")
    print(f"\nTotal steps: {step_counter[0]}")
    print(f"Minimum possible steps: {2**n - 1}")


def main():
    """
    Entry point of the program.
    """
    try:
        n = int(input("Enter number of disks: "))

        if n <= 0:
            print("The number of disks must be a positive integer!")
            return

        if n > 10:
            confirm = input(f"Warning: {2**n - 1} steps will be required. Continue? (y/n): ")
            if confirm.lower() != 'y':
                return

        print(f"\n{'='*60}")
        print(f"Solution for Tower of Hanoi with {n} disks")
        print(f"{'='*60}\n")

        solve_hanoi(n)

    except ValueError:
        print("Error: Please enter a valid integer!")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")


if __name__ == "__main__":
    main()
