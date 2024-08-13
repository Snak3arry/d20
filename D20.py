import random

print("Quer jogar um D20? Y/N")
x = input()
if x == ("Y"):
 print(random.randrange(1,20))
elif x == ("N"):
 print("Blz então")
else:
  print("Só sei ler Y/N, pare de me falar essas letras estranhas!")