## Filter inbuild function 

def check_even(no):
    if no%2 == 0:
        return True
    return False

list1 = [1,2,3,4,5,6,7,8,9]
list2 = filter(check_even,list1)
print(list(list2))