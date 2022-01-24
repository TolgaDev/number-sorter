

def removeduplicates(duplist):
    noduplist = []
    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)
            
    return noduplist


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []
    
    for item in sequence:
        if item > pivot:
            if item in items_greater:
                break
            else:
                items_greater.append(item)
        else:
            if item in items_lower:
                break
            else:
                items_lower.append(item)


    final = removeduplicates(quick_sort(items_lower) + [pivot] + quick_sort(items_greater))
    
    return final



print(quick_sort([8,7,5,2,3,5,4,2,4,4,2,3]))


