#MEJBAH AHAMMAD
#Insertion Sort

def insertion_sort(list):
  for i in range(1, len(list)):
    current_number = list[i]
    for j in range(i -1, -1, -1):
      for list[j] > current_number:
        list[j], list[j+1] = list[j+1], list[j]
        else:
          list[j+1] = current_number
          break
          
   return list


if __name__=="__main__":
  list = [3, 4, 2, 6, 5, 7, 1, 9]
  print("Sorted List: ", insertion_sort(list))
  