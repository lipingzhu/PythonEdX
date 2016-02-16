def my_fun(m):
    x = m[:]
    for k in x:
        if type(k) == int:
            m.remove(k)

values = [3, [3,4], 2.9, 3, 6, 'dog', 5]
my_fun(values)
print(values)

