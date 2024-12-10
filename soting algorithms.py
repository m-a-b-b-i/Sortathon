import random
import time
import matplotlib.pyplot as plt

# Sorting Algorithms

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def radix_sort(arr):
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in arr:
            index = (i // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        for i in range(n):
            arr[i] = output[i]

    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def bucket_sort(arr):
    if len(arr) == 0:
        return
    bucket = []
    bucket_count = 10
    max_val = max(arr)
    min_val = min(arr)
    range_per_bucket = (max_val - min_val) / bucket_count
    for _ in range(bucket_count):
        bucket.append([])

    for num in arr:
        bucket_index = int((num - min_val) // range_per_bucket)
        if bucket_index == bucket_count:
            bucket_index -= 1
        bucket[bucket_index].append(num)

    arr.clear()
    for i in range(bucket_count):
        bucket[i].sort()
        arr.extend(bucket[i])

def tim_sort(arr):
    arr.sort()  # Python's built-in Timsort implementation

# Helper Function for Time Measurement
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Main Functionality
def main():
    print("Enhanced Sortathon: Sorting Algorithms Comparison")
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": lambda arr: quick_sort(arr),
        "Heap Sort": heap_sort,
        "Radix Sort": radix_sort,
        "Counting Sort": counting_sort,
        "Shell Sort": shell_sort,
        "Bucket Sort": bucket_sort,
        "Tim Sort": tim_sort
    }

    n = int(input("Enter the size of the array to sort: "))
    array = [random.randint(1, 10000) for _ in range(n)]

    results = {}

    for name, func in algorithms.items():
        test_array = array.copy()
        print(f"Testing {name}...")
        time_taken = measure_time(func, test_array)
        results[name] = time_taken
        print(f"{name} took {time_taken:.6f} seconds")

    # Display Results
    print("\nPerformance Summary:")
    for name, time_taken in results.items():
        print(f"{name}: {time_taken:.6f} seconds")

    # Plot Results
    plt.bar(results.keys(), results.values(), color='skyblue')
    plt.xlabel('Sorting Algorithm')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
