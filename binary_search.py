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

