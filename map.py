## Map function 

def get_sq(no):
    return no**2


data = map(get_sq,range(10))
print(list(data))
