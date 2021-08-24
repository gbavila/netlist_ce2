from functions import file_readlines, get_components, create_zeros_matrix, apply_stamps, solve_system, remove_ground_eq, print_system
import numpy as np

def main():

    lines = file_readlines()
    #print(f'lines: {lines}')
    components = get_components(lines)
    #print(f'componentes: {components}')
    
    G_matrix, I_vector = create_zeros_matrix(components)

    apply_stamps(G_matrix, I_vector, components)

    remove_ground_eq(G_matrix, I_vector)

    e_vector = solve_system(G_matrix, I_vector)
    
    print_system(G_matrix, I_vector, e_vector)



main()