# compare_sorting.py
import random
import timeit

# Insertion Sort

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Run benchmarks

def benchmark():
    sizes = [1000, 5000, 10000, 20000]
    results = []

    for n in sizes:
        data = [random.randint(0, 1000000) for _ in range(n)]

        print(f"\n--- Array size: {n} ---")

        t_ins = timeit.timeit(lambda: insertion_sort(data), number=1)
        t_merge = timeit.timeit(lambda: merge_sort(data), number=1)
        t_timsort = timeit.timeit(lambda: sorted(data), number=1)

        print(f"Insertion Sort: {t_ins:.4f} sec")
        print(f"Merge Sort:     {t_merge:.4f} sec")
        print(f"Timsort:        {t_timsort:.4f} sec")

        results.append((n, t_ins, t_merge, t_timsort))

    return results

# Main execution

def main():
    print("Running sorting benchmarks...\n")
    results = benchmark()

    print("\n\n--- Summary Table ---")
    print(f"{'Size':>8} | {'Insertion':>10} | {'Merge':>10} | {'Timsort':>10}")
    print("-" * 50)
    for n, ins, merge, tim in results:
        print(f"{n:>8} | {ins:>10.4f} | {merge:>10.4f} | {tim:>10.4f}")

    print("\nBenchmark complete!")
    print("See readme.md for conclusions.")


if __name__ == "__main__":
    main()
