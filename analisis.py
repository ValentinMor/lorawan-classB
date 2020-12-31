import os

print("Procesando")
output = open("resultados.csv", "w+")
output.write("Gateways | EndDevices | Sent | Received | Loss \r\n")

id = []
for (root,dirs,files) in os.walk('./simulations'): 
	for file in files:
		filepath = os.path.join(root,file)
		filepath = filepath.split('-')
		if (filepath[1] not in id):
			id.append(filepath[1])
			settings =  '-'.join(filepath[0:3])+'-sim-settings.txt'
			edmsgs = '-'.join(filepath[0:3])+'-trace-ed-msgs.csv'
			dsmsgs = '-'.join(filepath[0:3])+'-trace-ns-dsmsgs.csv'
			f = open(settings,'r')
			for x in f:
				line = x.split()
				if(line[0] == 'nGateways'):
					output.write(line[2]+" | ")
				elif(line[0] == 'nEndDevices'):
					output.write(line[2]+" | ")
			f.close()
			sent = -1 #mensajes enviados, -1 ya qe la primera linea corresponde a los parametros
			recieved = -1 #mensajes recibidos
			f = open(edmsgs,'r')
			for r in f:
				sent += 1.0
			output.write(str(sent)+" | ")
			f.close()
			f = open(dsmsgs,'r')
                        for l in f:
                                recieved += 1.0
			output.write(str(recieved)+" | ")
                        f.close()
			output.write(str((sent-recieved)/sent)+"\n")

output.close()
print("Terminado")
