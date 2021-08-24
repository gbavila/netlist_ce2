from stamps import *
import numpy as np

def file_readlines():

    with open('netlist.txt') as f: # O with já fecha o arquivo após sua finalização (f.close)
        lines = f.read().splitlines() 
    
    return lines

def get_components(file_lines):

    components = []

    for line in file_lines:
        id = line[0]
        component = components_dict[id](line=line)
        components.append(component) # components_dict definido no arquivo stamps.py

    return components

def create_zeros_matrix(components):
    greater_node = 0
    for comp in components: # Descobrir o tamanho da matriz
        if comp.maior_no > greater_node:
            greater_node = comp.maior_no

    G_matrix = []
    I_vector = []
    # Criar matriz quadrada de zeros
    for count1 in range(0, greater_node+1, 1):
        G_matrix.append([])
        I_vector.append(0)
        for count2 in range(0, greater_node+1, 1):
            G_matrix[count1].append(0)

    return G_matrix, I_vector

def apply_stamps(G_matrix, I_vector, components):

    for comp in components:
        if comp.id == FC.id:
            comp.applyStamp(I_vector)
        else:
            comp.applyStamp(G_matrix)

def solve_system(G_matrix, I_vector):

    G = np.array(G_matrix)

    I = np.array(I_vector)

    e = np.linalg.solve(G,I)

    return e

def remove_ground_eq(G_matrix, I_vector):
    G_matrix.pop(0)
    I_vector.pop(0)

    for count in range(0,len(G_matrix),1):
        G_matrix[count].pop(0)
