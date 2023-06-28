#Marina Benvenuti Cardeal 23103131
#Iago Rodrigues Munoz 23104313
import time
from datetime import datetime 
import random
from obras import *
from funcionarios import *

def printarObra(i):
    for i in obras:    
        print("    ")
        print('ID:', i.cod)
        print ('Cliente: ', i.cliente)
        for j in range(len(i.materiais)):
            print (i.materiais[j]['nome'], "em quantidade de", i.materiais[j]['qtd'], "(unidade de medida em {})".format(i.materiais[j]['medição']))
        print('Mestre de obra:', i.pedreiro.nome)
        print('Data de início:', i.dataIn)
        print('Data de fim:', i.dataFim)
        print('Valor total: R${:.2f}'.format(i.total))
        time.sleep(0.5)
        
def printarObrass(i):    
    print("    ")
    print('ID:', i.cod)
    print ('Cliente: ', i.cliente)
    for j in range(len(i.materiais)):
        print (i.materiais[j]['nome'], "em quantidade de", i.materiais[j]['qtd'], "(unidade de medida em {})".format(i.materiais[j]['medição']))
    print('Mestre de obra:', i.pedreiro.nome)
    print('Data de início:', i.dataIn)
    print('Data de fim:', i.dataFim)
    print('Valor total: R${:.2f}'.format(i.total))
    time.sleep(0.5)
        
def semObra():
    print("    ")
    print('Nenhuma obra cadastrada')
    time.sleep(1.5)
    
def semFuncionario():
    print("    ")
    print('Nenhum funcionário cadastrado')
    time.sleep(1.5)
    
def verificaNumeros(x, valor):
    print("    ")
    while len(valor)!=x or not valor.isdigit():
        valor=input('Valor inválido! Digite novamente: ')    
    return valor

def verificaAno(anoContrat):
    while not anoContrat.isdigit():
        print("    ")
        anoContrat = input('Digite o ano novamente: ')
    anoContrat = int(anoContrat)
    print("    ")
    while anoContrat<1990: #supomos que a empresa foi criada em 1990
        anoContrat = int(input('Valor inválido! Digite o ano da contratação[AAAA]: '))
    return anoContrat

def verificaSN(x):
    print("    ")
    while x!='S' and x!='N':
        x = input('Inválido! Digite S para sim e N para não: ')
    return x

def verificaNs(x):
    while not x.isdigit():
        print("    ")
        x = input('Digite o valor novamente: ')
    x = int(x)
    return x        

def verificaData(aux):
    if len(aux)!=10:
        return False
    if (aux[2]!='/' or aux[5]!='/'):
        return False
    if not (aux[0].isdigit() and aux[1].isdigit() and aux[3].isdigit() and aux[4].isdigit() and aux[6].isdigit() and aux[7].isdigit() and aux[8].isdigit() and aux[9].isdigit()):
        return False
    dia, mes, ano = aux.split("/")
    ano = int(ano)
    dia = int(dia)
    mes = int(mes)
    if ano>1990: #supondo que a empresa iniciou em 1990
        if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
            if(dia<=31):
                return True
        if (mes==4 or mes==6 or mes==9 or mes==11):
            if(dia<=30):
                return True
        if mes==2:
            if (ano%4==0 and ano%100!=0) or (ano%400==0):
                if(dia<=29):
                    return True
            if(dia<=28):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def verConsul(x):
    while not x in ['1','2', '3', '4', '5', '6']:
        print("    ")
        x=(input("Digite novamente o número da ação: "))
    return x

def consultaMain(x):
    while not x in ['1', '2', '3', '4']:
        print("    ")
        x=(input("Digite novamente o número da ação: "))
    return x

