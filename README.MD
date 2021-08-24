# Trabalho I - Circuitos Elétricos II
## Engenharia Eletrônica e de Computação - UFRJ
### Gabriel Almeida Avila e Silva

O programa tem o objetivo de calcular todas as tensões de nó de um dado circuito.
O input do programa é dado por um arquivo .txt representando a netlist do circuito. Cada linha representa um componente, informando suas principais informações. O padrão é o seguinte:

**Resistor**: <br/>
_R<identificação> <nó1> <nó2> <valor da resistência>_
<br/>

**Indutor**: <br/>
_L<identificação> <nó1> <nó2> <valor da indutância>_
<br/>

**Capacitor**:<br/> 
_C<identificação> <nó1> <nó2> <valor da capacitância>_
<br/>

**Transformador**: <br/>
_K<identificação> <nó a> <nó b> <nó c> <nó d> <valor da indutância mútua>_
<br/>

**Fonte de corrente**:

- **_Fonte DC_**:<br/>
_I<identificação> <nó cuja corrente é drenada pela fonte> <nó cuja corrente é injetada pela fonte> DC <valor da corrente>_

- **_Fonte senoidal ( amplitude\*cos(frequência\*t + fase) )_**:<br/>
_I<identificação> <nó cuja corrente é drenada pela fonte> <nó cuja corrente é injetada pela fonte> SIN <amplitude> <frequência> <fase>_
<br/>

**Fonte de corrente controlada por tensão**: <br/>
_G<identificação> <nóI(fonte drena a corrente desse nó)> <nóI(fonte injeta a corrente nesse nó)> <nóv(positivo)> <nóv(negativo)> <valor da transcondutância Gm>_
