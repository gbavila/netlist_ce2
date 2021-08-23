class Resistor(): 

    id = 'R'
    no1 = int
    no2 = int
    valor = float

    def __init__(self, line): # line = 'Rident 1 2 1'
        self.no1=int(line[-5])
        self.no2=int(line[-3])
        self.valor=int(line[-1])


class Indutor():

    id = 'L'
    no1 = int
    no2 = int
    valor = float


class Capacitor():

    id = 'C'
    no1 = int
    no2 = int
    valor = float


class Transformador():

    id = 'K'
    no_a = int
    no_b = int
    no_c = int
    no_d = int
    valor = float


class FC(): # Fonte de corrente independente

    id = 'I'
    no1 = int # nó cuja corrente é drenada pela fonte
    no2 = int # nó cuja corrente é injetada pela fonte
    valor = float

    def __init__(self, line): # line = 'Iident 0 1 2'
        self.no1=int(line[-5])
        self.no2=int(line[-3])
        self.valor=int(line[-1])


class FCT(): # Fonte de corrente controlada por tensão

    id = 'G'
    no_dreno = int
    no_inject = int
    no_controle_pos = int
    no_controle_neg = int
    valor = float


components_dict = {Resistor.id: Resistor,
                   Indutor.id: Indutor, 
                   Capacitor.id: Capacitor,
                   Transformador.id: Transformador, 
                   FC.id: FC, 
                   FCT.id: FCT}
                   