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

def notaFiscal(qtd, valor, imp_e, valorRefImp_e, imp_f, valorRefImp_f, cartao, total):
    '''Função que gera a nota fiscal no arquivo .txt'''
    arq = open('notaFiscal-q3.txt','a')
    arq.write(f'QUANTIDADE:{qtd}\nVALOR: R$ {valor}\nIMPOSTO ESTADUAL: {imp_e}% \t R$ {valorRefImp_e}\nIMPOSTO FEDERAL: {imp_f}% \t\t R$ {valorRefImp_f}0\nCARTÃO: {cartao}\nTOTAL: R${total}\n\n')
    arq.close()
    print('\nDADOS CADASTRADOS COM SUCESSO\n')

qtdVendas = int(input('QUANTAS VENDAS DESEJAS ADICIONAR: '))
for x in range(qtdVendas):
    qtd    = int(input('QUANTIDADE: '))
    valor  = float(input('VALOR: '))
    imp_e  = float(input('IMPOSTO ESTADUAL (%): '))
    imp_f  = float(input('IMPOSTO FEDERAL (%): '))

    cartao = int(input('CARTÃO (1 - DÉBITO / 2 - CRÉDITO / 3 - A VISTA): '))
    if cartao == 1:
        cartao = 'DÉBITO'
    elif cartao == 2:
        cartao = 'CRÉDITO'
    elif cartao == 3:
        cartao = 'A VISTA'
    else:
        cartao = 'DESCONHECIDO'
        
    valorTotal    = qtd*valor #valor total
    valorRefImp_e = (valorTotal*imp_e)/100 #valor levando em consideração apenas os impostos estaduais
    valorRefImp_f = (valorTotal*imp_f)/100 #valor levando em consideração apenas os impostos federais
    total         =  valorTotal + valorRefImp_e + valorRefImp_f

    notaFiscal(qtd, valor, imp_e, valorRefImp_e, imp_f, valorRefImp_f, cartao, total)
