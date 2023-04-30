Here is a C# console application that finds a peak element in an array using binary search:

```C#
using System;

class Program
{
    static int FindPeakElement(int[] nums)
    {
        return Search(nums, 0, nums.Length - 1);
    }

    static int Search(int[] nums, int l, int r)
    {
        if (l == r)
            return l;
        int mid = (l + r) / 2;
        if (nums[mid] > nums[mid + 1])
            return Search(nums, l, mid);
        return Search(nums, mid + 1, r);
    }

    static void Main(string[] args)
    {
        int[] nums = { 1, 2, 3, 1 };
        int peak = FindPeakElement(nums);
        Console.WriteLine("Peak element is: " + nums[peak]);
    }
}
```

This program defines a method `FindPeakElement` that uses binary search to find a peak element in an array. The binary search is performed by the `Search` method, which recursively divides the array into two halves until it finds a peak element. The peak element is an element that is greater than its neighbors. In the `Main` method, we define an array and find its peak element using the `FindPeakElement` method. The peak element is then printed to the console.