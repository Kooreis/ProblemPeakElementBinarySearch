Here is a Java console application that finds a peak element in an array using binary search:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array:");
        int n = scanner.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }
        int index = findPeakElement(nums);
        System.out.println("Peak element is " + nums[index] + " at index " + index);
    }

    public static int findPeakElement(int[] nums) {
        return search(nums, 0, nums.length - 1);
    }

    public static int search(int[] nums, int l, int r) {
        if (l == r)
            return l;
        int mid = (l + r) / 2;
        if (nums[mid] > nums[mid + 1])
            return search(nums, l, mid);
        return search(nums, mid + 1, r);
    }
}
```

This program first takes the number of elements in the array and the elements of the array as input from the user. It then calls the `findPeakElement` method with the array as the argument. This method calls the `search` method with the array and the start and end indices of the array as arguments. The `search` method recursively finds the peak element in the array using binary search and returns its index. The peak element and its index are then printed to the console.