def opcoesObras():
    while True:
        print("    ")
        print("[--------------------------------Menu de Obras--------------------------------]")
        print("    ")
        print("1) Exibir todas as obras cadastradas")
        print("2) Pesquisar obra")
        print("3) Cadastrar obra")
        print("4) Editar obra")
        print("5) Excluir obra")
        print("6) Voltar para o menu principal")
        print("    ")
   
        consultaObra=(input("Numero da ação a ser realizada: "))
        
        consultaObra=verConsul(consultaObra)
        consultaObra=verificaNs(consultaObra)
        
        if consultaObra==1:
            print("    ")
            print('[--------------------------------Obras cadastradas:--------------------------------]')
            
            if len(obras)==0:
                semObra()        
            else:   
                pn=0
                printarObra(pn)
                    
        elif consultaObra==2:
            #pesquisa de obra específica
            print("    ")
            print('[--------------------------------Pesquisar obra:--------------------------------]')
            
            if len(obras)==0:
                semObra()
                
            else:
                print("    ")
                cliente_pesquisa = input('Digite o id da obra a ser pesquisada: ')
                flag=False
                for i in obras:  # percorre a lista de obras
                    if int(cliente_pesquisa) == i.cod: 
                        printarObrass(i)
                        flag=True
                        
                if flag==False:
                    print("    ")
                    print('Obra não cadastrada')
                    time.sleep(1)
                            
        elif consultaObra==3:
            #cadastro de nova obra
            materiais = []

            material = {}
            material['nome'] = str('Areia')
            material['medição'] = str('m³')
            material['qtd'] = int(0)
            material['preço'] = float(170.00)
            materiais.append(material.copy())
    
            material = {}
            material['nome'] = str('Cal')
            material['medição'] = str('kg')
            material['qtd'] = int(0)
            material['preço'] = float(13.00)
            materiais.append(material.copy())
    
            material = {}
            material['nome'] = str('Brita')
            material['medição'] = str('m³')
            material['qtd'] = int(0)
            material['preço'] = float(96.00)
            materiais.append(material.copy())
    
            material = {}
            material['nome'] = str('Cimento')
            material['medição'] = str('kg')
            material['qtd'] = int(0)
            material['preço'] = float(30.00)
            materiais.append(material.copy())
    
            material = {}
            material['nome'] = str('Telha de aço')
            material['medição'] = str('m²')
            material['qtd'] = int(0)
            material['preço'] = float(20.00)
            materiais.append(material.copy())
    
            material = {}
            material['nome'] = str('Vergalhão')
            material['medição'] = str('m')
            material['qtd'] = int(0)
            material['preço'] = float(16.00)
            materiais.append(material.copy())

            print("    ")
            print('[--------------------------------Cadastrar obra:--------------------------------]')
            print("    ")
            cliente = input('Cliente: ').title()  
            o = Obra('', '', '', '', '', '', '') # cria o objeto Obra
            cod = random.randint(10000, 100000)
            o.setCod(cod)
            o.setCliente(cliente)
            vargra=0
            
            for i in range (len(materiais)):
                print("    ")
                print("O material", materiais[i]['nome'], "possui", materiais[i]['qtd'], "itens")
                add_num_mat=str(input("Quantos voce deseja adicionar? a medida é em {} com o valor de R${}: ".format(materiais[i]['medição'], materiais[i]['preço'])))
                add_num_mat = verificaNs(add_num_mat)
                materiais[i]['qtd']+=add_num_mat
                vargra+=(materiais[i]['preço']*add_num_mat*1.22)
                o.setMateriais(materiais)
  
            flag = False
            print("    ")
            cont=0
            while True: #isso pode ser colocado numa função pois é usado na edição também
                if cont==0:
                    nomePedr = input('Digite o nome completo do mestre de obra: ').title()
                else:
                    nomePedr = input('O mestre de obras digitado não está cadastrado. Tente novamente: ').title()
                for pedreiro in pedreiros:
                    if nomePedr == pedreiro.nome:
                        o.setPedreiro(pedreiro)    
                        flag = True
                if flag==True:
                    break
                cont+=1
            
            print("    ")
            aux = str(input('Digite a data de início da obra no formato "DD/MM/AAAA": '))
            dataIn = verificaData(aux)
            while dataIn==False:
                aux = str(input('Data inválida! Digite a data de início da obra no formato "DD/MM/AAAA": '))
                dataIn = verificaData(aux)
            dataIn = datetime.strptime(aux, '%d/%m/%Y')
            o.setDataIn(dataIn)
            
            print("    ")
            cont=0
            while True:
                if cont==0:
                    aux = str(input('Digite a data de fim da obra no formato "DD/MM/AAAA": '))
                else:
                    aux = str(input('Data inválida! Digite a data de fim da obra no formato "DD/MM/AAAA": '))
                dataFim = verificaData(aux)
                while dataFim==False:
                    aux = str(input('Data inválida! Digite a data de fim da obra no formato "DD/MM/AAAA": '))
                    dataFim = verificaData(aux)
                dataFim = datetime.strptime(aux, '%d/%m/%Y')

                if dataIn<dataFim:
                    break
                cont+=1
            o.setDataFim(dataFim) 
            months = (o.dataFim.year - o.dataIn.year) * 12 + (o.dataFim.month - o.dataIn.month)
            vargra+=((months+1)*350*1.22)
            o.setTotal(vargra)     
            obras.append(o) #adicionando à lista de objetos obra
             
            for vsf in pedreiros:
                if o.pedreiro==vsf:
                    vsf.setNumObras()
                    vsf.calculaSalario()
                
            print("    ")      
            print('Obra cadastrada com sucesso!')
            
            time.sleep(1)
            
        elif consultaObra == 4:
            print("    ")
            print('[--------------------------------Editar obra:--------------------------------]')
            
            if obras==[]:
                semObra()
            
            else:
                print("    ")
                cliente_pesquisa = input('Digite o nome do id da obra a ser editada: ')
                
                flag=False
                
                for i in obras:  # percorre a lista de obras
                    if int(cliente_pesquisa) == i.cod:  # busca pelo cliente da obra a ser alterado
                        print("    ")
                        while True:
                            
                            print("1) Editar cliente")
                            print("2) Editar materiais")
                            print("3) Editar mestre de obra")
                            print("4) Editar data de início")
                            print("5) Editar data de fim")
                            print("6) Voltar para o menu de obras")
                            print("    ")
                            editaObra=(input("Numero da ação a ser realizada: "))
                            editaObra=verConsul(editaObra)
                            editaObra=verificaNs(editaObra)
                            
                            if editaObra==1:
                                print("    ")
                                cliente = input('Novo cliente: ').title()
                                i.setCliente(cliente)
                                print("    ")
                                print('Cliente atualizado com sucesso!')
                                time.sleep(1)
                                
                            if editaObra==2:
                                print("    ")
                                print("Você deseja:")
                                print("1)Adicionar materiais")
                                print("2)Remover materiais")
                                print("    ")
                                Fazercoisa=input("O que você deseja fazer?: ")
                                Fazercoisa = verificaNs(Fazercoisa)
                                
                                while Fazercoisa!=1 and Fazercoisa!=2:
                                    
                                    Fazercoisa=input("Opção inválida! O que você deseja fazer?: ")
                                    Fazercoisa = verificaNs(Fazercoisa)
                                
                                if Fazercoisa==1:
                                    tururu=0
                                    
                                    for j in range(6):
                                        print("    ")
                                        print("O material", i.materiais[j]['nome'], "possui", i.materiais[j]['qtd'], "itens")
                                        add_num_mat=input("Quantos voce deseja adicionar? a medida é em {} com o valor de R${}: ".format(i.materiais[j]['medição'], i.materiais[j]['preço']))
                                        add_num_mat = verificaNs(add_num_mat)
                                        i.materiais[j]['qtd']+=add_num_mat
                                        tururu = (i.materiais[j]['qtd'] * i.materiais[j]['preço'])*1.22
                                        i.setTotal(tururu)
                                        
                                    print("    ")
                                    print('Materiais atualizados com sucesso!')
                                    time.sleep(1)
                                    
                                elif Fazercoisa==2:
                                    for j in range(6):
                                        print("    ")
                                        print("O material", i.materiais[j]['nome'], "possui", i.materiais[j]['qtd'], "itens")
                                        rem_num_mat=input("Quantos foram utilizados?: ")
                                        rem_num_mat = verificaNs(rem_num_mat)
                                        while rem_num_mat>i.materiais[j]['qtd']:
                                            rem_num_mat=input("Digite novamente quantos foram utilizados?: ")
                                            rem_num_mat = verificaNs(rem_num_mat)
                                        i.materiais[j]['qtd']-=rem_num_mat
                                    print("    ")
                                    print('Materiais atualizados com sucesso!')
                                    
                                    time.sleep(1)
                            
                            if editaObra==3:
                                
                                nomePedr = input('Digite o nome completo do novo mestre de obra: ').title()
                                contsocorro=0
                                for chama in pedreiros:
                                    if nomePedr==chama.nome:
                                        contsocorro+=1
                                        if contsocorro==1:
                                            i.pedreiro.setNumObrasBosta()
                                            i.pedreiro.calculaSalario()
                                            i.setPedreiro(chama)
                                            i.pedreiro.setNumObras()
                                            i.pedreiro.calculaSalario()
                                            print("    ")
                                            print('Mestre de obras atualizado com sucesso!')
                                            time.sleep(1)
                                            break
                                        elif contsocorro==0:
                                            print('O mestre de obras digitado não está cadastrado. Tente novamente: ')
                                        
                                
                            
                                    
                            if editaObra==4:
                                print("    ")
                                aux = str(input('Digite a nova data de início da obra no formado "DD/MM/AAAA": '))
                                
                                dataIn = verificaData(aux)
                                print("    ")
                                while dataIn==False:
                                    aux = str(input('Data inválida! Digite a data de início da obra no formato "DD/MM/AAAA": '))
                                    dataIn = verificaData(aux)
                                dataIn = datetime.strptime(aux, '%d/%m/%Y')     
                                kubs=0
                                months = (i.dataFim.year - i.dataIn.year) * 12 + (i.dataFim.month - i.dataIn.month)
                                kubs+=((months+1)*350*1.22)
                                i.setTotalRem(kubs)
                                i.setDataIn(dataIn)
                                casbran=0
                                months = (i.dataFim.year - i.dataIn.year) * 12 + (i.dataFim.month - i.dataIn.month)
                                casbran+=((months+1)*350*1.22)
                                i.setTotal(casbran)
                                print("    ")
                                print('Data de início atualizada com sucesso')
                                
                                time.sleep(1)
                                
                            if editaObra==5:
                                cont=0
                                while True:
                                    if cont==0:
                                        print("    ")
                                        aux = str(input('Digite a nova data de fim da obra no formato "DD/MM/AAAA": '))
                                        print("    ")
                                    else:
                                        aux = str(input('Data inválida! Digite a data de fim da obra no formato "DD/MM/AAAA": '))
                                    dataFim = verificaData(aux)
                                    while dataFim==False:
                                        aux = str(input('Data inválida! Digite a data de fim da obra no formato "DD/MM/AAAA": '))
                                        dataFim = verificaData(aux)
                                    dataFim = datetime.strptime(aux, '%d/%m/%Y')

                                    if i.dataIn<dataFim:
                                        break
                                    cont+=1
                                kubs=0
                                months = (o.dataFim.year - o.dataIn.year) * 12 + (o.dataFim.month - o.dataIn.month)
                                kubs+=((months+1)*350*1.22)
                                o.setTotalRem(kubs)
                                
                                i.setDataFim(dataFim)
                                
                                casbran=0
                                months = (i.dataFim.year - i.dataIn.year) * 12 + (i.dataFim.month - i.dataIn.month)
                                casbran+=((months+1)*350*1.22)
                                i.setTotal(casbran)
                                print("    ")
                                print('Data de fim atualizada com sucesso!')
                                
                                time.sleep(1)
                            
                            if editaObra==6:
                                break
                        
                        flag=True
                if flag == False:
                    
                    print("    ")
                    print("Cliente não encontrado!")
                    
                    time.sleep(1)
                    
        elif consultaObra == 5:
            #exclusão de obra
            if obras==[]:
                semObra()
            else:
                print("    ")
                print('[--------------------------------Excluir obra:--------------------------------]')
                print("    ")
                cliente_pesquisa = input('Digite o id da obra a ser excluída: ')
                
                flag=False
                for i in obras:  # percorre a lista de obras
                    if int(cliente_pesquisa) == i.cod: 
                        printarObrass(i)
                        flag=True
                        print("    ")
                        Del_Fun_F=input('Excluir esta obra? [S/N] ').title()
                        Del_Fun_F = verificaSN(Del_Fun_F)
                        if Del_Fun_F=='S':
                           
                            for vsf in pedreiros:
                                if i.pedreiro==vsf:
                                    vsf.setNumObrasBosta()
                                    vsf.calculaSalario()
                            obras.remove(i)
                            print("    ")
                            print('Obra deletada com sucesso')
                                
                            time.sleep(1)
                            
                if flag==False:
                    print("    ")
                    print('Obra não cadastrada')
                    
                    time.sleep(1)
                    
                
        elif consultaObra == 6:
            break
        
        
