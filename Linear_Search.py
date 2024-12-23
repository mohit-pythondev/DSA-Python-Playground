def linear_search(arr, target):
    # Iterate through the list
    for i in range(len(arr)):
        # Check if the current element is the target
        if arr[i] == target:
            return i  # Return the index of the found element
    return -1  # Return -1 if the element is not found

# Example usage 
arr = [2, 4, 6, 8, 10]
target = 8
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
