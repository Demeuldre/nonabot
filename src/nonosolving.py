import time
from numpy import array

def printBoard(n_rows, n_cols, nano_given):
    counter = 0
    for i in range(n_rows):
        for x in range(n_cols):
            if nano_given[counter] == 1:
                print("Position [", i, "][", x, "] will be paint")
                # Enviar coordenades a Inverse Kinematics Module
                giveCoordinates()
                #Esperamos a que pinte
                time.sleep(2)
            else:
                print("Position [", i, "][", x, "] will NOT be paint")
            counter += 1

def giveCoordinates():
    # Give info to Inverse Kinematics
    print("Info for Kinematics")


def checkParameters(rows, columns, array_nono):
    print("-----------")
    print(f'Filas: {rows}')
    print(f'Columnas: {columns}')
    print(f'Array: {array_nono}')
    print("-----------")