def opcoesFuncionarios():
    print("    ")
    while True:
        print("    ")
        print("[--------------------------------Menu de Funcionários--------------------------------]")
        print("    ")
        print("1) Exibir todos os funcionários cadastrados")
        print("2) Pesquisar funcionário")
        print("3) Cadastrar funcionário")
        print("4) Editar funcionário")
        print("5) Excluir funcionário")
        print("6) Voltar para o menu principal")
        print("    ")
            
        consultaFunc=input("Numero da ação a ser realizada: ")
        consultaFunc=verConsul(consultaFunc)
        consultaFunc = verificaNs(consultaFunc)
        
        if consultaFunc==1:
            #exibir todos os funcionários da empresa
            if funcionarios==[]:
                semFuncionario()
            
            else:
                print("    ")
                print("[--------------------------------Funcionários cadastrados:--------------------------------]")
                for i in funcionarios:
                    print("    ")
                    print ('Cargo:', i.__class__.__name__)
                    print ('Cadastro:', i.cadastro)
                    print ('Nome:', i.nome)
                    print ('Salario: R${}'.format(i.salario))
                    print ('CPF: {}.{}.{}-{}'.format(i.cpf[0:3], i.cpf[3:6], i.cpf[6:9], i.cpf[9:11]))
                    print ('Contato: (0{}){}-{}'.format(i.fone[0:2], i.fone[2:7], i.fone[7:12]))

                    if i.__class__.__name__=='Gestor':
                        print ('Data contratação:', i.anoContrat)
                    if i.__class__.__name__=='Pedreiro':
                        print ('Presente em {} obras'.format(i.numObras))
                    time.sleep(0.25)
                time.sleep(2)
                        
        if consultaFunc==2:
            #pesquisa de funcionário específico
            if funcionarios==[]:
                semFuncionario()
                
            else:
                print("    ")
                print("[--------------------------------Pesquisar funcionário:--------------------------------]")
                Pes_Fun=input('Nome do funcionario a ser pesquisado: ').title()
                flag=False
                for i in funcionarios:
                    if i.nome==Pes_Fun:
                        flag=True
                        print ("   ")
                        print ('Cargo:', i.__class__.__name__)
                        print ('Cadastro:', i.cadastro)
                        print ('Nome:', i.nome)
                        print ('Salario: R${}'.format(i.salario))
                        print ('CPF: {}.{}.{}-{}'.format(i.cpf[0:3], i.cpf[3:6], i.cpf[6:9], i.cpf[9:11]))
                        print ('Contato: (0{}){}-{}'.format(i.fone[0:2], i.fone[2:7], i.fone[7:12]))
                        
                        if i.__class__.__name__=='Gestor':
                            print ('Data contrataçao:', i.anoContrat)
                        if i.__class__.__name__=='Pedreiro':
                            print ('Presente em {} obras'.format(i.numObras))
                        time.sleep(2)
                            
                if flag==False:
                    print("    ")
                    print('Funcionário não cadastrado')
                    
                    time.sleep(1)
                        
        if consultaFunc==3:
            #cadastro de novo funcionário
            print("    ")
            print("[--------------------------------Cadastrar funcionário:--------------------------------]")
            print("    ")

            Faz_Cad=input('O que deseja cadastrar? ["Gestor/Pedreiro"]: ').title()
            print("    ")
            while Faz_Cad!='Gestor' and Faz_Cad!='Pedreiro':
                Faz_Cad=input('Valor inválido! O que deseja cadastrar? ["Gestor/Pedreiro"]: ').title()
            
            Fun_Nome=input('Nome do Funcionario: ').title()
            Fun_CPF=input('CPF do funcionario[sem"." e "-"]: ')
            Fun_CPF=verificaNumeros(11, Fun_CPF)
            
            for x in funcionarios:
                while Fun_CPF==x.cpf:
                    Fun_CPF=input('Esse CPF já está cadastrado! Digite o CPF do funcionario[sem"." e "-"]: ')
                    Fun_CPF=verificaNumeros(11, Fun_CPF)
            Fun_Fone=input('Telefone do Funcionario[DDD e número juntos]: ')
            Fun_Fone=verificaNumeros(11, Fun_Fone)
            Fun_Cadastro=(random.randint(10000,100000))
            
            for x in funcionarios:
                while Fun_Cadastro==x.cadastro:
                    Fun_Cadastro=(random.randint(10000,100000))
            Fun_Salario = 1500
            
            if Faz_Cad=='Gestor':
                print("    ")
                anoContrat = input('Digite o ano da contratação[AAAA]: ')
                anoContrat=verificaAno(anoContrat)
                    
                Gestor(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario, anoContrat)
                for i in gestores:
                    if i==gestores[-1]:
                        print("    ")
                        salarioTot = i.calculaSalario(Fun_Salario, anoContrat)
                        i.setSalario(salarioTot)
                        
                        print('Gestor cadastrado com sucesso!')
                        time.sleep(1)
                
            elif Faz_Cad=='Pedreiro':
                print("    ")
                numObras = 0
                Pedreiro(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario, numObras)
                
                print('Pedreiro cadastrado com sucesso!')
                time.sleep(1)
                
        if consultaFunc==4:
            #edição de funcionário
            if funcionarios==[]:
                semFuncionario()
            
            else:
                flag=False
                print("    ")
                print("[--------------------------------Editar funcionário:--------------------------------]")
                print("    ")
                editFunc = input('Digite o nome completo do funcionário a ser editado: ').title()
                
                for i in funcionarios:
                    if i.nome == editFunc:
                        flag=True
                        if i.__class__.__name__=='Gestor':
                            while True:
                                print("    ")
                                print("1) Editar nome")
                                print("2) Editar CPF")
                                print("3) Editar telefone")
                                print("4) Editar ano de contratação")
                                print("5) Voltar para o menu de funcionários")
                                print("    ")
                                editaFunc2=input("Numero da ação a ser realizada: ")
                                print("    ")
                                editaFunc2=verificaNs(editaFunc2)   
                                while not editaFunc2 in [1,2, 3, 4, 5]:
                                    editaFunc2=int(input("Valor inválido! Numero da ação a ser realizada: "))
                            
                                if editaFunc2==1:
                                    print("    ")
                                    nome = input('Digite o novo nome do funcionário: ').title()
                                    i.setNome(nome)
                                    print("    ")
                                    print('Nome atualizado com sucesso!')
                                    time.sleep(1)
                                    
                                if editaFunc2==2:
                                    print("    ")
                                    cpf = input('Digite o novo cpf do funcionário: ')
                                    cpf=verificaNumeros(11, cpf)
                                    for x in funcionarios:
                                        print("    ")
                                        while cpf==x.cpf:
                                            cpf=input('Esse CPF já está cadastrado! Digite o CPF do funcionario[sem"." e "-"]: ')
                                            cpf=verificaNumeros(11, cpf)
                                            
                                    i.setCPF(cpf)
                                    print("    ")
                                    print('CPF atualizado com sucesso!')
                                    time.sleep(1)
                                    
                                if editaFunc2==3:
                                    print("    ")
                                    fone = input('Digite o novo telefone do funcionário: ')
                                    fone=verificaNumeros(11, fone)
                                    i.setFone(fone)
                                    print("    ")
                                    print('Telefone atualizado com sucesso!')
                                    time.sleep(1)
                                
                                if editaFunc2==4:
                                    print("    ")
                                    anoContrat = (input('Digite o novo ano de contratação do funcionário: '))
                                    anoContrat=verificaAno(anoContrat)
                                    i.setContra(anoContrat)
                                    for j in gestores:
                                        if i.nome==j.nome:
                                            salarioTot = j.calculaSalario(1500, anoContrat)
                                            j.setSalario(salarioTot)
                                            print("    ")
                                            print('Ano de contratação atualizado com sucesso!')
                                            time.sleep(1)
                                    
                                if editaFunc2==5:
                                    break
                                    
                        else:
                            while True:
                                print("    ")
                                print("1) Editar nome")
                                print("2) Editar CPF")
                                print("3) Editar telefone")
                                print("4) Voltar para o menu de funcionários")
                               
                                print("    ")
                                editaFunc2=(input("Numero da ação a ser realizada: "))
                                editaFunc2=verificaNs(editaFunc2)
                                print("    ")
                                
                                while not editaFunc2 in [1,2, 3, 4]:
                                    editaFunc2=(input("Valor inválido! Numero da ação a ser realizada: "))
                                    
                                    editaFunc2=verificaNs(editaFunc2)
                                if editaFunc2==1:
                                    print("    ")
                                    nome = input('Digite o novo nome do funcionário: ').title()
                                    i.setNome(nome)
                                    print("    ")
                                    print('Nome atualizado com sucesso!')
                                    time.sleep(1)
                                    
                                if editaFunc2==2:
                                    
                                    print("    ")
                                    cpf = input('Digite o novo cpf do funcionário: ')
                                    cpf=verificaNumeros(11, cpf)
                                    
                                    for x in funcionarios:
                                        while cpf==x.cpf:
                                            cpf=input('Esse CPF já está cadastrado! Digite o CPF do funcionario[sem"." e "-"]: ')
                                            
                                            cpf=verificaNumeros(11, cpf)
                                    i.setCPF(cpf)
                                    print("    ")
                                    print('CPF atualizado com sucesso!')
                                    time.sleep(1)
                                    
                                if editaFunc2==3:
                                    print("    ")
                                    fone = input('Digite o novo telefone do funcionário: ')
                                    fone=verificaNumeros(11, fone)
                                    i.setFone(fone)
                                    print("    ")
                                    print('Telefone atualizado com sucesso!')
                                    time.sleep(1)
                                
                                if editaFunc2==4:
                                    break
                                
                if flag==False:
                    print("    ")
                    print('Funcionário não cadastrado')
                    time.sleep(1)
                                    
        if consultaFunc==5:
            #exclusão de funcionário
            if funcionarios==[]:
                semFuncionario()
                
            else:
                
                print("    ")
                print("[--------------------------------Excluir funcionário:--------------------------------]")
                print("    ")
                flag=False
                Del_Fun=input('Digite o nome completo do funcionario a ser excluido: ').title()
                
                for i in funcionarios:
                    if i.nome==Del_Fun:
                        print ("   ")
                        print ('Cargo:', i.__class__.__name__)
                        print ('Cadastro:', i.cadastro)
                        print ('Nome:', i.nome)
                        print ('Salario: R${}'.format(i.salario))
                        print ('CPF: {}.{}.{}-{}'.format(i.cpf[0:3], i.cpf[3:6], i.cpf[6:9], i.cpf[9:11]))
                        print ('Contato: (0{}){}-{}'.format(i.fone[0:2], i.fone[2:7], i.fone[7:12]))
                        
                        if i.__class__.__name__=='Gestor':
                            print ('Data contratação: ', i.anoContrat)
                            
                        if i.__class__.__name__=='Pedreiro':
                            print ('Presente em {} obras'.format(i.numObras))
                            
                        flag=True
                        print("    ")
                        Del_Fun_F=input('Excluir este funcionario? [S/N] ').title()
                        Del_Fun_F = verificaSN(Del_Fun_F)
                        
                        if Del_Fun_F=='S':
                            if len(obras)!=0:
                                for vsf in obras:
                                    if vsf.pedreiro==i:
                                        print("    ")
                                        print("O Funcionario é Mestre de obras e está cadastrado em uma obra, altere o Mestre de obras de tal obra para poder exclui-lo")
                                        time.sleep(1)
                                        break
                                    
                                    else:
                                        funcionarios.remove(i)
                                        print("    ")
                                        print('Funcionário deletado com sucesso')
                                        time.sleep(1)
                            else:
                                funcionarios.remove(i)
                                print("    ")
                                print('Funcionário deletado com sucesso')
                                time.sleep(1)
                                                           
                if flag==False:
                    print("    ")
                    print('Funcionário não cadastrado')
                    time.sleep(1)
                                       
        if consultaFunc==6:
            break
        
