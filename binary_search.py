def binary_search(elements, element):
    rp = len(elements) - 1
    lp = 0
    mp = 0
    while lp <= rp:
        mp = (rp + lp + 1) // 2
        num = elements[mp]

        if num == element:
            return mp

        if element < num:
            rp = mp - 1
        if element > num:
            lp = mp + 1
        
    return -1



def binary_search_recursive(elements, element, rp=None, lp=0):
    if rp is None:
        rp = len(elements) - 1

    if rp < lp:
        return -1

    mp = (rp + lp) // 2
    mn = elements[mp]
    
    if mn == element:
        return mp

    if element < mn:
            rp = mp - 1
    if element > mn:
        lp = mp + 1
    
    return binary_search_recursive(elements, element, rp, lp)


def binary_search_duplicates(elements, element):
    index = binary_search(elements, element)
    duplicates = []
    i = index - 1
    while i >= 0:
        if elements[i] == element:
            duplicates.append(i)
            i -= 1
        else:
            break

    duplicates.append(index)
    i = index + 1
    while i < len(elements):
        if elements[i] == element:
            duplicates.append(i)
            i += 1
        else:
            break

    duplicates.sort()
    return duplicates
        