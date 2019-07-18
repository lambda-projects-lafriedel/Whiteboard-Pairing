# function that returns number of non-zero ints and reorders the same array

def howManyNonZeros(arr):
  # variable to hold the amount of non-zero integers
  num = 0
  # for loop on the array
  for i in range(len(arr)):
    if arr[i] is not 0:
      num += 1
      removed = arr.pop(i)
      arr.insert(0, removed)
    # if the value is greater than 0, increase num variable by one
    # and remove that value from its current pos and insert it at the zeroth index
  return num

array = [0, 3, 1, 0, -2]
print(howManyNonZeros(array))