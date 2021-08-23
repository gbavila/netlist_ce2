from stamps import *

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
