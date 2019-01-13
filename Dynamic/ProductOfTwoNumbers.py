def product_of_numbers(a,b):
    smaller=min(a,b)
    bigger=max(a,b)
    return product_helper(smaller, bigger)

def product_helper(small,big):
    if small == 0:
        return 0
    if small == 1:
        return big

    shifted_small= small >> 1
    halfprod= product_helper(shifted_small, big)
    if small%2==0:
        return halfprod+ halfprod
    else:
        return halfprod+halfprod+ big

print(product_of_numbers(30,5))