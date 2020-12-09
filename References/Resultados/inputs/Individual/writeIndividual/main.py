input=open("config.um",'r')
inputs=input.readlines()
inputnumber=open("iteracao.txt",'r')
inputnumbers=inputnumber.readlines()
n=inputnumbers[len(inputnumbers)-1]
inputnumber.close()
output=open("iteracao.txt",'a')
output.write("\n{}".format(int(n)+10))
inputs[6]="variable2=t;20;{}\n".format(n)
input.close()
outputnumber=open("config.um",'w')
for i in range (0,len(inputs)):
    outputnumber.write("{}".format(inputs[i]))


