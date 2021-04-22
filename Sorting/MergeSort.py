# MEJBAH AHAMMAD
# Merge Sort Algorithm

def merge(a, b):
  """Function to merge two arrays """
  c = [] # Create empty list
  while len(a) !=0 and len(b) !=0:
    if a[0] < b[0]:
      c.append(a[0])
      a.remove(a[0])
      
     else:
      c.append(b[0])
      b.remove(b[0])
      
     
  if len(a) == 0:
    c+=b
  else:
    c+=a
    
  return c


def mergeSort(list):
  """ Function to sort an array using merge sort algorithm """
  if len(list) == 0 or len(list) == 1:
    return list
  else:
    middle = len(x) //2
    a = mergeSort(list[:middle])
    b = mergeSort(list[middle:])
    retrun merge(a, b)
    
if __name__ == "__main__":
  list = [3, 4, 2, 6, 5, 7, 1, 9]
  print("Sorted List: ", mergeSort(list))