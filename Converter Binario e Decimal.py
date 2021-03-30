print('''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor: Vinícius Luiz da Silva França (vlsf2)
Email: vlsf2@cin.ufpe.br
Data: 2019-11-24

Copyright(c) 2019 Vinícius Luiz da Silva França
''')

def removerEspaco (string):
    '''Função quer remove \\n das strings'''
    novaString = ''
    for caractere in string:
        if caractere != '\n':
            novaString += caractere
    return novaString

def lerBinarios(cont = 0, binarios = {}):
    '''Função que ler todos os números decimais e seu correspondente em base binária'''
    arq = open('binario.txt','r')
    linhas = arq.readlines()
    numeros = len(linhas)//2
    arq.close()
    while cont < numeros:
        binarios[int(removerEspaco(linhas[2*cont]))] = int(removerEspaco(linhas[2*cont+1]))
        cont +=1
    return binarios

def lerDecimais(cont = 0, decimais = {}):
    '''Função que ler todos os números binários e seu correspondente em base decimal'''
    arq = open('decimal.txt','r')
    linhas = arq.readlines()
    numeros = len(linhas)//2
    arq.close()
    while cont < numeros:
        decimais[int(removerEspaco(linhas[2*cont]))] = int(removerEspaco(linhas[2*cont+1]))
        cont +=1
    return decimais

def salvarBinarios (dicionario):
    '''Função para salvar números convertidos em binários'''
    arq = open('binario.txt','w')
    for numero in dicionario:
        arq.write(str(numero))
        arq.write('\n')
        arq.write(str(dicionario[numero]))
        arq.write('\n')
    arq.close()

def salvarDecimais (dicionario):
    '''Função para salvar números convertidos em decimais'''
    arq = open('decimal.txt','w')
    for numero in dicionario:
        arq.write(str(numero))
        arq.write('\n')
        arq.write(str(dicionario[numero]))
        arq.write('\n')
    arq.close()

def inverterBinario(string, novaString = '', cont = 0, cont2 = -1):
    '''Função para inverter os número binário gerado'''
    if cont == len(string):
        return novaString
    else:
        novaString += string[cont2]
        cont +=1
        cont2 -= 1
        return inverterBinario(string, novaString, cont, cont2)    

def convBinario(quociente, binario = '',verificado = False):
    '''Função para converter um número em binário'''
    if quociente in binarios and not verificado:
        verificado = True
        return binarios[quociente]
    else:
        verificado = True
        if quociente == 1:
            binario += '1'
            binario = inverterBinario(binario)
            return binario
        elif quociente == 0:
            binario += '0'
            binairo = inverterBinario(binario)
            return binario
        else:
            num = quociente//2
            resto = quociente%2
            binario += str(resto)
            return convBinario(num, binario, verificado)

def convDecimal (num, decimal = 0, cont = 0, cont2 = -1, verificado = False):
    '''Função para converter um número em decimal'''
    if num in decimais and not verificado:
        verificado = True
        return decimais[num]
    else:
        verificado = True
        if cont == len(str(num)):
            return decimal
        else:
            decimal += (2**cont)*int(str(num)[cont2])
            cont +=1
            cont2 -= 1
            return convDecimal(num, decimal, cont, cont2, verificado)

        
binarios = lerBinarios()
decimais = lerDecimais()
    
programa = True
while programa:
    op = input('\n1- CONVERTER DECIMAL P/ BINÁRIO\n2- CONVERTER BINÁRIO P/ DECIMAL\n3- SAIR\n')
    if op == '1':
        num = int(input('DIGITE O NÚMERO DECIMAL: '))
        result = (convBinario(num))
        print(result)
        binarios[num] = result
    elif op == '2':
        num = int(input('DIGITE O NÚMERO BINÁRIO: '))
        result = (convDecimal(num))
        print(result)
        decimais[num] = result
    elif op == '3':
        programa = False

salvarBinarios(binarios)
salvarDecimais(decimais)

