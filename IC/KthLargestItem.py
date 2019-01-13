def kth_largest_item(my_list, k):
    if not my_list or not my_list:
        raise Exception('List/k empty')
    if k == 1:
        return max(my_list)
    while k >= 1:
        current_max = max(my_list)
        my_list.pop(my_list.index(current_max))
        k = k-1
    return current_max


def kth_largest_item_recursion(my_list, k):
    if not my_list:
        raise Exception('List empty/ invalid k')
    if k == 1:
        return max(my_list)
    current_max = max(my_list)
    return kth_largest_item([x for x in my_list if x != current_max], k - 1)


print(kth_largest_item([8, 1, 11, 23, 7, 9], 2))
