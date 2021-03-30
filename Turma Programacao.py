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

def addAluno (dicionario, semestre):
    '''Função que adiciona um aluno no semestre correspondente'''
    print('_'*80)
    if semestre == '1':
        print('2019.1')
    else:
        print('2019.2')
    nomeValido = False
    while not nomeValido:
        nome = input('NOME: ').upper()
        if nome in dicionario:
            print('\nNOME JÁ EXISTENTE, ABREVIE O SOBRENOME\n')
        else:
            faltas   = 0
            nota = 0
            dicionario[nome]=[semestre, faltas, nota]
            nomeValido = True
            print('CADASTRADO COM SUCESSO')

def popAluno (dicionario, semestre):
    '''Função que remove um aluno'''
    print('_'*80)
    if semestre == '1':
        print('2019.1')
    else:
        print('2019.2')
    nome = input('NOME DO ALUNO: ').upper()
    if nome in dicionario:
        if dicionario[nome][0] == semestre:
            dicionario.pop(nome)
            print('REMOVIDO COM SUCESSO')
        else:
            print('ALUNO NÃO ESTÁ CADASTRADO NESTE SEMESTRE')
    else:
        print('ALUNO NÃO CADASTRADO')

def notaAluno (dicionario,semestre):
    '''Função que atualiza a nota do aluno'''
    print('_'*80)
    if semestre == '1':
        print('2019.1')
    else:
        print('2019.2')
    nome = input('NOME DO ALUNO: ').upper()
    if nome in dicionario:
        if dicionario[nome][0] == semestre:
            nota = input('NOTA DO ALUNO: ')
            dicionario[nome]=(semestre, dicionario[nome][1], nota)
            print('NOTA ATRIBUIDA COM SUCESSO')
        else:
            print('ALUNO NÃO ESTÁ CADASTRADO NESTE SEMESTRE')
    else:
        print('ALUNO NÃO CADASTRADO')

def faltasAlunos(dicionario, semestre):
    '''Função que gera uma chamada de frequência dos alunos'''
    print('_'*80)
    if semestre == '1':
        print('2019.1')
    else:
        print('2019.2')
    print('\nFALTAS\nP - PRESENÇA\nF - FALTA\n')
    for aluno in dicionario:
        if dicionario[aluno][0] == semestre:
            valido = False
            while not valido:
                falta = input(f'{aluno}: ').upper()
                if falta == 'F':
                    dicionario[aluno][1] += 1
                    valido = True
                elif falta == 'P':
                    valido = True
    print('NOTAS ATUALIZADAS COM SUCESSO')

def relatorioDisciplina(dicionario, semestre, reprovados_1 = 0, reprovados_2 = 0):
    '''Função que gera um relatório geral da disciplina'''
    print('_'*80)

    matriculados_1 = verMatriculados(alunos, '1')
    matriculados_2 =  verMatriculados(alunos, '2')
    reprovados_1 = verReprovados(alunos, '1')
    reprovados_2 = verReprovados(alunos, '2')
    
    arq = open('relatorio-programacao.txt','w')
    arq.write(f'PROGRAMAÇÃO 2019.1\nNÚMERO DE ALUNOS MATRICULADOS: {matriculados_1}\nPERCENTUAL DE REPROVAÇÃO POR FALTA: {reprovados_1}%')
    arq.write('\n')
    arq.write('_'*80)
    arq.write('\n')
    arq.write(f'PROGRAMAÇÃO 2019.2\nNÚMERO DE ALUNOS MATRICULADOS: {matriculados_2}\nPERCENTUAL DE REPROVAÇÃO POR FALTA: {reprovados_2}%')
    arq.write('\n')
    arq.close()
    print('\nRELATÓRIO CRIADO COM SUCESSO')
        

