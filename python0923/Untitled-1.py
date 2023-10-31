'''
def perform_add(x,y,z=80):
    res1 = x+y
    res2 = y-z
    return res1,res2

et1,et2 =perform_add(y=8,x=7)
print(et1,et2)

et1,et2 = et2,et1
print(et1,et2)

for _ in range(3):
    print("*",end='')
''' 

# c++ struct
#typedef struct stu
#{
#    int id;
#    char name;
#}tStudentIbfo;

#key : value
#(8,9):['a']

'''
def print_info(stu_list):
    for per_stu in stu_list: #daa type:dictionary
        id = per_stu["id"]
        name = per_stu["name"]
        print("id : {},name : {}".format(id,name))

def main():
    stu_list = list()
    keep_going = "y"
    while keep_going == "y" :
        id = int (input("input id :"))
        name = input("input name :")

        stu_info = {
            "id" : id,
            "name" : name
            #"secore" : {
            #"math" : 90,
            #"eng" : 70
            #}
        }
        stu_list.append(stu_info) 
        keep_going = input("keep go ?")
    print(stu_list) 
'''

#計算機
def perform_add(x,y):
    return(x+y)

def perform_sub(x,y):
    return(x-y)

def perform_mul(x,y):
    return(x*y)
def main():
    keep_going = "y"
    while keep_going == "y":
        choice = int(input("choice function :"))
        x = int(input("input x :"))
        y = int(input("input y :"))
        if choice == 0:
            print("reslut :{}".format(perform_add(x,y)))
        elif choice == 1:
            print("reslut :{}".format(perform_add(x,y)))
        elif choice == 2:
            print("reslut :{}".format(perform_add(x,y)))
        keep_going = input("keep go ?")
main()

