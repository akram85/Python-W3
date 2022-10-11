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
num = int(input('enter a number '))
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
  print (rev - 2 * rev)
