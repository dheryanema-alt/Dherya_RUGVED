#Write a Python function to perform selection sort on a given string
def selection_Sort(a):
    arr =list(a)
    for i in range (len(a)):
        min_index=i
        for j in range (i+1,len(a)):
            if arr[j]<arr[i]:
                min_index=j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return ''.join(arr)
a = input("Enter a string: ")
print("Sorted string:", selection_Sort(a))

