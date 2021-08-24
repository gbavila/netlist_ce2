from functions import (file_readlines, get_components, create_zeros_matrix, apply_stamps, 
                       solve_system, remove_ground_eq, print_system, find_circuit_freq)
import numpy as np

def main():

    lines = file_readlines()
    components = get_components(lines)
    
    G_matrix, I_vector = create_zeros_matrix(components)

    freq = find_circuit_freq(components)  # Assumindo que o circuito só terá uma frequência nas fontes de corrente

    apply_stamps(G_matrix, I_vector, components, freq)

    remove_ground_eq(G_matrix, I_vector)
    
    e_vector = solve_system(G_matrix, I_vector)

    print_system(G_matrix, I_vector, e_vector)


main()