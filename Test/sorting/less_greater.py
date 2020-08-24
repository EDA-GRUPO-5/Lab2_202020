def less(element1, element2):
    if int(element1['book_id']) < int(element2['book_id']):
        return True
    return False


def greater(element1, element2):
    return not(less(element1, element2))