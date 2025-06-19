import time

b= time.strftime("%H", time.localtime())
a=int(b)
print("The time is",time.strftime("%I:%M:%S:%P",time.localtime()))
if(a>5 and a<12):
  print("Good morning")
elif(a>=12 and a<17):
  print("Good afternoon ")
elif(a>=17 and a<21):
  print("Good evening")
else:
  print("Good night")

