def divide(num, den):
    if den == 0:
        return "undifined"
    i = 0
    while num >= den:
        num = num - den
        i += 1
    return i

print divide(8,2)
print divide(8,3)
print divide(8,0)
print divide(9,5)
print divide(15,3)
print divide(15,2)
