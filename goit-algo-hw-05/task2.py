def binary_search_with_upper_bound(arr, target):
    """
    Binary search for a sorted array of floating-point numbers.
    Returns a tuple: (iteration_count, upper_bound)

    Parameters:
        arr (list of float): Sorted list of numbers
        target (float): Value to search for

    Returns:
        tuple:
            iterations (int): Number of iterations needed to determine the result
            upper_bound (float or None): The smallest element >= target,
                                         or None if no such element exists
    """

    # Handle empty list
    if not arr:
        return (0, None)

    iterations = 0
    left = 0
    right = len(arr) - 1
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        # If arr[mid] is >= target, it may be the new upper bound
        if arr[mid] >= target:
            upper_bound = arr[mid]
            right = mid - 1  # Try to find a smaller valid element
        else:
            left = mid + 1  # Search in the right half

    return (iterations, upper_bound)

arr = [0.5, 1.2, 2.8, 3.3, 4.7, 5.0, 7.1]

print(binary_search_with_upper_bound(arr, 3.0))  # (iterations, 3.3)
print(binary_search_with_upper_bound(arr, 4.7))  # (iterations, 4.7)
print(binary_search_with_upper_bound(arr, 7.5))  # (iterations, None)
print(binary_search_with_upper_bound(arr, 0.1))  # (iterations, 0.5)
print(binary_search_with_upper_bound([], 5))     # (0, None)