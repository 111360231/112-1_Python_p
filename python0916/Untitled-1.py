#python ep1
'''print("hello word")
print(5*8)

money=34
print('money :',money)

input_string = input("please enter a name :")
print(input_string)
print("the name yot entered is :{}".format(input_string))

first_num1 = int(input("please enter first number :"))
second_num1 = int(input("please enter second number :"))
print("the result is {}".format(first_num1*second_num1))
print(end='\n')
'''

#ptrhon ep2
'''first_num2 = int(input("please enter first number :"))
second_num2 = int(input("please enter second number :"))
if first_num2 > second_num2 :
    print("first > second")
elif first_num2 == second_num2:
    print("first = second")
else:
    print("first < second")

test=(first_num2 > second_num2)
print(test)
print(end='\n')
'''
#python ep3
'''
keep_going = "y"
while keep_going == "y":
    working_hour = int(input("please enter your hour or 0 to stop :"))
    if working_hour == 0:
        keep_going = "n"
        continue
    if working_hour < 30:
        print("salary is {}".format(working_hour * 100))
    elif working_hour >= 30 and working_hour < 50:
        print("salary is {}".format(working_hour * 120))
    else:
        print("salary is {}".format(working_hour * 130))

for i in [1,2,3,4,5]:
    print(i)

for i in [1,2,3,4,5,6,7,8,9]:
    for j in range(1,10):
        print("{}*{}={}".format(i,j,i*j))

for i in range(10):
    print(i," ",end='')
print(end='\n')
for j in range(1,10,2):
    print(j," ",end='')
print(end='\n')
for k in range(10,0,-1):
    print(k," ",end='')
print(end='\n')

for i in range(1,5):
    for j in range(i):
        print("*",end='')
    print(end='\n')
print("#"*2)
for i in range(1,5):
    print("*"*i)
print("#"*2)
for i in range(4):
    print(" "*i+"*"*(4-i))
'''

#python ep4
'''
list_a = [1,5,8,6,9,4]
list_b = ["a","test",1,4.4]

for content in list_a:
    print(content," ",end='')
print(end='\n')

list_a.sort()
for content in list_a:
    print(content," ",end='')
print(end='\n')
list_a.sort(reverse=False)
for content in list_a:
    print(content," ",end='')
print(end='\n')
list_a.sort(reverse=True)
for content in list_a:
    print(content," ",end='')
print(end='\n')

print("maximum in list_a :",max(list_a))
print("list_a's length :",len(list_a))
print("fourth element in list_a :",list_a[3])

for content in list_b:
    print(content," ",end='')
print(end='\n')

list_b.append("QQ")
for content in list_b:
    print(content," ",end='')
print(end='\n')

list_b.pop()
for content in list_b:
    print(content," ",end='')
print(end='\n')

list_b.pop(0)
for content in list_b:
    print(content," ",end='')
print(end='\n')

list_c = list_a[2:4]
print("second element and third element in list_a : ",end='')
for content in list_c:
    print(content," ",end='')
print(end='\n')
'''