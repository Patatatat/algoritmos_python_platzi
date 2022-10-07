#  def sum(arr):
#    total = 0
#    for x in arr:
#      total += x
#    return total
#  print(sum([1, 2, 3, 4]))


# def sum(list):
  #if list == []:
    #return 0
  #return list[0] + sum(list[1:])

# def count(list):
#  if list == []:
#    return 0
#  return 1 + count(list[1:])

#print(count(list= [1, 8, 5, 6, 2])) # ==> 5

# def max(list):
#  if len(list) == 2:
#    return list[0] if list[0] > list[1] else list[1]
#  sub_max = max(list[1:])
#  return list[0] if list[0] > sub_max else sub_max

#print(max(list= [2, 9, 1, 10])) # ==> 10

#print(sum(list= [1, 2, 3]))

#def quicksort(array):
  #if len(array) < 33:
    #return array

#print(quicksort(array=[15, 10, 33]))

def quicksort(array):
  if len(array) < 2:
    return array 
  else:
    pivot = array[0] 
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
  return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort([10, 70, 521, 3]))