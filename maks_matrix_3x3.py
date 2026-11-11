import os
import time

color_1 = "🟢"
color_2 = "🔴"
num = 0.0 

list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

matrix_1 = f"{list[0]}{list[1]}{list[2]}"
matrix_2 = f"{list[3]}{list[4]}{list[5]}"
matrix_3 = f"{list[6]}{list[7]}{list[8]}"

def dell():
    print("\n" * 100)
    
def set_color(index, color):
    if color == 1:
        list[index] = color_1
    if color == 2:
        list[index] = color_2

def print_matrix():
    matrix_1 = f"{list[0]}{list[1]}{list[2]}"
    matrix_2 = f"{list[3]}{list[4]}{list[5]}"
    matrix_3 = f"{list[6]}{list[7]}{list[8]}"
    print(matrix_1)
    print(matrix_2)
    print(matrix_3)

def simple_matrix():
    list[0] = color_1
    list[1] = color_1
    list[2] = color_1
    list[3] = color_1
    list[4] = color_1
    list[5] = color_1
    list[6] = color_1
    list[7] = color_1
    list[8] = color_1
    print_matrix()
    time.sleep(1)
    dell()
    list[0] = color_2
    list[1] = color_1
    list[2] = color_1
    list[3] = color_1
    list[4] = color_1
    list[5] = color_1
    list[6] = color_1
    list[7] = color_1
    list[8] = color_1
    print_matrix()
    time.sleep(1)
    dell()
    list[0] = color_2
    list[1] = color_2
    list[2] = color_1
    list[3] = color_2
    list[4] = color_1
    list[5] = color_1
    list[6] = color_1
    list[7] = color_1
    list[8] = color_1
    print_matrix()
    time.sleep(1)
    dell()
    list[0] = color_2
    list[1] = color_2
    list[2] = color_2
    list[3] = color_2
    list[4] = color_2
    list[5] = color_1
    list[6] = color_2
    list[7] = color_1
    list[8] = color_1
    print_matrix()
    time.sleep(1)
    dell()
    list[0] = color_2
    list[1] = color_2
    list[2] = color_2
    list[3] = color_2
    list[4] = color_2
    list[5] = color_2
    list[6] = color_2
    list[7] = color_2
    list[8] = color_1
    print_matrix()
    time.sleep(1)
    dell()
    list[0] = color_2
    list[1] = color_2
    list[2] = color_2
    list[3] = color_2
    list[4] = color_2
    list[5] = color_2
    list[6] = color_2
    list[7] = color_2
    list[8] = color_2
    print_matrix()
    time.sleep(1)
    dell()
    list[0] = color_1
    list[1] = color_1
    list[2] = color_1
    list[3] = color_1
    list[4] = color_1
    list[5] = color_1
    list[6] = color_1
    list[7] = color_1
    list[8] = color_1
    print_matrix()
    
    
    
    
simple_matrix()

        
        


