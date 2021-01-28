
s = input()
cnt = 0
stop = False
for i in range(len(s)-1):
  if(s[-1] == 's' and s[-2] == 's'):
    print('hiss')
    stop = True
    break
  elif(s[cnt] == 's' and s[cnt+1] == 's'):
    print('hiss')
    stop = True
    break
  cnt+=1
if(stop == False):
  print('no hiss')