#saque, deposito e visualização de extrato
# somente valor positivo 1 usuario deve exibir no extrato tdoos os dados
#3 saques diários de $500 exibir a mensagem quando não tiver saldo
# listar depositos e saques

menu = '''

Banco Start

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
'''

saldo = 0
limite = 500
extrato = ' '
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
            
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação cancelada! Valor informado é inválido!")    
                
    elif opcao == "s":        
        valor = float(input("Informe o valor do saque: "))
        
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente!")
            
        elif valor > limite:
            print("Operação falhou! Excedeu o valor do limite!")
            
        elif numero_saque >= LIMITE_SAQUES:
            print("Operação falhou! Excedeu limite de saques!")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            
        else:
            print("Operação falhou! O valor informado é inválido!")
                
    elif opcao == "e":
        print("\n *******Extrato********")
        if not extrato:
            print("Nenhum movimento efetuado até agora.")
        else:
            print(extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("*************************")
        
    elif opcao == "q":
        break
    
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")
