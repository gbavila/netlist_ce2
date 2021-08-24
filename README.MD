# Trabalho I - Circuitos Elétricos II
## Engenharia Eletrônica e de Computação - UFRJ
#### Gabriel Almeida Avila e Silva

O programa tem o objetivo de calcular todas as tensões de nó de um dado circuito.
O input do programa é dado por um arquivo .txt representando a netlist do circuito. Cada linha representa um componente, informando suas principais informações. O padrão é o seguinte:

• Resistor: R<identificação> <nó1> <nó2> <valor da resistência>
• Indutor: L<identificação> <nó1> <nó2> <valor da indutância>
• Capacitor: C<identificação> <nó1> <nó2> <valor da capacitância>
• Transformador: K<identificação> <nó a> <nó b> <nó c> <nó d> <valor da indutância mútua>
• Fonte de corrente: I<identificação> <nó cuja corrente é drenada pela fonte> <nó cuja corrente é injetada pela fonte> <valor da corrente>
• Fonte de corrente controlada por tensão: G<identificação> <nóI(fonte drena a corrente desse nó)> <nóI(fonte injeta a corrente nesse nó)> <nóv(positivo)> <nóv(negativo)> <valor da transcondutância Gm>
