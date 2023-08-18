

#Função Menu
def menu():
    menu = """\n
    --------- MENU ---------

    [1] Saldo
    [2] Depósito
    [3] Saque
    [4] Extrato
    [5] Novo Usuário
    [6] Nova Conta
    [7] Listar Usuários
    [8] Sair

    ==> Selecione uma opção:"""
    return input(menu)

#Função Saldo
def mostrar_saldo(saldo):
    print("--- SALDO ---")
    print(f"Sado atual: R${saldo: .2f}")
    return  saldo

#Função Depósito
def depositar(saldo, valor_deposito, extrato, /):
        
        if valor_deposito >0:
            saldo += valor_deposito
            extrato += f"Depósito:                      +R${valor_deposito: .2f}\n"
            print("Valor depositado com sucesso!")
        else:
            print("Não é possível realizar o depósito do valor infomado.")

        return saldo, extrato

#Função Saque
def sacar(*,saldo, valor_saque, extrato, valor_limite_saque, numero_saques, qtde_saques_max):
    print("--- SAQUE ---")

    excedeu_saldo = valor_saque > saldo
    excedeu_valor_limite = valor_saque > valor_limite_saque 
    excedeu_qtde_saque = numero_saques >= qtde_saques_max

    if excedeu_saldo:
            print("Falha ao realizar o saque! Saldo insuficisente.")
        
    elif excedeu_valor_limite:
            print("Falha ao realizar o saque! O valor solicitado excedeu o limite permitido.")

    elif excedeu_qtde_saque:
            print(f"Falha ao realizar o saque! A quantidade de saques diários foi atingida.")
        
    else:
            numero_saques += 1
            print(f'Saques realizados hoje {numero_saques}')
            saldo -= valor_saque
            extrato += f"Saque:                         -R${valor_saque: .2f}\n"
            print(f"Saque de R${valor_saque: .2f} realizado com sucesso, retire o valor no local indicado.")

    return saldo, extrato, numero_saques

#Função Extrato
def mostrar_extrato(saldo, /,*,extrato):

      print("\n--------------------- EXTRATO -------------------------")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo atual:                    R$ {saldo:.2f}")
      print("-------------------------------------------------------")

#Função Filtrar Usuário
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf']==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#Função Cadastrar Cliente
def cadastrar_cliente(usuarios):
     cpf = input("Informe o CPF (Somente números): ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("Já existe usuário com esse CPF!")
          return
     
     nome = input("Informe o nome completo: ")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereço (Logradouro, Nro - Bairro - Cidade/Estado): ")

     usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

     print("Usuário cadastrado com sucesso!")

#Função Cadastrar Conta
def cadastrar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF do usuário: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("Conta criada com sucesso!")
          return{"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
     
     print("Usuário não encontrado, fluxo de criação de conta encerrado!")

#Função Listar Contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/c:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

#Função Sair
def sair():
      print("Obrigado por nos escolher como seu banco!")  




#Programa
def main():

    #constantes
    QTDE_SAQUES_MAX = 3
    AGENCIA = "0001"

    #variáveis
    saldo = 0
    valor_limite_saque = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        #SALDO
        if opcao == "1":
            mostrar_saldo(saldo)

        #DEPÓSITO   
        elif opcao == "2":
            print("--- DEPÓSITO ---")
            valor_deposito = float(input("Digite o valor para depósito: R$ "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        #SAQUE
        elif opcao == "3":
            print("--- SAQUE ---")
            valor_saque = float(input("Digite o valor para saque: R$ "))
            
              

            saldo, extrato, numero_saques = sacar(
                saldo =  saldo, 
                valor_saque = valor_saque, 
                extrato = extrato, 
                valor_limite_saque = valor_limite_saque, 
                numero_saques = numero_saques, 
                qtde_saques_max = QTDE_SAQUES_MAX
            )

        #EXTRATO   
        elif opcao == "4":
            mostrar_extrato(saldo, extrato=extrato)  
        
        #CADASTRAR CLIENTE   
        elif opcao == "5":
            cadastrar_cliente(usuarios)

        #CADASTRAR CONTA  
        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                 contas.append(conta)


        #CADASTRAR CONTA  
        elif opcao == "7":
            listar_contas(contas)  


        #SAIR
        elif opcao == "8":
            sair()
            break

        else:
            print("Opção inválida, selecione novamente.")    

main()


    
    
               