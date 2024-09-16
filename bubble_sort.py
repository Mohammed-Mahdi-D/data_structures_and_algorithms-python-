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


# ******** example **********
# friends = [{"name": "person1","age": 17,"score": 100},
#            {"name": "person2","age": 18,"score": 99},
#            {"name": "person0","age": 20,"score": 95},
#            {"name": "person3","age": 18,"score": 85}]


# bubble_sort_by(friends, "name")
# print(friends)    
