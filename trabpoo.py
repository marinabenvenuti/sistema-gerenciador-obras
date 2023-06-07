#Iago Rodrigues Munoz
#23104313

#funçoes

def menu(x):
    print ("  ")
    print("[--------------------Menu--------------------]")
    print("  ")
    print("1) Ver obras cadastrdas")
    print("2) Encerrar o programa")
    print("  ")
    
    consulta=input("Numero da açao a ser realizada: ")
    ver_consul=verconsul(consulta)
    
    if ver_consul=="1":
        ver1(ver_consul)
        
    elif ver_consul=="2":
        print("Programa encerrado")
        break
    
def verconsul(x):
    while not x in ["1","2"]:
        x=input("Digite novamente: ")
    return x

def ver1(p):
    for i in range (len(cads)):
        print("popo")
    
    escolha_menu=input("Numero da açao a ser realizada: ")
    ver_esc_menu=verescmenu(escolha_menu)
        
def ver2(p):

def verescmenu(x):
    while not x in ["1","2"]:
        x=input("Digite novamente: ")
    return x




                
#corpo
bobi=0
cads=list()

    
menu(iago)
