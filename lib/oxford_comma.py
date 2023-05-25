
def oxford_comma(items):
    if len(items) == 1:
        items2 = ''.join(items)
        return items2
    if len(items) == 2:
        items2 = ' and '.join(items)
        return items2
    else:
        a = ', '.join(items[:-1])
        b = ', and ' + items[-1]
        items2 = a + b
        return items2
