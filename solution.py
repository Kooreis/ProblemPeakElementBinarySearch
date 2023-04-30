Here is a Python console application that finds a peak element in an array using binary search:

```python
def find_peak(arr, low, high, n):
    mid = low + (high - low) / 2
    mid = int(mid)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid

    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return find_peak(arr, low, (mid - 1), n)

    else:
        return find_peak(arr, (mid + 1), high, n)

def main():
    arr = [1, 3, 20, 4, 1, 0]
    n = len(arr)
    print("Index of a peak point is", find_peak(arr, 0, n - 1, n))

if __name__ == "__main__":
    main()
```

This Python console application first defines a function `find_peak` that uses binary search to find a peak element in an array. The function takes four arguments: the array, the low index, the high index, and the length of the array. It calculates the mid index and checks if the element at the mid index is a peak element. If it is, it returns the mid index. If it's not, it recursively calls itself on the half of the array where a peak element could be.

The `main` function initializes an array and calls the `find_peak` function on it. It then prints the index of the peak element.

The application is run by calling the `main` function in the `if __name__ == "__main__":` block. This block ensures that the `main` function is only run when the script is run directly, not when it's imported as a module.