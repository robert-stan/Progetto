import csv
import math

def OpenCSV():
    filename = 'Progetto-ASD/src/Log/Output.csv'
    header = ['#RUN,', ' #TEST,', ' TOTAL_TIME,', ' ITERATIONS,', ' SINGLE_COMPUTE_TIME']
    csv_file = open(filename, 'w')
    csv_file.writelines(header)
    csv_file.write('\n')
    csv_file.flush()
    return csv_file
        

def WriteData(run, test, total_time, iterations, single_compute_time, csv_file):
    filename = 'Progetto-ASD/src/Log/Output.csv'
    data = [str(run) + ', ', str(test) + ', ', str(total_time) + ', ', str(iterations) + ', ', str(single_compute_time)]
    csv_file.writelines(data)
    csv_file.write('\n')
    csv_file.flush()
    
def CloseCSV(csv_file):
    csv_file.close()
