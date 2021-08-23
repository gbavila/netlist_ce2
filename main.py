from functions import file_readlines, get_components

def main():

    lines = file_readlines()
    print(f'lines: {lines}')
    components = get_components(lines)
    print(f'componentes: {components}')
    for c in components:
        print(c,":", c.__dict__)

    return



main()