# URI JUDGE

Esse repositório contém os enunciados e as soluções criadas para os problemas propostos no site [URI JUDE](https://www.urionlinejudge.com.br).
## 1 - Nivel Iniciante

### Extremamente Básico
#### Problema - 1001
|Enunciado|
|-|
|Leia 2 valores **inteiros** e armazene-os nas variáveis **A** e **B**. Efetue a **soma** de **A** e **B** atribuindo o seu resultado na variável **X**. Imprima **X** conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".|
|**Entrada:** A entrada contém 2 valores inteiros.|
|**Saída:** Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha. Cuide para que tenha um espaço antes e depois do sinal de igualdade, conforme o exemplo abaixo.|

| Exemplos de Entrada | Exemplos de Saída |
|---------------------|-------------------|
|10 <br> 9            | X = 19            |
-10 <br> 4            | X = -6            |
|15 <br>-7            |X = 8              | 

<hr>

### Área do Círculo
#### Problema - 1002
|Enunciado|
|-|
|A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159: <br> - Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.|
|**Entrada:** A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.|
|**Saída:** Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".|

|Exemplos de Entrada|Exemplos de Saída|
|-------------------|-----------------|
|2.00               |A=12.5664        |
|100.64             |A=31819.3103     |
|150.00             |A=70685.7750     |

<hr>

### Soma Simples
#### Problema - 1003

|Enunciado|
|-|
|Leia dois valores inteiros, no caso para variáveis A e B. A seguir, calcule a soma entre elas e atribua à variável SOMA. A seguir escrever o valor desta variável.|
|**Entrada:** O arquivo de entrada contém 2 valores inteiros.|
|**Saída:** Imprima a variável SOMA com todas as letras maiúsculas, com um espaço em branco antes e depois da igualdade seguido pelo valor correspondente à soma de A e B. Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".|

| Exemplos de Entrada | Exemplos de Saída |
|---------------------|-------------------|
| 30 <br> 10          | SOMA = 40         |
| -30 <br> 10         | SOMA = -20        |
| 0 <br> 0            | SOMA = 0          |

<hr>

### Produto Simples
#### Problema - 1004

|Enunciado|
|-|
|Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.|   
|**Entrada:** O arquivo de entrada contém 2 valores inteiros.|
|**Saída:** Imprima a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. Não esqueça de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation Error”.|

| Exemplos de Entrada | Exemplos de Saída |
|---------------------|-------------------|
| 3 <br> 9            | PROD = 27         |
| -30 <br> 10         | PROD = -300       |
| 0 <br> 9            | PROD = 0          |

<hr>

### Média 1
#### Problema - 1005

|Enunciado|
|-|
|Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.|
|**Entrada:** O arquivo de entrada contém 2 valores com uma casa decimal cada um.|
|**Saída:** Calcule e imprima a variável MEDIA conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".|

| Exemplos de Entrada | Exemplos de Saída |
|---------------------|-------------------|
| 5.0 <br> 7.1        | MEDIA = 6.43182   |
| 0.0 <br> 7.1        | MEDIA = 4.84091   |
| 10.0 <br> 10.0      | MEDIA = 10.00000  |

<hr>

### Média 2
#### Problema - 1006

|Enunciado|
|-|
|Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.|
|**Entrada:** O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).|
|**Saída:** Imprima a variável MEDIA conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade. Assim como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".|

|   Exemplos de Entrada   | Exemplos de Saída |
|-------------------------|-------------------|
| 5.0 <br> 6.0 <br> 7.0   | MEDIA = 6.3       |
| 5.0 <br> 10.0 <br> 10.0 | MEDIA = 9.0       |
| 10.0 <br> 10.0 <br> 5.0 | MEDIA = 7.5       |

<hr>

### Diferença
#### Problema - 1007

|Enunciado|
|-|
| Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).|
|**Entrada:** O arquivo de entrada contém 4 valores inteiros.|
|**Saída:** Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.|

|   Exemplos de Entrada   | Exemplos de Saída |
|-------------------------|-------------------|
| 5 <br> 6 <br> 7 <br> 8  | DIFERENCA = -26   |
| 0 <br> 0 <br> 7 <br> 8  | DIFERENCA = -56   |
| 5 <br> 6 <br> -7 <br> 8 | DIFERENCA = 86    |

<hr>

### Salário
#### Problema - 1008

|Enunciado|
|-|
|Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.|
|**Entrada:** O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.|
|**Saída:** Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.|

|  Exemplos de Entrada  |          Exemplos de Saída          |
|-----------------------|-------------------------------------|
| 25 <br> 100 <br> 5.50 | NUMBER = 25 <br> SALARY = U$ 550.00 |
| 1 <br> 200 <br> 20.50 | NUMBER = 1 <br> SALARY = U$ 4100.00 |
| 6 <br> 145 <br> 15.55 | NUMBER = 6 <br> SALARY = U$ 2254.75 | 

<hr>

### Salário com Bônus
#### Problema - 1009

|Enunciado|
|-|
|Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha **15% de comissão** sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.|
|**Entrada:** O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.|
|**Saída:** Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.|

|      Exemplos de Entrada       | Exemplos de Saída  |
|--------------------------------|--------------------|
| JOAO <br> 500.00 <br> 1230.30  | TOTAL = R$ 684.54  |
| PEDRO <br> 700.00 <br> 0.00    | TOTAL = R$ 700.00  |
| JOSE <br> 1700.00 <br> 1230.50 | TOTAL = R$ 1884.58 |

<hr>

### Cálculo Simples
#### Problema - 1010

|Enunciado|
|-|
|Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.|
|**Entrada:** O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.|
|**Saída:** A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.|

|    Exemplos de Entrada     |    Exemplos de Saída    |
|----------------------------|-------------------------|
| 12 1 5.30 <br> 16 2 5.10   | VALOR A PAGAR: R$ 15.50 |
| 13 2 15.30 <br> 161 4 5.20 | VALOR A PAGAR: R$ 51.40 |
| 1 1 15.10 <br> 2 1 15.10   | VALOR A PAGAR: R$ 30.20 |
