def find_duplicates(arr):
    duplicates = []
    for element in arr:
        count = 0
        
        for sub_element in arr:
            if element == sub_element:
                count += 1
                # print(count)
        
        if count > 1:
            # print(element)
            if element not in duplicates:
                duplicates.append(element)
    return duplicates


print(find_duplicates([1, 2,  3, 4, 4, 5, 2, 3, 1]))
