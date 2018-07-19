#program in python for tic tac toe game

again='y'
while again == 'y':
 a=['0','1','2','3','4','5','6','7','8']
 print('',a[0],"|",a[1],"|",a[2])
 print("- -|- -|- -")
 print('',a[3],"|",a[4],"|",a[5])
 print("- -|- -|- -")
 print('',a[6],"|",a[7],"|",a[8])
 m=2
 l=[]
 n=[0,1,2,3,4,5,6,7,8]
 for x in range(9):
  if m!=1:
   m=1
   b='x'
  else:
   m=2
   b='o'
  r=1 
  while r: 
   r=0
   print("index player",m,':') 
   try:
    c=int(input()) 
   except ValueError:
    r=1
    print("enter correct value b/w 0 to 9")   
  while c not in n or c in l:
   print("you have entered wrong index or already used")
   s=1
   while s:
    s=0
    print("index player",m,':')
    try:    
     c=int(input())
    except ValueError:
     s=1
     print("enter correct value b/w 0 to 9")
  l.append(c)  
  a[c]=b
  print('',a[0],"|",a[1],"|",a[2])
  print("- -|- -|- -")
  print('',a[3],"|",a[4],"|",a[5])
  print("- -|- -|- -")
  print('',a[6],"|",a[7],"|",a[8])
  if a[0]==a[3]==a[6] or a[1]==a[4]==a[7] or a[2]==a[5]==a[8] or a[0]==a[1]==a[2] or a[3]==a[4]==a[5] or a[6]==a[7]==a[8] or a[0]==a[4]==a[8] or a[2]==a[4]==a[6]:
   print('player ',m,' have won')
   print("do you want to play again press y or n")
   again=input()
   break
  else: 
   if x==8:
    print('game draw')
    print("do you want to play again press y or n")
    again=input()
  
   

# o | x | x
#- -|- -|- -
# o | x | o
#- -|- -|- -
# 6 | x | 8
#player  1  have won
#do you want to play again press y or n