def relatorioAlunosDisciplina(dicionario, semestre):
    '''Função que gera um relatório geral dos alunos da disciplina'''
    if semestre == '1':
        arq = open('programacao-2019-1.txt','w')
    elif semestre == '2':
        arq = open('programacao-2019-2.txt','w')
    for aluno in dicionario:
        if dicionario[aluno][0] == semestre:
            arq.write(f'ALUNO: {aluno}')
            arq.write('\n')
            arq.write(f'FALTAS: {dicionario[aluno][1]}')
            arq.write('\n')
            arq.write(f'NOTA: {dicionario[aluno][2]}')
            arq.write('\n')
            if dicionario[aluno][1] >= 8:
                arq.write('SITUAÇÃO: ALUNO REPROVADO POR FALTA')
                arq.write('\n'*2)
            if dicionario[aluno][2] < 7:
                arq.write('SITUAÇÃO: ALUNO REPROVADO POR MÉDIA')
                arq.write('\n'*2)
            if dicionario[aluno][1] < 8 and dicionario[aluno][2] >= 7:
                arq.write('SITUAÇÃO: ALUNO APROVADO')
                arq.write('\n'*2)
    arq.close()
    print('\nRELATÓRIO CRIADO COM SUCESSO')

def verMatriculados(dicionario, semestre, matriculados_1 = 0, matriculados_2 = 0):
    '''Função que calcula quantos matriculados há em cada semestre'''
    for aluno in dicionario:
        if dicionario[aluno][0] == '1':
            matriculados_1 += 1
        elif dicionario[aluno][0] == '2':
            matriculados_2 += 1
    if semestre == '1':
        return matriculados_1
    elif semestre == '2':
        return matriculados_2

def verReprovados(dicionario, semestre, reprovados_1 = 0, reprovados_2 = 0):
    '''Função que calcula em porcentagem quantos reprovados há em cada semestre'''
    for aluno in dicionario:
        if dicionario[aluno][1] >= 8:
            if dicionario[aluno][0] == '1':
                reprovados_1 += 1
            else:
                reprovados_2 += 1
    matriculados_1 = verMatriculados(alunos, '1')
    matriculados_2 = verMatriculados(alunos, '2')

    if matriculados_1 != 0:
        pReprovados_1 = float((100*reprovados_1)/matriculados_1)
    else:
        pReprovados_1 = 0
        
    if matriculados_2 != 0:
        pReprovados_2 = float((100*reprovados_2)/matriculados_2)
    else:
        pReprovados_2 = 0
    
    if semestre == '1':
        return pReprovados_1
    elif semestre == '2':
        return pReprovados_2

def menuP (dicionario, semestre):
    '''Função que gera o menu da disciplina'''
    op = True
    while op:
        print('_'*80)
        opP = input('\n1- ADICIONAR ALUNO\n2- REMOVER ALUNO\n3- ATRIBUIR NOTA DE UM ALUNO\n4- REGISTRAR FALTA DOS ALUNOS\n\n5- GERAR RELATÓRIO DA DISCIPLINA POR SEMESTRE\n6- GERAR RELATÓRIO DOS ALUNOS POR SEMESTRE\n\n7- SAIR\n')
        if opP == '1':
            addAluno(alunos, semestre)
        elif opP == '2':
            popAluno(alunos, semestre)
        elif opP == '3':
            notaAluno(alunos, semestre)
        elif opP == '4':
            faltasAlunos(alunos, semestre)
        elif opP == '5':
            relatorioDisciplina(alunos, semestre)
        elif opP == '6':
            relatorioAlunosDisciplina(alunos, semestre)
        elif opP == '7':
            op = False    

def menu():
    '''Função que gera o menu principal'''
    op = True
    while op:
        print('_'*80)
        opMenu = input('\n1- ACESSAR DADOS / PROGRAMAÇÃO\n2- SAIR\n')
        if opMenu == '1':
            semestre = input('\n<< SEMESTRE >>\n1- 2019.1\n2- 2019.2\n')
            menuP(alunos, semestre)
        elif opMenu == '2':
            op = False
    
#Alunos-padrão para facilitar o teste
#Não carreguei/salvei alunos em arquivos porque não foi pedido
alunos = {'VINICIUS LUIZ':['1',10,7],'LUIS GABRIEL':['1',3,4],'DANIEL MORAES':['1',3,10],'ALEXANDRO HENRIQUE':['2',3,6],'JOÃO PEDRO VELOSO':['2',3,8],'FLÁVIO HENRIQUE':['2',8,6]}
menu()
