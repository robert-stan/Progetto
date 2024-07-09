
# AETA

# Si richiede di implementare un programma per la misurazione dei tempi medi di esecuzione degli algoritmi, al variare della lunghezza n dell'array e del parametro k forniti in input.
#  - La lunghezza n dell'array deve essere compresa in un range di valori fra 100 e 100000. È necessario generare almeno 100 campioni per le possibili lunghezze n
#    su cui fare i test, e queste ultime devono seguire una serie geometrica. A tale scopo, è possibile utilizzare un ciclo for con un indice i
#    che varia da 0 a 99, e definire la lunghezza dell'array come funzione esponenziale di i, ad esempio n_i=⌊A⋅Bi⌋, dove A e B
#    sono costanti in virgola mobile calcolate opportunamente in modo da ottenere n_i=100 quando i=0 e  n_i=100000 quando i=99.

#  - Ogni test su una lunghezza n data deve generare in modo pseudo-casuale un array di n interi, in un intervallo a scelta (es. interi compresi fra 0 e 1000000) e un parametro k ∈ {1,...,n}. 
#    Si noti che la complessità di alcuni algoritmi può dipendere in modo significativo dalla scelta del range di interi e dal parametro k, 
#    ed è quindi possibile immaginare test diversificati in funzione di queste variabili allo scopo di evidenziare tali dipendenze.

#  - La stima dei tempi di esecuzione di un algoritmo su un array di interi deve garantire un errore relativo massimo pari a 0.001. A tal fine si procede nel modo seguente:
#     - Il primo passo consiste nello stimare la risoluzione del clock di sistema, utilizzando un ciclo while per calcolare l'intervallo minimo di tempo misurabile. 
#       A tale scopo è possibile utilizzare uno dei seguenti frammenti di codice in linguaggio Python:

#       # linguaggio Python
#       import time
#      ...
#       def resolution():
#         start = time.monotonic()
#         while time.monotonic() == start:
#             pass
#         stop = time.monotonic()
#         return stop - start

import sys
sys.setrecursionlimit(10**5)
import time
import math
from QuickSelect import QuickSelect
from HeapSelect import HeapSelect
from MedianOfMediansSelect import MedianOfMediansSelect
from Support import ArrayGenerator, TimeManager
import random
import matplotlib.pyplot as plt

A = 100  # Valore fisso di A
B = 1.07226722202 # Valore fisso di B per garantire la serie geometrica una volta che viene elevato alla i, con i che va da 0 a 99

def main():
    try:
        # Imposto il tempo minimo
        MinTime = TimeManager.MinTime()
        # Creo un dizionario per mappare i nomi degli algoritmi alle funzioni
        algoritmi = {
            'QuickSelect': QuickSelect,
            'HeapSelect': HeapSelect,
            'Median of Medians': MedianOfMediansSelect
        }
        # Creo un dizionario per salvare i tempi medi d'esecuzione nei casi medi o peggiori
        tempi_medi = {nome: {'medio': [], 'peggiore': [], 'dimensioni': []} for nome in algoritmi.keys()}
        for i in range(100): # Numero di run
            print("TEST NUMERO:" + str(i))
            n = ArrayGenerator.SizeGen(A, B, i) # Genero la grandezza dell'input
            arr = ArrayGenerator.ArrGen(n) # Genero l'array per il caso medio
            k = random.randrange(1, n) # Genero k per il caso medio
            # k = n // 2

            for nome, algorithm in algoritmi.items(): # Mando in esecuzione ciascun algoritmo, con parametri d'input per il caso medio e peggiore, memorizzando i tempi
                '''

                CASO MEDIO:

                '''
                print("K caso Medio " + str(k))

                print("Inizio misurazione caso medio di " + nome)
                tempo_medio = measure(arr, k, MinTime, algorithm) # Misuro il tempo medio d'esecuzione del caso medio
                print("Fine misurazione caso medio di " + nome)

                tempi_medi[nome]['medio'].append(tempo_medio) # Salvo il tempo medio nel dizionario
                tempi_medi[nome]['dimensioni'].append(n) # Salvo la dimensione dell'array durante questa run.

                print(f"CASO MEDIO con: {nome}, Dimensione dell'input: {n}, Tempo medio di exec: {tempo_medio:.6f} secondi") # Printo in console i dati
                '''

                CASO PEGGIORE:

                '''
                k_caso_peggiore, array_caso_peggiore = ArrayGenerator.GeneraCasiPeggiori(arr, k, n, nome) # Genero array e k per il caso peggiore
                print("K caso Peggiore " + str(k_caso_peggiore))

                print("Inizio misurazione caso peggiore di " + nome)
                tempo_medio_caso_peggiore = measure(array_caso_peggiore, k_caso_peggiore, MinTime, algorithm) # Misuro il temo medio d'esecuzione del caso peggiore
                print("Fine misurazione caso peggiore di " + nome)

                tempi_medi[nome]['peggiore'].append(tempo_medio_caso_peggiore) # Salvo il tempo medio nel dizionario

                print(f"CASO PEGGIORE: {nome}, Dimensione dell'input: {n}, Tempo medio di exec: {tempo_medio_caso_peggiore:.6f} secondi") # Printo in console i dati

                print("\n")

        genGrafico(algoritmi, tempi_medi) # Alla fine di tutte le Run, genero i grafici comparativi per ogni algoritmo

    except KeyboardInterrupt: # Se l'utente stoppa l'esecuzione con Ctrl + C, genero i grafici ed esco dal programma.
        print("Exit")
        genGrafico(algoritmi, tempi_medi)


def genGrafico(algoritmi, tempi_medi): # Funzione per generare i grafici comparativi
    for nome in algoritmi.keys(): # Per ogni algoritmo nel dizionario, creo il plot con tutti i dati memorizzati nel dizionario dei tempi medi d'esecuzione e delle dimensioni
            plt.figure(figsize=(20, 10))
            plt.plot(tempi_medi[nome]['medio'], label='Caso Medio')
            plt.plot(tempi_medi[nome]['peggiore'], label='Caso Peggiore')
            x_labels = [f"Dim. {d}" for d in tempi_medi[nome]['dimensioni']] # Creo le etichette sull'asse delle x con le dimensioni degli array
            plt.xticks(ticks=range(len(x_labels)), labels=x_labels, rotation=45)  # Setto le etichette dell'asse delle x
            plt.title(nome)
            plt.ylabel("Tempo d'esecuzione medio")
            plt.xlabel('Numero della run e Dimensione dell\'array')
            plt.legend()
            plt.savefig(f'{nome}_grafico.png')


def measure(arr, k, min_time, algorithm):
    iterazioni = 0
    start_time = TimeManager.Now()
    while True:
        algorithm(arr, k)
        iterazioni = iterazioni  + 1
        end_time = TimeManager.Now()
        if (end_time - start_time >= min_time):
            break
    return (end_time - start_time) / iterazioni



if __name__ == "__main__":
    main()



            

