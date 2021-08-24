from stamps import *
import numpy as np

def print_start_menu():
    print()
    print(35*"*")
    print("Trabalho I - Circuitos Elétricos II\nGabriel Almeida Avila e Silva\n")
    print(35*"*")
    print("O seu arquivo da netlist deve estar na mesma pasta do arquivo main.py.\nCaso contrário, especifique todo o caminho para ele (path)")

def file_readlines(file_name):

    with open(f'{file_name}') as f: # O with já fecha o arquivo após sua finalização (f.close)
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

def apply_stamps(G_matrix, I_vector, components, sys_freq):

    for comp in components:
        if comp.id == FC.id:
            comp.applyStamp(I_vector)
        elif comp.id == Capacitor.id or comp.id == Indutor.id or comp.id == Transformador.id:
            comp.applyStamp(G_matrix, sys_freq)
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

def print_system(G_matrix, I_vector, e_vector):

    print(f'\nMatriz de transcondutâncias: \n{np.array(G_matrix)}\n')
    print(f'Vetor de correntes: \n{np.array(I_vector)}\n')
    print(f'Vetor de tensões: \n{np.array(e_vector)}\n')

    print("\nResultados Aproximados:\n")
    for i in range (0, len(e_vector),1):
        print(f'e{i+1} = {round(e_vector[i],3)} V')
    print()

def find_circuit_freq(components):

    for c in components:
        if c.id == FC.id and c.tipo == "SIN":
            return c.freq
    return None
    