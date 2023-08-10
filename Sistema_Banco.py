menu = """

[1] Saldo
[2] Depósito
[3] Saque
[4] Extrato
[5] Sair

==> Selecione uma opção:"""

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
QTDE_SAQUES = 3

while True:
    opcao = input(menu)

    #SALDO
    if opcao == "1":
        print("--- SALDO ---")
        print(f"Sado atual: R${saldo: .2f}")

    #DEPÓSITO   
    elif opcao == "2":
        print("--- DEPÓSITO ---")
        valor_deposito = float(input("Digite o valor para depósito: R$ "))
        if valor_deposito >0:
            saldo += valor_deposito
            extrato += f"Depósito:                      +R${valor_deposito: .2f}\n"
            print("Valor depositado com sucesso!")
        else:
            print("Não é possível realizar o depósito do valor infomado.")

    #SAQUE
    elif opcao == "3":
        print("--- SAQUE ---")

        valor_saque = float(input("Digite o valor para saque: R$ "))

        if valor_saque > saldo:
            print("Falha ao realizar o saque! Saldo insuficisente.")
        
        elif valor_saque < 0:
            print("Falha ao realizar o saque! Não é possível sacar o valor informado.")

        elif valor_saque > limite_saque:
            print(f"Falha ao realizar o saque! O valor limite para saque é de R$ {limite_saque}.")

        elif numero_saques >= QTDE_SAQUES:
            print(f"Falha ao realizar o saque! A quantidade de {QTDE_SAQUES} saques diários foi atingida.")
        
        else:
            numero_saques += 1
            saldo -= valor_saque
            extrato += f"Saque:                         -R${valor_saque: .2f}\n"
            print(f"Saque de R${valor_saque: .2f} realizado com sucesso, retire o valor no local indicado.")

    #EXTRATO   
    elif opcao == "4":
            
        print("\n--------------------- EXTRATO -------------------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual:                    R$ {saldo:.2f}")
        print("-------------------------------------------------------")
        
    #SAIR
    elif opcao == "5":
        print("Obrigado por nos escolher como seu banco!")
        break
    

    else:
        print("Opção inválida, selecione novamente.")    



    
    
               