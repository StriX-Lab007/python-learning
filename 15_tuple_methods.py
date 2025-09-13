#Topic: Converting list to tuple and using methods


n = int(input("Enter no of elements in a list:"))
l = list()
for i in range(n):
    e = input("Enter element:")
    l.append(e)
print("List elements are:", l)

t = tuple(l)
print("Tuple elements are:", t)
print("Type of t", type(t))

e = input("Enter existing element to find index:")
print("Element ", e, " is at index", t.index(e))

e = input("Enter existing element to find no of occurences:")
print("Element ", e, ",", t.count(e), " times occured")
