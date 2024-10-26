import random

'''
1 is for snake
-1 is for water
0 for gun
'''

computer=random.choice([-1,0,1])
youstr=input("enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:'Snake',-1:'Water',0:'Gun'}

you=youDict[youstr]

#by now we have 2 numbers (variables), you and computer


print(f'You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}')


if(computer==you):
    print("ITS A DRAW!!!")    

elif(computer==-1 and you==1):
    print("YOU WIN!!!")               #snake wins over water

elif(computer==-1 and you==0):
    print("YOU LOSE!!!")              #water wins over gun

elif(computer==1 and you==-1):
    print("YOU LOSE!!!")              #snake wins over water

elif(computer==1 and you==0):
    print("YOU WIN!!!")               #gun wins over snake

elif(computer==0 and you==-1):
    print("YOU WIN!!!")               #water wins over gun

elif(computer==0 and you==1):
    print("YOU LOSE!!!")              #gun wins over water

else:
    print('something went wrong!!')