import os

print("Iniciando...")

for i in range (5): #Devices:  50,100,500,1000,5000
	print("Ciclo: ", i)
	for j in range (300): #300 para cada uno
		if(i==0):
			devices = "50"
		elif(i==1):
			devices = "100"
                elif(i==2):
			devices = "500"
                elif(i==3):
			devices = "1000"
                elif(i==4):
			devices = "5000"
		cmd = './waf --run=lorawan-example-tracing --command-template="%s'
		cmd += ' --randomSeed=12354 --nEndDevices=%s --nGateways=1 --discRadius=6100.0 --totalTime=600 --nRuns=1 --usPacketSize=21 --usDataPeriod=600 --usConfirmedData=0 --dsDataGenerate=0 --verbose=0 --stdcout=0 --tracePhyTransmissions=0 --tracePhyStates=0 --traceMacPackets=0 --traceMacStates=0 --outputFileNamePrefix=simulations/"' % (devices)
		print('Executing: ',cmd)
		os.system(cmd)
print("Terminado")
