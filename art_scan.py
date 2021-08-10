import socket

ports  = [21,23,135,137,139,80,443,445,8080]

print('digite: arc IP A/P (A:todas portas / P: portas principais)')
print('Ex: arc google.com P \n')
print('****** ART SCAN ******* \n')

entrada = input()
name = entrada.split(' ')[0]
ip = entrada.split(' ')[1]
op = entrada.split(' ')[2]
if (name == 'arc'):
    if op == 'A':
        print("PORTA   STATUS   SERVICE  (1-65535)")
        cont = 0
        for port in range(1,65535):
            cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cli.settimeout(0.1)
            codi = cli.connect_ex((ip, port))
            if codi == 0:
                name = socket.getservbyport(port)
                status = 'Aberta'
                cont = cont + 1
                print(port,' ',status,' ',str(name))
            '''
            else:
                status = 'Fechada'
            '''
            
        print ("busca comcluida  ",cont ,"portas abertas")

    elif op == 'P':
        print("PORTA   STATUS   SERVICE")
        cont = 0
        for port in ports:
            cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cli.settimeout(0.2)
            codi = cli.connect_ex((ip, port))
            if codi == 0:
                name = socket.getservbyport(port)
                status = 'Aberta'
                cont = cont + 1
                print(port,' ',status,' ',str(name))
            
            '''
            else:
                status = 'Fechada'
            '''
        print ("busca comcluida  ",cont ,"portas abertas")
    else:
        print('complemento invalido')
else:
    print('Erro - Servico nao indentificado \n')