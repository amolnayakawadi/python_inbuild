### Zip inbuild function

name = ['Amol','Abhi','Akash','Viv','Hanu'] 
marks = [44,55,66,77,88]
roll_no = [1,2,3,4,5]

info = zip(name,marks,roll_no)
print(list(info))

for i,j,k in info:
    print(f'{i} {j} {k}')

data = zip(name,roll_no)
print(dict(data))


student = ['Amol','Abhi','Akash','Viv','Hanu'] 
marks = [44,55,66,77,88]
roll_no = [1,2,3,4,5]

shit = zip(student,marks,roll_no)
for i,j,k in shit:
    print(f'{i} {j} {k}')
