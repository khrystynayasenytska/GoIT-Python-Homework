def merge_two_lists(a, b):
    """Merge two sorted lists into one sorted list."""
    i = j = 0
    merged = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # Add remaining elements
    merged.extend(a[i:])
    merged.extend(b[j:])
    
    return merged

def merge_k_lists(lists):
    """Merge k sorted lists using pairwise merging (similar to merge sort)."""
    if not lists:
        return []

    while len(lists) > 1:
        merged_lists = []

        # Merge lists pairwise
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 < len(lists) else []
            merged_lists.append(merge_two_lists(list1, list2))

        lists = merged_lists

    return lists[0]


def run_tests():
    print("Running test cases...\n")

    # Test 1 — Example from the assignment
    lists1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
    result1 = merge_k_lists(lists1)
    print("Test 1 result:", result1)

if __name__ == "__main__":
    run_tests()
