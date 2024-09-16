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