# -->                 Bubble sorting

# def bubble_sort(arr):
#     n = len(arr)
    
#     # Traverse through all array elements
#     for i in range(n-1):
        
#         # Last i elements are already in place
#         for j in range(0, n-1):
            
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 temp = arr[j]
#                 arr[j]= arr[j+1]
#                 array[j+1] = temp

# array = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(array)
# print("Sorted array:", array)


# -->                 Selection sorting

# def selection_sort(arr):
#     n = len(arr)
    
#     # Traverse through all array elements
#     for i in range(n):
#         # Find the minimum element in the remaining unsorted array
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
                
#         # Swap the found minimum element with the first element
#         arr[i], arr[min_index] = arr[min_index], arr[i]

# # Example usage
# array = [64, 34, 25, 12, 22, 11, 90]
# selection_sort(array)
# print("Sorted array:", array)


# -->                 Insert sorting

def insertion_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key element at its correct position in the sorted part of the array
        arr[j + 1] = key

# Example usage
array = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(array)
print("Sorted array:", array)

