from decimal import *

input=open("config.um",'r')
inputs=input.readlines()
inputnumber=open("fussel.txt",'r')
n=inputnumber.readlines()
inputnumber.close()
passo=open("iteracao.txt",'r')
passos=passo.readlines()
passon=passos[len(passos)-1]
passo.close()
output=open("iteracao.txt",'a')
output.write("\n{}".format(int(passon)+1))
mod = n[int(passon)].split()
print(mod)

#ResistorFixo
inputs[4]="variable0=P0;7;{};{}\n".format(mod[1],float(mod[2]))
inputs[5]="variable1=Pbase;7;{};{}\n".format(mod[4],float(mod[5]))


input.close()
outputnumber=open("config.um",'w')
for i in range (0,len(inputs)):
    outputnumber.write("{}".format(inputs[i]))

