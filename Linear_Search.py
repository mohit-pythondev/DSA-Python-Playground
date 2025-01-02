def linear_search(arr, target):
    # Iterate through the list
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1


    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    Best Case: O(1)
    Worst Case: O(n)
    """
# Example usage 
arr = [2, 4, 6, 8, 10]
target = 8
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
