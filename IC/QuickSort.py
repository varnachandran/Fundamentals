def quick_sort(numbers, start, stop):
    if not numbers:
        return None

    pivot = numbers[start]

    i =start +1
    j= stop

    while i <= j and i <= stop and j >= start:
        if numbers[i] > pivot:
            if numbers[j] < pivot:
                numbers[i], numbers[j] = numbers[j], numbers[i]
            j = j-1
        i= i +1

    if j > start and j<stop:
        numbers[j], numbers[start] = numbers[start], numbers[j]

        quick_sort(numbers, start, j-1)
        quick_sort(numbers, j+1, stop)

    return numbers

numbers = [10, 16, 8, 12, 15, 6, 3, 9, 5]
print (quick_sort(numbers, 0, 8))
print (quick_sort([1,2,3, 4], 0, 0))