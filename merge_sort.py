# def merge(left, right):
    
#     result = []
#     n, m = 0, 0
#     while n < len(left) and m < len(right):
#         if left[n] <= right[m]:
#             result.append(left[n])
#             n += 1
#         else:
#             result.append(right[m])
#             m += 1

#     result += left[n:]
#     result += right[m:]
#     return result


# def sort(seq):
#     if len(seq) <= 1:
#         return seq

#     middle = int(len(seq) / 2)
#     left = sort(seq[:middle])
#     right = sort(seq[middle:])
#     return merge(left, right)
# l=[1,5,8,57,45,3,5,7,86,8,67,6,45,34,6,5,34,65]
# print(sort(l))
#code for merge sort
def merge_sort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    return arr
arr=[1,5,8,57,45,3,5,7,86,8,67,6,45,34,6,5,34,65]
print(merge_sort(arr))
#Output: [1,3,5,5,5,6,6,7,8,8,34,34,45,45,57,65,67,86]
#Time complexity: O(nlogn)
#Space complexity: O(n)
#Merge sort is a divide and conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
#Merge sort is a stable sorting algorithm. If two elements are equal, their relative order in the sorted array does not change.
#Merge sort is an in-place algorithm. It does not require any extra space.
#Merge sort is not a comparison based algorithm. It can also be applied to sorting linked lists.
#Merge sort is a recursive algorithm.
#In computer science, merge sort is a divide and conquer algorithm that was invented by John von Neumann in 1945.
#It was one of the first sorting algorithms.
#Merge sort is a comparison based algorithm. It is not stable.
#Innitial thoughts:
#1. Divide the array into two halves
#2. Sort the two halves
#3. Merge the two sorted halves
#4. Repeat the above steps until the array is sorted
#Innitialize the left and right subarrays
#1. If the array has only one element, return the array
#2. If the array has more than one element, divide the array into two halves
#3. Sort the two halves
#4. Merge the two sorted halves
#5. Return the sorted array
#6. Merge two sorted arrays
#7. Return the sorted array
#8. Repeat the above steps until the array is sorted
#Algorithm:

#def merge(left, right):
#     result = []
#     n, m = 0, 0
#     while n < len(left) and m < len(right):
#         if left[n] <= right[m]:
#             result.append(left[n])
#             n += 1
#         else:
#             result.append(right[m])
#             m += 1
#     result += left[n:]
#     result += right[m:]
#     return result
#def sort(seq):
#     if len(seq) <= 1:
#         return seq
#     middle = int(len(seq) / 2)
#     left = sort(seq[:middle])
#     right = sort(seq[middle:])
#     return merge(left, right)
