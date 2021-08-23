
def file_readlines():

    with open('netlist.txt') as f: # O with já fecha o arquivo após sua finalização (f.close)
        lines = f.read().splitlines() 
    
    return lines
