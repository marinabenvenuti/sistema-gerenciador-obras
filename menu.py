import time
from datetime import datetime
import random
from obras import *
from funcionarios import *

def printarObra(i):
    contObras=1
    for i in obras:
        print('  ')
        print('ID:', i.cod)
        print ('Cliente: ', i.cliente)
        for j in range(len(i.materiais)):
            print (i.materiais[j]['nome'], "em quantidade de", i.materiais[j]['qtd'], "(unidade de medida em {})".format(i.materiais[j]['medição']))
        print('Mestre de obra:', i.pedreiro)
        print('Data de início:', i.dataIn)
        print('Data de fim:', i.dataFim)
        print('Valor total: R${}'.format(i.total))
    
    
#def verificaData(aux):
 #   verif = 0
  #  for i in range(10):
   #     #fazer função pra verificar se a data está certa
    

def verConsul(x):
    while not x in [1,2, 3, 4, 5, 6]:
        x=int(input("Digite novamente o número da ação: "))
    return x

def opcoesObras():
    while True:
        print("[--------------------------------Menu de Obras--------------------------------]")
        print("  ")
        print("1) Exibir todas as obras cadastradas")
        print("2) Pesquisar obra")
        print("3) Cadastrar obra")
        print("4) Editar obra")
        print("5) Excluir obra")
        print("6) Voltar para o menu principal")
        print("  ")
            
        consultaObra=int(input("Numero da ação a ser realizada: "))
        consultaObra=verConsul(consultaObra)
        
        if consultaObra==1:
            if len(obras)==0:
                print('Nenhuma obra cadastrada')
            else:
                print('--------------------------------Obras cadastradas:--------------------------------')
                pn=0
                printarObra(pn)
                    
        elif consultaObra==2:
            #pesquisa de obra específica
            if len(obras)==0:
                print('Nenhuma obra cadastrada')
            else:
                print('--------------------------------Pesquisar obra:--------------------------------')
                print('1 - Pesquisar pelo ID')
                print('2 - Pesquisar pelo nome do cliente')
                consulta2 = int(input('Escolha a forma de consulta: '))
                    
                if consulta2 == 1: # Consultar pelo ID
                    flag=False
                    c = str(input('Digite o ID: '))
                    for obr in obras:
                        if c == func.get_cod():
                            printarObra(obr)
                            flag = True
                        if flag == False:
                            print("ID não cadastrado!")
                            
                                
                elif consulta2 == 2: # Consultar pelo Nome
                    c = str(input('Digite o nome do cliente: '))
                    flag = False
                    for obr in obras:
                        if c == func.get_cod():
                            printarObra(obr)
                            flag = True
                        if flag == False:
                            print("Nome não cadastrado!")
                            
        elif consultaObra==3:
            #cadastro de nova obra
            materiais = []

            material = {}
            material['nome'] = str('areia')
            material['medição'] = str('m³')
            material['qtd'] = int(0)
            material['preço'] = float(170.00)
            materiais.append(material.copy())
    
            material = {}
            material['nome'] = str('cal')
            material['medição'] = str('kg')
            material['qtd'] = int(0)
            material['preço'] = float(13.00)
            materiais.append(material.copy())
    
            material = {}
            material['nome'] = str('brita')
            material['medição'] = str('m³')
            material['qtd'] = int(0)
            material['preço'] = float(96.00)
            materiais.append(material.copy())
    
            material = {}
            material['nome'] = str('cimento')
            material['medição'] = str('kg')
            material['qtd'] = int(0)
            material['preço'] = float(30.00)
            materiais.append(material.copy())
    
            material = {}
            material['nome'] = str('telha de aço')
            material['medição'] = str('m²')
            material['qtd'] = int(0)
            material['preço'] = float(20.00)
            materiais.append(material.copy())
    
            material = {}
            material['nome'] = str('vergalhão')
            material['medição'] = str('m')
            material['qtd'] = int(0)
            material['preço'] = float(16.00)
            materiais.append(material.copy())
            
            print('--------------------------------Cadastrar obra:--------------------------------')
                
            cliente = input('Cliente: ').title()
            
            o = Obra('', '', '', '', '', '', '') # cria o objeto Obra
            cod = random.randint(10000, 100000)
            o.setCod(cod)
            o.setCliente(cliente)
            
            for i in range (len(materiais)):
                print("O material", materiais[i]['nome'], "possui", materiais[i]['qtd'], "itens")
                add_num_mat=int(input("Quantos voce deseja adicionar? a medida é em {} com o valor de R${}: ".format(materiais[i]['medição'], materiais[i]['preço'])))
                materiais[i]['qtd']+=add_num_mat
                o.setMateriais(materiais)


            
            flag = False
            while True: #isso pode ser colocado numa função pois é usado na edição também
                nomePedr = input('Digite o nome completo do mestre de obra: ')
                for pedreiro in pedreiros:
                    if nomePedr == pedreiro.nome:
                        o.setPedreiro(nomePedr)
                        flag = True
                if flag==True:
                    break
            
            aux = str(input('Digite a data de início da obra no formado "DD/MM/AAAA": '))
            #data_inicio = verificaData(aux)
            dataIn = datetime.strptime(aux, '%d/%m/%Y')
            o.setDataIn(dataIn)
            
            aux = str(input('Digite a data de fim da obra no formado "DD/MM/AAAA": '))
            #data_fim = verificaData(aux)
            dataFim = datetime.strptime(aux, '%d/%m/%Y')
            o.setDataFim(dataFim)
            
            totalObra = 350*1.22
            for i in materiais:
                totalObra += material['qtd'] * material['preço']
            o.setTotal(totalObra)
            
            obras.append(o) #adicionando à lista de objetos obra
            print('Obra cadastrada com sucesso!')
            
        elif consultaObra == 4:
            print('--------------------------------Editar obra:--------------------------------')
            idO_pesquisa = str(input('Digite o ID da obra: '))
            flag=False
            for obra in obras:  # percorre a lista de obras
                if idO_pesquisa == obra.get_cod():  # busca pelo ID da obra a ser alterado
                    materiaisusados = []
                    print('Digite as novas informações de obra')
                    cliente = str(input('Cliente: ')).title
                    obra.set_cliente(cliente)
                    
                    aux = int(input('Digite a quantidade de materiais que serão utilizados: '))
                    while aux>len(materiais)+1:
                        aux = int(input('Valor inválido! Digite a quantidade de materiais que serão utilizados novamente: '))
                    materiaisusados.append(addMateriais(aux, materiaisusados))
                    obra.set_materiais(materiaisusados)
                    
                    flagg = False
                    while True:
                        nomePedr = input('Digite o nome completo do mestre de obra: ').title
                        for pedreiro in pedreiros:
                            if nomePedr == pedreiro.nome:
                                o.set_pedreiro(nomePedr)
                                flagg = True
                        if flagg==True:
                            break
                    
                    aux = str(input('Digite a data de início da obra no formado "DD/MM/AAAA": '))
                    data_inicio = verificaData(aux)
                    dataIn = datetime.strptime(data_inicio, '%d/%m/%Y')
                    obra.set_dataIn(dataIn)
            
                    aux = str(input('Digite a data de fim da obra no formado "DD/MM/AAAA": '))
                    data_fim = verificaData(aux)
                    dataFim = datetime.strptime(data_fim, '%d/%m/%Y')
                    obra.set_dataFim(dataFim)
            
                    totalObra = calculaObra(pedreirosusados, materiaisusados) #arrumar
                    obra.set_total(totalObra)
                    
                    flag=True
                if flag == False:
                    print("ID não encontrado!")
                    
        elif consultaObra == 5:
            #exclusão de obra
            print('--------------------------------Excluir obra:--------------------------------')
            idO_pesquisa = str(input('Digite o ID da obra: '))
            
            for i, j in enumerate(obras): # percorre a lista de obras
                if idO_pesquisa == j.get_cod():
                    obras.pop(i)
                    print("Exclusão efetuada com sucesso!")
                    flag=True
            if flag == False:
                print("Id não cadastrado!")
                
        elif consultaObra == 6:
            break
        
        
