print("hello!")
for i in [0,1,2,3,4]:
    print(i)
    
data = ['환자1','환자2','환자3','환자4']
for subj in data:
    print(subj)

for i in [0,1,2,3]:
    print(i,data[i])

for i in [0,1,2,3]:
    if i<2:
        print (data[i],'is A 유형.')
    else:
        print (data[i],"is B 유형.")
    


for i in range(0,4):
    print(i,data[i])

for i in range(0,4):
    print('환자',i+1)    
    
for i in range(5):
    if i%2 == 0:
        print (i,'is even.')
    else:
        print (i,"is odd.")
print ("Great!")


""" 
This will not be executed...
print("This is an example 1”)
"""
