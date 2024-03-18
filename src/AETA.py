
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
import time
import math
import ArrayGenerator
import QuickSelect
import Logger
import TimeManager
import random

RUNS = 1 # Numero di run
A = 100
B = 1.07226722202

def truncate(number, digits) -> float:
    # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
    nbDecimals = len(str(number).split('.')[1]) 
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def main():
    MinTime = TimeManager.MinTime()

    for this_run in range(0, RUNS):
        for i in range(0, 99):

            print("#Run: " + str(this_run) + " #Test: " + str(i))
            
            iteration = 0
            
            n = ArrayGenerator.SizeGen(A, B, i)
            arr = ArrayGenerator.ArrGen(n)
            print("Array size is " + str(len(arr)))

            k = random.randrange(1, n)
            print("K is: " + str(int(k)))

            start_time = TimeManager.Now()
            while True:
                element = QuickSelect.QuickSelect(arr, 0, len(arr) - 1, k-1)
                end_time = TimeManager.Now()
                iteration = iteration + 1
                if(end_time - start_time > MinTime):
                    break
            
            elapsed_time = end_time - start_time
            Logger.WriteLog(i, this_run, elapsed_time, iteration)

if __name__ == "__main__":
    main()



            

