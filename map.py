## Map function 

def get_sq(no):
    return no**2


data = map(get_sq,range(10))
print(list(data))


def get_info(no):
    return no*3


info = map(get_info,range(20))
print(list(info))
