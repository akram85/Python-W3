#while
# factorial
'''num = int(input('enter a number '))
fact = 1
if (num < 0):
  print('not defined')
else:
  while (num > 0):
    fact = fact * num
    num = num - 1

  print(fact)'''

#find no of digits in a number
'''num =abs(int(input('enter a number ')))
count =1
while(num>9):
  num=num//10
  count = count +1

print(count)'''
#reverse the digits in the given number
# 1234 to 4321
'''num = int(input('enter a number '))
absNum =abs(num)
rev = absNum % 10  #4
absNum = absNum // 10  #123
while (absNum > 0):
  r = absNum % 10  #3
  absNum = absNum // 10  #12
  rev = rev * 10 + r  #43
  
if(num>=0):
  print(rev)
else:
  print (rev - 2 * rev)'''
# For loop , format printing

'''for i in range(10):
  print(i,'hello world'''

'''for i in range(1,11):
  print(2*i)'''

'''for i in range(1,11,2):
  print(i, end =' ')
country ='india'
for l in country:
  print(l,end =' ')'''

#formatted printing
'''d= 10
m=5
y=2022

print("Today's date is" ,end =' ')
print(d,m,y, sep ='/')'''

#num = int(input())
#for i in range(1,11):
  #print(num ,'X', i,'=',num*i)
  #print(f'{num} X {i} = {num*i}')
  #print('{0} X {1} = {2}'.format(num,i,num*i))
  #print('%d X %d = %d' % (num,i,num*i))
#pi=22/7
#print(f'Value of PI = {pi:.2f}')
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))

# Nested loops
  

