# Sortathon

# Enhanced Sortathon: Sorting Algorithms Comparison

This project compares the performance of various sorting algorithms. The goal is to understand their behavior and efficiency across different datasets by measuring the execution time for sorting an array of random integers.

---

## **Table of Contents**
1. [Project Description](#project-description)
2. [Implemented Sorting Algorithms](#implemented-sorting-algorithms)
    - [Bubble Sort](#bubble-sort)
    - [Selection Sort](#selection-sort)
    - [Insertion Sort](#insertion-sort)
    - [Merge Sort](#merge-sort)
    - [Quick Sort](#quick-sort)
    - [Heap Sort](#heap-sort)
    - [Radix Sort](#radix-sort)
    - [Counting Sort](#counting-sort)
    - [Shell Sort](#shell-sort)
    - [Bucket Sort](#bucket-sort)
    - [Tim Sort](#tim-sort)
3. [How to Run](#how-to-run)
4. [Visualization](#visualization)
5. [License](#license)

---

## **Project Description**

This project implements and benchmarks the performance of 11 popular sorting algorithms. It generates random arrays of integers and measures the time taken to sort these arrays. The results are visualized using a bar chart.

---

## **Implemented Sorting Algorithms**

### **Bubble Sort**
- **Description**: Repeatedly compares adjacent elements and swaps them if they are out of order. The largest element "bubbles up" to its correct position in each pass.
- **Complexity**:
  - Best: \(O(n)\) (nearly sorted arrays)
  - Worst: \(O(n^2)\)
- **Characteristics**: Easy to implement but inefficient for large datasets.

---

### **Selection Sort**
- **Description**: Divides the array into sorted and unsorted regions. Finds the smallest element in the unsorted region and swaps it into the sorted region.
- **Complexity**:
  - Best & Worst: \(O(n^2)\)
- **Characteristics**: Performs fewer swaps but is not suitable for large datasets.

---

### **Insertion Sort**
- **Description**: Builds the sorted array one element at a time by inserting each element in its correct position within the sorted region.
- **Complexity**:
  - Best: \(O(n)\) (nearly sorted arrays)
  - Worst: \(O(n^2)\)
- **Characteristics**: Works well for small or nearly sorted datasets.

---

### **Merge Sort**
- **Description**: A divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and merges them into a sorted array.
- **Complexity**: 
  - All cases: \(O(n \log n)\)
- **Characteristics**: Stable, efficient for large datasets, but requires additional memory.

---

### **Quick Sort**
- **Description**: Partitions the array around a pivot element such that smaller elements are on one side and larger on the other. Recursively sorts the partitions.
- **Complexity**:
  - Best & Average: \(O(n \log n)\)
  - Worst: \(O(n^2)\) (poor pivot choice)
- **Characteristics**: Fast in practice; in-place sorting.

---

### **Heap Sort**
- **Description**: Constructs a max-heap or min-heap from the array and repeatedly extracts the root (largest or smallest) to sort the array.
- **Complexity**:
  - All cases: \(O(n \log n)\)
- **Characteristics**: Memory-efficient, but not stable.

---

### **Radix Sort**
- **Description**: A non-comparative sorting method that sorts numbers digit by digit, starting from the least significant digit.
- **Complexity**: 
  - Worst: \(O(d \cdot (n + b))\), where \(d\) is the number of digits and \(b\) is the base.
- **Characteristics**: Very efficient for integers or strings of fixed length.

---

### **Counting Sort**
- **Description**: Counts the frequency of each element and uses this to sort. Works only for non-negative integers.
- **Complexity**: 
  - All cases: \(O(n + k)\), where \(k\) is the range of input values.
- **Characteristics**: Space-efficient for small ranges of integers.

---

### **Shell Sort**
- **Description**: A variation of Insertion Sort that starts by sorting far-apart elements and reduces the gap incrementally.
- **Complexity**: 
  - Worst: \(O(n^{2})\) (depends on gap sequence)
- **Characteristics**: More efficient than Insertion Sort for large datasets.

---

### **Bucket Sort**
- **Description**: Distributes elements into buckets, sorts each bucket, and then concatenates them. Effective for uniformly distributed data.
- **Complexity**:
  - Average: \(O(n + k)\), where \(k\) is the number of buckets.
- **Characteristics**: Requires a good choice of bucket ranges.

---

### **Tim Sort**
- **Description**: A hybrid sorting algorithm combining Merge Sort and Insertion Sort. It divides the array into small runs, sorts each run, and merges them.
- **Complexity**: 
  - All cases: \(O(n \log n)\)
- **Characteristics**: Python's built-in `sort()` function uses Tim Sort.

---

## **How to Run**

1. Install the required library:
   ```bash
   pip install matplotlib

2. Run the script:
   '''bash
     python sortathon.py
3.Input the size of the array when prompted.

Visualization
The program generates a bar chart comparing the time taken by each sorting algorithm to sort the same dataset.

License
This project is licensed under the MIT License.

vbnet

This README provides detailed descriptions of the algorithms, their use cases, and how to use the project.  
