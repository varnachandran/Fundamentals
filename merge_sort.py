def merge_sort(arr,first,last):
    if first<last:
        mid=(first+last)//2
        merge_sort(arr,first,mid)
        merge_sort(arr,mid+1,last)

        arr=joinarrays(arr,first,mid,last)
    return arr

def joinarrays(arr,first,mid,last):
    l=arr[first:mid+1]
    r=arr[mid+1:last+1]
    counter=first
    i=0
    j=0
    newarr=arr[:]
    while i<mid+1-first and j < last-mid:
        if l[i]<r[j]:
            newarr[counter]=l[i]
            i=i+1
        else:
            newarr[counter]=r[j]
            j=j+1
        counter=counter+1
    return newarr







arr=[10,1,20,3,5,7]
print(merge_sort(arr,0,5))