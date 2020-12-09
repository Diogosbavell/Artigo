from decimal import *

input=open("config.um",'r')
inputs=input.readlines()
inputnumber=open("fault.txt",'r')
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
inputs[4]="variable0=PR1;7;{};{}\n".format(mod[1],float(mod[2])/float(mod[3]))
inputs[5]="variable1=PR2;7;{};{}\n".format(mod[1],float(mod[2])/float(mod[3]))
inputs[6]="variable2=PR3;7;{};{}\n".format(mod[1],float(mod[2])/float(mod[3]))
inputs[11]="variable3=PR4;7;{};{}\n".format(mod[1],float(mod[2])/float(mod[3]))
inputs[12]="variable4=PR5;7;{};{}\n".format(mod[1],float(mod[2])/float(mod[3]))
inputs[13]="variable5=PR6;7;{};{}\n".format(mod[1],float(mod[2])/float(mod[3]))
inputs[16]="variable6=PR7;7;{};{}\n".format(mod[1],float(mod[2])/float(mod[3]))
inputs[17]="variable7=PR8;7;{};{}\n".format(mod[1],float(mod[2])/float(mod[3]))
inputs[18]="variable8=PR9;7;{};{}\n".format(mod[1],float(mod[2])/float(mod[3]))
#Amp Op
inputs[8]="variable9=PU1;7;{};{}\n".format(mod[7],float(mod[8])/float(mod[9]))
inputs[9]="variable10=PU2;7;{};{}\n".format(mod[7],float(mod[8])/float(mod[9]))
inputs[14]="variable11=PU3;7;{};{}\n".format(mod[7],float(mod[8])/float(mod[9]))
#ResistorVariavel
inputs[7]="variable12=PRV1;7;{};{}\n".format(mod[4],float(mod[5])/float(mod[6]))
inputs[10]="variable13=PRV2;7;{};{}\n".format(mod[4],float(mod[5])/float(mod[6]))
inputs[15]="variable14=PRV3;7;{};{}\n".format(mod[4],float(mod[5])/float(mod[6]))

input.close()
outputnumber=open("config.um",'w')
for i in range (0,len(inputs)):
    outputnumber.write("{}".format(inputs[i]))

