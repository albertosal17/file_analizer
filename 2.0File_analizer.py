
import json
import numpy as np
import matplotlib.pyplot as plt

filename = "C:\\Users\\ASUS\\Desktop\\TESI\\data\\lima2112.json"
num_qubits = 3

#importo i dati contenuti dentro al file
with open(filename) as fh: #with ti consente di non dovere chiudere manualmente il file alla fine 
    data = json.load(fh) #data sarà un dictonary (lista di coppie label-elemento)

#mi salvo a parte i conteggi delle misure 
counts = data["results"][0]["data"]["counts"] #counts = {"0x0": 1441, "0x1": 606, "0x2": 559, "0x3": 616, "0x4": 3543, "0x5": 575, "0x6": 603, "0x7": 249}

shots = data["results"][0]["shots"] #shots = 8192

#ridefinisco opportunamente il dictionary che contiene le misure al fine di plottare
new_counts = {}
moment = []
for idx, cnt in counts.items(): # idx, cnt mi permette di accedere ad ogni iterazione ad una certa coppia label+elemento del dictionary
    #The items() method returns a view object. 
    #The view object contains the key-value pairs 
    #of the dictionary, as tuples in a list.

    new_counts[ np.binary_repr( int(idx, base=0), num_qubits) ] = cnt 
   # moment.append( num_qubits*( 2**(-int(idx, base=0) )-1/2) )

values = np.array( list(new_counts.values() ) ) #values() returns a view object that contains the values of the dictionary, as a list #new_counts.values = [1441, 606, 559,....]

values_normalized = []
for i in values:
    values_normalized.append(i/shots)

print(values)
print(values_normalized)
plt.plot(np.arange(2**num_qubits)-int("1"+"0"*(num_qubits-1), 2), values_normalized, 'o--') #matplotlib.pyplot.plot(x, y, ?)
plt.grid()
plt.show()