def faturamento():
    print("    ")
    print("[--------------------------------Faturamento atual:--------------------------------]")
    dindin=0
    print("    ")
    if len(obras)==0:
        print("Nenhuma obra cadastrada, faturamento nulo.")
        time.sleep(2)
    else:
        
        for grana in obras:
            dindin+=grana.total
            casbran=0
            months = (grana.dataFim.year - grana.dataIn.year) * 12 + (grana.dataFim.month - grana.dataIn.month)
            casbran+=((months+1)*350)
            
            dindin-=casbran
            print("    ")
            print('O faturamento da empresa, caso todas obras sejam acabadas em seus prazos e sem alterações, não contando com o desconto do salários dos funcionários, porém considerando o adicional por obra do pedreiro, será de R${:.2f}'.format(dindin))
            time.sleep(2)
   
#main
Pedreiro('Igor', '00000005252', '48999934599', 16745, 1500, 0)
Pedreiro('Iago', '00000000000', '48999999999', 12345, 1500,0)
Gestor('Marina Benvenuti', '11111111111', '48908888888', 23412, 1500, 2023)

while True:
    print ("  ")
    print("[--------------------Sistema Gerenciador de Obras--------------------]")
    print("[-----------------------------------Menu-----------------------------------]")
    print("    ")
    print("1) Obras")
    print("2) Funcionários")
    print("3) Faturamento da empresa")
    print("4) Encerrar programa")
    print("    ")
        
    consulta=(input("Numero da ação a ser realizada: "))
    
    consulta=consultaMain(consulta)
    consulta=verificaNs(consulta)
    
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
        print("Programa encerrado com sucesso! ")
        break
