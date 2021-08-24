from functions import file_readlines, get_components, create_zeros_matrix, apply_stamps, solve_system, remove_ground_eq

def main():

    lines = file_readlines()
    print(f'lines: {lines}')
    components = get_components(lines)
    print(f'componentes: {components}')
    #for c in components:
     #   print(c,":", c.__dict__)
    
    G_matrix, I_vector = create_zeros_matrix(components)
    #print(f'Zero matrix (G): \n {G_matrix}\n\n Zero I_vector: \n{I_vector}\n')

    apply_stamps(G_matrix, I_vector, components)
    #print(f'Applied G_matrix: \n {G_matrix}\n\n Applied I_vector: \n{I_vector}\n')

    remove_ground_eq(G_matrix, I_vector)

    e_vector = solve_system(G_matrix, I_vector)

    print(f'\n\nMatriz de transcondutâncias: \n{G_matrix}\n\n\
        Vetor de correntes: \n{I_vector}\n\n\
        Vetor de tensões: \n{e_vector}\n')

    return


main()