def bubble_sort(elements):
    size = len(elements) - 1

    for i in range(size):
        swapped = False

        for j in range(size):
            
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        

        if not swapped:
            break
    return elements


def bubble_sort_by(elements, key):
    size = len(elements) - 1

    for i in range(size):
        swapped = False

        for j in range(size):
            
            if elements[j][key] > elements[j+1][key]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True

        if not swapped:
            break
    return elements

