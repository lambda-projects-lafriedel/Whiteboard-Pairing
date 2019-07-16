import numpy

def productOfAllNums(arr):
  # make a dict
  storage = dict()
  products = list()
  # loop through the array
  for num in arr:
    if num not in storage:
      # storage[num] = 1
      storage[num] = []
    for j in range(len(arr)):
      if arr[j] == num:
        continue
      else:
        # storage[num] = storage[num] * arr[j]
        storage[num].append(arr[j])
    # products.append(storage[num])
    products.append(numpy.prod(storage[num]))

  # return list
  return products

array = [1,7,3,4]
print(productOfAllNums(array))