def opcoesFuncionarios():
    while True:
        print("[--------------------------------Menu de Funcionários--------------------------------]")
        print("  ")
        print("1) Exibir todos os funcionários cadastrados")
        print("2) Pesquisar funcionário")
        print("3) Cadastrar funcionário")
        print("4) Editar funcionário")
        print("5) Excluir funcionário")
        print("6) Voltar para o menu principal")
        print("  ")
            
        consultaFunc=int(input("Numero da ação a ser realizada: "))
        consultaFunc=verConsul(consultaFunc)
        
        if consultaFunc==1:
            #exibir todos os funcionários da empresa
            if funcionarios==[]:
                print('Nenhum funcionário cadastrado')
            
            else:
                print("[--------------------------------Funcionários cadastrados:--------------------------------]")
                for i in funcionarios:
                    print ("   ")
                    print ('Cargo:', i.__class__.__name__)
                    print ('Cadastro:', i.cadastro)
                    print ('Nome:', i.nome)
                    print ('Salario: R${}'.format(i.salario))
                    print ('CPF: {}.{}.{}-{}'.format(i.cpf[0:3], i.cpf[3:6], i.cpf[6:9], i.cpf[9:11]))
                    print ('Contato: {}-{}'.format(i.fone[0:5], i.fone[5:9]))

                    if i.__class__.__name__=='Gestor':
                        print ('Data contrataçao:', i.anoContrat)
                    if i.__class__.__name__=='Pedreiro':
                        print ('Presente em {} obras'.format(i.NumObras))
                        
        if consultaFunc==2:
            #pesquisa de funcionário específico
            print("[--------------------------------Pesquisar funcionário:--------------------------------]")
            Pes_Fun=input('Nome do funcionario a ser pesquisado: ').title()
            for i in funcionarios:
                if i.nome==Pes_Fun:
                    print ("   ")
                    print ('Cargo:', i.__class__.__name__)
                    print ('Cadastro:', i.cadastro)
                    print ('Nome:', i.nome)
                    print ('Salario: R${}'.format(i.salarioTot))
                    print ('CPF: {}.{}.{}-{}'.format(i.cpf[0:3], i.cpf[3:6], i.cpf[6:9], i.cpf[9:11]))
                    print ('Contato: {}-{}'.format(i.fone[0:5], i.fone[5:9]))
                    
                    if i.__class__.__name__=='Gestor':
                        print ('Data contrataçao:', i.contra)
                    if i.__class__.__name__=='Pedreiro':
                        print ('Presente em {} obras'.format(i.NumObras))
                        
        if consultaFunc==3:
            #cadastro de novo funcionário
            print("[--------------------------------Cadastrar funcionário:--------------------------------]")
            print(' ')

            Faz_Cad=input('O que deseja cadastrar? ').title()   
            Fun_Nome=input('Nome do Funcionario: ').title()
            Fun_CPF=input('CPF do funcionario[sem"." e "-"]: ')
            Fun_Fone=input('Telefone do Funcionario[Com "9" e sem DDD]: ')
            Fun_Cadastro=(random.randint(10000,100000))
            Fun_Salario =1500
               
            
            
            if Faz_Cad=='Gestor':
                anoContrat = int(input('Digite o ano da contratação[AAAA]: '))
                Gestor(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario, anoContrat)
                
                
            elif Faz_Cad=='Pedreiro':
                Pedreiro(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario)
                
                
        if consultaFunc==4:
            #edição de funcionário
            print("[--------------------------------Editar funcionário:--------------------------------]")
            print(' ')
            editFunc = input('Digite o nome completo do funcionário a ser editado: ')
            for i in funcionarios:
                if i.nome == editFunc:
                    nome = input('Digite o novo nome do funcionário: ')
                    i.setNome(nome)
                    
                    cpf = input('Digite o novo cpf do funcionário: ')
                    i.setCpf(cpf)
                    
                    fone = input('Digite o novo telefone do funcionário: ')
                    i.setFone(fone)
                    
                    if i.__class__.__name__=='Gestor':
                        contratacao = int(input('Digite o novo ano de contratação do funcionário: '))
                        i.setContra(contratacao)
                        
        if consultaFunc==5:
            #exclusão de funcionário
            print("[--------------------------------Excluir funcionário:--------------------------------]")
            print('   ')
            Del_Fun=input('Digite o nome completo do funcionario a ser excluido: ').title()
            for i in funcionarios:
                if i.nome==Del_Fun:
                    print ("   ")
                    print ('Cargo:', i.__class__.__name__)
                    print ('Cadastro:', i.cadastro)
                    print ('Nome:', i.nome)
                    print ('Salario: R${}'.format(i.salario))
                    print ('CPF: {}.{}.{}-{}'.format(i.cpf[0:3], i.cpf[3:6], i.cpf[6:9], i.cpf[9:11]))
                    print ('Contato: {}-{}'.format(i.fone[0:5], i.fone[5:9]))
                    
                    if i.__class__.__name__=='Gestor':
                        print ('Data contrataçao:', i.contra)
                    if i.__class__.__name__=='Pedreiro':
                        print ('Presente em {} obras'.format(i.NumObras))

                    print('   ')
                    Del_Fun_F=input('Excluir este funcionario?').title()
                    if Del_Fun_F=='Sim':
                        funcionarios.remove(i)
                        print('Funcionário deletado com sucesso')
                else:
                    print('Funcionário não cadastrado')
                    
        if consultaFunc==6:
            break
        
