
'''
Si richiede di implementare un programma per la misurazione dei tempi medi di esecuzione degli algoritmi, al variare della lunghezza n dell'array e del parametro k forniti in input.
 - La lunghezza n dell'array deve essere compresa in un range di valori fra 100 e 100000. È necessario generare almeno 100 campioni per le possibili lunghezze n
   su cui fare i test, e queste ultime devono seguire una serie geometrica. A tale scopo, è possibile utilizzare un ciclo for con un indice i
   che varia da 0 a 99, e definire la lunghezza dell'array come funzione esponenziale di i, ad esempio n_i=⌊A⋅Bi⌋, dove A e B
   sono costanti in virgola mobile calcolate opportunamente in modo da ottenere n_i=100 quando i=0 e  n_i=100000 quando i=99.

 - Ogni test su una lunghezza n data deve generare in modo pseudo-casuale un array di n interi, in un intervallo a scelta (es. interi compresi fra 0 e 1000000) e un parametro k ∈ {1,...,n}. 
   Si noti che la complessità di alcuni algoritmi può dipendere in modo significativo dalla scelta del range di interi e dal parametro k, 
   ed è quindi possibile immaginare test diversificati in funzione di queste variabili allo scopo di evidenziare tali dipendenze.

 - La stima dei tempi di esecuzione di un algoritmo su un array di interi deve garantire un errore relativo massimo pari a 0.001. A tal fine si procede nel modo seguente:
    - Il primo passo consiste nello stimare la risoluzione del clock di sistema, utilizzando un ciclo while per calcolare l'intervallo minimo di tempo misurabile. 
      A tale scopo è possibile utilizzare uno dei seguenti frammenti di codice in linguaggio Python:

      # linguaggio Python
      import time
      ...
      def resolution():
        start = time.monotonic()
        while time.monotonic() == start:
            pass
        stop = time.monotonic()
        return stop - start

'''
import sys
sys.setrecursionlimit(10**5)
import time
import math
import QuickSelect
from Log import Logger
from Support import ArrayGenerator, TimeManager
import random

RUNS = 6 # Numero di run
A = 100  # Valore fisso di A
B = 1.07226722202 # Valore fisso di B per garantire la serie geometrica una volta che viene elevato alla i, con i che va da 0 a 99

# Funzione per troncare le cifre dopo la virgola in base ai parametri passati come argomenti di funzione
def truncate(number, digits) -> float:
    # Migliora la precisione con operazioni in floating point, per evitare: truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
    nbDecimals = len(str(number).split('.')[1]) 
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def main():
    # Imposto il tempo minimo
    MinTime = TimeManager.MinTime()
    csv = Logger.OpenCSV()
    # this_run indica la run attuale
    for this_run in range(RUNS):
        # i e' l'esponente con cui eleviamo B per aumentare la dimensione dell vettore (secondo A*B^i)
        for i in range(0, 100):

            print("#Run: " + str(this_run + 1) + " #Test: " + str(i + 1))
            
            iteration = 0
            # Genero la dimensione del vettore
            n = ArrayGenerator.SizeGen(A, B, i)
            # Genero il vettore
            arr = ArrayGenerator.ArrGen(n)
            print("Array size is " + str(len(arr)))
            # Genero k in modo randomico
            k = random.randrange(1, n)
            print("K is: " + str(int(k)))

            # Salvo l'istante di tempo all'avvio
            start_time = TimeManager.Now()

            while True: # Simulo un ciclo do while
                # Eseguo QuickSelect sul vettore
                element = QuickSelect.QuickSelect(arr, 0, len(arr) - 1, k-1)
                # Salvo l'istante di tempo una volta terminata l'esecuzione di QuickSelect
                end_time = TimeManager.Now()
                # Conto l'iterazione
                iteration = iteration + 1
                # Se ho computato più tempo rispetto MinTime esco dal while
                if(end_time - start_time >= MinTime):
                    #Esco dal ciclo while
                    break
            
            print("Element in k-th position is " + str(element))
            # Ottengo il tempo impiegato nel while all'i-esima iterazione del for
            elapsed_time = end_time - start_time
            # Salvo le informazioni nel log file
            Logger.WriteData(this_run, i, truncate(elapsed_time, 5), iteration, truncate((elapsed_time/iteration) * 1000, 5), csv)
    Logger.CloseCSV(csv)

if __name__ == "__main__":
    main()



            

