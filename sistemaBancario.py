#Desafio Sistema Bancário

# Menu de opções para o cliente

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

# Variável que define o limite do número de saques e limite total de saque
LIMITE_SAQUE = 500 
LIMITE_SAQUES_DIARIOS = 3 

#Variável para armazenar o saldo 

saldo = 200.00

#Variável para guardar o histórico de transações
extrato = ""
#Variável que salva o número de saques realizados no dia
numero_saques = 0

#Mensagem de boas vindas para o usuário
print(f'Bem vindo, seu saldo é de R$ {saldo:.2f}. Selecione uma operação:')

while True:
    #Imprime o menu e recebe a opção selecionada pelo cliente
    opcao = input(menu)
    
    #Verifica a opção escolhida e executa a ação
    
    #Depósito
    if opcao == 'd':
        print('Deposito')
        valor = float(input('Informe o valor do depósito: \n'))
        
        if valor <= 0:
            print('Valor invalido. Cancelando operação.')
        else:
            saldo += valor
            print(f'Foram depositados R$ {valor:.2f} na sua conta.')
            extrato += f'Depósito: R$ {valor:.2f}\n'
    #Saque
    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES_DIARIOS:
            print('Operação falhou. Você excedeu o limite de saques diários.')
        
        else:
            
            print('Saque')
            valor = float(input('Informe o valor do saque: \n'))
            
            if valor > LIMITE_SAQUE:
                print('Operação falhou. O valor excede o limite.')
            elif valor <= 0:
                print('Operação falhou. Valor informado inválido')
    
            else:
                if valor > saldo:
                    print('Operação falhou. Saldo insuficiente')
                elif valor >0:
                    saldo -= valor
                    extrato += f'Saque: R$ {valor:.2f}\n'
                    numero_saques += 1
                    print('Saque realizado com sucesso.')
    #Extrato               
    elif opcao == 'e':
        print('Extrato')
        print('\n========== EXTRATO ==========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
    
    #Sair    
    elif opcao == 'q':
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")