def search(dir):
    n=input("search the id")
    c=0
    for key,value in dir.items():
        if key==n:
            c=1
    if c==0:
        print("id is present")
    else:
        print("id is not present")

           
        
def update(dir,index):
   for i in dir:
       if i==index:
           a=dir[i]
           name=input("enter the updated name")
           id=input("enter the updated id")
           dept=input("enter the updated dept")
           salary=input("enter the updated salary")
           a[name2]=name
           a[id2]=id
           a[dept2]=dept
           a[salary2]=salary
def add(dir,index):
    for i in range(0,2):
        name=input("enter the name")
        id=input("enter the id")
        dept=input("enter the dept")
        salary=input("enter the salary")
        dir2={"name2":name,"id2":id,"dept2":dept,"salary2":salary}
        dir[index]=dir2
        index=index+1

dir={}
index=1
add(dir,index)
print(dir)
search(dir)
j=input("enter the index which you want to update")
update(dir,j)
print(dir)

