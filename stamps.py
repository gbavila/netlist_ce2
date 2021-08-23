class Resistor(): 

    id = 'R'
    no1 = int
    no2 = int
    valor = float

    def __init__(self, line): # line = 'Rident 1 2 1'
        line = line.split()
        self.no1=int(line[-3])
        self.no2=int(line[-2])
        self.valor=float(line[-1])


class Indutor():

    id = 'L'
    no1 = int
    no2 = int
    valor = float

    def __init__(self, line): # line = 'Lident 3 1 2'
        line = line.split()
        self.no1=int(line[-3])
        self.no2=int(line[-2])
        self.valor=float(line[-1])


class Capacitor():

    id = 'C'
    no1 = int
    no2 = int
    valor = float

    def __init__(self, line): # line = 'Cident 2 1 1'
        line = line.split()
        self.no1=int(line[-3])
        self.no2=int(line[-2])
        self.valor=float(line[-1])


class Transformador():

    id = 'K'
    no_a = int
    no_b = int
    no_c = int
    no_d = int
    valor = float

    def __init__(self, line): # line = 'Kident 2 1 4 3 10'
        line = line.split()
        self.no_a=int(line[-5])
        self.no_b=int(line[-4])
        self.no_c=int(line[-3])
        self.no_d=int(line[-2])
        self.valor=float(line[-1])


class FC(): # Fonte de corrente independente

    id = 'I'
    no1 = int # nó cuja corrente é drenada pela fonte
    no2 = int # nó cuja corrente é injetada pela fonte
    valor = float

    def __init__(self, line): # line = 'Iident 0 1 2'
        line = line.split()
        self.no1=int(line[-3])
        self.no2=int(line[-2])
        self.valor=float(line[-1])


class FCT(): # Fonte de corrente controlada por tensão

    id = 'G'
    no_dreno = int
    no_inject = int
    no_controle_pos = int
    no_controle_neg = int
    valor = float

    def __init__(self, line): # line = 'Gident 2 1 4 3 10'
        line = line.split()
        self.no_dreno=int(line[-5])
        self.no_inject=int(line[-4])
        self.no_controle_pos=int(line[-3])
        self.no_controle_neg=int(line[-2])
        self.valor=float(line[-1])


components_dict = {Resistor.id: Resistor,
                   Indutor.id: Indutor, 
                   Capacitor.id: Capacitor,
                   Transformador.id: Transformador, 
                   FC.id: FC, 
                   FCT.id: FCT}
                   