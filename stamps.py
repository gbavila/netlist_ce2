from math import e

class Resistor(): 

    id = 'R'
    maior_no = int
    no1 = int
    no2 = int
    valor = float

    def __init__(self, line): # line = 'Rident 1 2 1'
        line = line.split()
        self.no1=int(line[-3])
        self.no2=int(line[-2])
        self.valor=float(line[-1])
        self.maior_no=int(max([self.no1,self.no2]))

    def applyStamp(self, matrix):
        matrix[self.no1][self.no1] += 1/self.valor
        matrix[self.no2][self.no2] += 1/self.valor
        matrix[self.no1][self.no2] += -1/self.valor
        matrix[self.no2][self.no1] += -1/self.valor


class Indutor():

    id = 'L'
    maior_no = int
    no1 = int
    no2 = int
    valor = float

    def __init__(self, line): # line = 'Lident 3 1 2'
        line = line.split()
        self.no1=int(line[-3])
        self.no2=int(line[-2])
        self.valor=float(line[-1])
        self.maior_no=int(max([self.no1,self.no2]))

    def applyStamp(self, G_matrix, freq):
        G_matrix[self.no1][self.no1] += 1/(1j*freq*self.valor)
        G_matrix[self.no2][self.no2] += 1/(1j*freq*self.valor)
        G_matrix[self.no1][self.no2] += -1/(1j*freq*self.valor)
        G_matrix[self.no2][self.no1] += -1/(1j*freq*self.valor)


class Capacitor():

    id = 'C'
    maior_no = int
    no1 = int
    no2 = int
    valor = float

    def __init__(self, line): # line = 'Cident 2 1 1'
        line = line.split()
        self.no1=int(line[-3])
        self.no2=int(line[-2])
        self.valor=float(line[-1])
        self.maior_no=int(max([self.no1,self.no2]))

    def applyStamp(self, G_matrix, freq):
        G_matrix[self.no1][self.no1] += 1j*freq*self.valor
        G_matrix[self.no2][self.no2] += 1j*freq*self.valor
        G_matrix[self.no1][self.no2] += -1j*freq*self.valor
        G_matrix[self.no2][self.no1] += -1j*freq*self.valor


class Transformador():

    id = 'K'
    maior_no = int
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
        self.maior_no=int(max([self.no_a,self.no_b,self.no_c,self.no_d]))


class FC(): # Fonte de corrente independente

    id = 'I'
    maior_no = int
    no1 = int # nó cuja corrente é drenada pela fonte
    no2 = int # nó cuja corrente é injetada pela fonte
    tipo = str
    amplitude = float
    freq = float
    fase = float
    valor = float

    def __init__(self, line): # line = 'Iident 0 1 2'
        line = line.split()
        self.no1=int(line[1])
        self.no2=int(line[2])
        if line[3] == 'DC' or line[3] == 'dc' or line[3] == 'Dc':
            self.valor=float(line[-1])
            self.tipo='DC'
        else:
            self.tipo='SIN'
            self.amplitude=float(line[4])
            self.freq=float(line[5])
            self.fase=float(line[6])

        self.maior_no=int(max([self.no1,self.no2]))

    def applyStamp(self, I_vector):
        if self.tipo == "DC":
            I_vector[self.no1] += -self.valor
            I_vector[self.no2] += self.valor
        else:
            I_vector[self.no1] += -self.amplitude*e**(1j*self.fase)
            I_vector[self.no2] += self.amplitude*e**(1j*self.fase)


class FCT(): # Fonte de corrente controlada por tensão

    id = 'G'
    maior_no = int
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
        self.maior_no=int(max([self.no_dreno,self.no_inject,self.no_controle_pos,self.no_controle_neg]))

    def applyStamp(self, G_matrix):
        G_matrix[self.no_dreno][self.no_controle_pos] += self.valor
        G_matrix[self.no_dreno][self.no_controle_neg] += -self.valor
        G_matrix[self.no_inject][self.no_controle_pos] += -self.valor
        G_matrix[self.no_inject][self.no_controle_neg] += self.valor


components_dict = {Resistor.id: Resistor,
                   Indutor.id: Indutor, 
                   Capacitor.id: Capacitor,
                   Transformador.id: Transformador, 
                   FC.id: FC, 
                   FCT.id: FCT}
                   