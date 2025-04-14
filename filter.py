def filter_function(a):
    return a>2

newli=list(filter(filter_function(),1))
print(newli)