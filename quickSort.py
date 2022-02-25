def swap(array,x,y):
    array[x], array[y] = array[y], array[x]
    return array
  
def partition(array,upperBound,lowerBound):
    pivotIndex = (len(array[lowerBound:upperBound]))//2
    swap(array, pivotIndex ,len(array)-1)
    pivot = array[-1]
    c1 = 0
    for c2,i in enumerate(array[:-1]):
        if i<pivot:
            swap(array,c1,c2)
            c1+=1
    swap(array,c1,-1)
    pivot = c1
    return pivot
  
def quickSort(array,upperBound,lowerBound):
    print("array in quick sort is :",array)
    if upperBound > lowerBound:
        pivot = partition(array,upperBound,lowerBound)
        quickSort(array,upperBound,pivot+1)
        quickSort(array,pivot-1,lowerBound)
 
if __name__ = "__main__":
  a = [4,12,7,5,3,6]
  quickSort(a,len(a)-1,0)
  print("This is sorted array",a)
  
  
