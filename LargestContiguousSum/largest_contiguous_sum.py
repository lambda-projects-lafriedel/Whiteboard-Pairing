def largest_sum(arr):
    # loop through arr of numbers and sum the numbers as I increase the index
    # when the sum becomes negative, slice the array and remove all preceding numbers 
    # when the sum becomes positive, that's when we want to actually log them sum to be returned
    arr_copy = arr
    curr_sum = 0
    for i in range(len(arr_copy)):

        if curr_sum < 0:
            arr_copy = arr[i:]
            curr_sum = arr[i]
            print(arr_copy)

        if sum(arr_copy[:i]) < curr_sum:
            arr_copy = arr_copy[:i]
        else:
            curr_sum += arr[i]
        
        
    return sum(arr_copy)
    


print(largest_sum([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))