def faturamento():
    print("[--------------------------------Faturamento atual:--------------------------------]")
    dinheiroGestores = 0
    for i in gestores:
        dinheiroGestores = i.salario
    aux = 0    
    for i in pedreiros:
        aux += i.salario-1000
    
    dinheiroPedreiros = len(pedreiros)*1000
    
    for i in obras:
        dinheiroObras = i.total-aux
    dinTotal = dinheiroObras - dinheiroGestores - dinheiroPedreiros
    print(f'O faturamento atual da empresa é de R${dinTotal}')
    
def consultaMain(x):
    while not x in [1,2, 3, 4]:
        x=int(input("Digite novamente o número da ação: "))
    return x

#main
funcionarios.append(Pedreiro('Iago Munoz', '00000000000', '999999999', 12345, 1500))
funcionarios.append(Gestor('Marina Benvenuti', '11111111111', '908888888', 23412, 1500, 2022))

while True:
    print ("  ")
    print("[--------------------Sistema Gerenciador de Obras--------------------]")
    print("[--------------------------------Menu--------------------------------]")
    print("  ")
    print("1) Obras")
    print("2) Funcionários")
    print("3) Faturamento da empresa")
    print("4) Encerrar programa")
    print("  ")
        
    consulta=int(input("Numero da ação a ser realizada: "))
    consulta=consultaMain(consulta)
    
    if consulta == 1:
        opcoesObras()
            
    elif consulta == 2:
        opcoesFuncionarios()
        
    elif consulta == 3:
        faturamento()
    
    elif consulta == 4:
        print("Programa encerrando...")
        for i in range (2):
            print("...")
            time.sleep(1)
            
        print("Por: Marina Benvenuti e Iago Munoz")
        print("Com agradecimentos a Alan Turing, ateu e homossexual, o pai da computação.")
        break
