def replace_space(string):
    char_array=[None]*len(string)
    for index in range(0,len(string)):
        if string[index] == ' ':
            char_array[index]='%20'
        else:

            char_array[index]=(string[index])
    return char_array


print(replace_space('abc tc'))