def binary_search(array, item):
    st = 0
    end = len(array) - 1
    
    while st <= end:
        midpoint = st + (end - st) // 2
        midpoint_value = array[midpoint]
        if midpoint_value == item:
            return midpoint
        
        elif item < midpoint_value:
            end = midpoint - 1
        
        else:
            st = midpoint + 1
    return None

array_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
item_1 = 13

print(binary_search(array_1, item_1))