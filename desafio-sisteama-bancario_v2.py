#adicionado funções
import textwrap


def menu():
    menu = """\n
    __________ MENU _______
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    ________________________
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
       if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
       else:
            print("Valor inválido!")
       return saldo, extrato     
            
def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido!")
        
        return saldo, extrato  
    
def exibir_extrato(saldo, /, *, extrato):
     print("\n================ EXTRATO ================")
     print("Não foram realizadas movimentações." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("==========================================")
 
def criar_usuario(usuarios):    
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print(f"Já existe usuário com esse CPF: {cpf}")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço completo: ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco":endereco})
    
    print("Usuário criado com sucesso")
    
def filtrar_usuario(cpf, usuarios):    
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
       print("Conta criada com sucesso!!") 
       return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
   
    print("Usuario não encontrado, fluxo de criação de conta encerrado!!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titual: {conta['usuario']['nome']}
        
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    

def main():    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
           
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))           
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao == "nu":
            criar_usuario(usuarios)        
         
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "e":
           exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("Operação finalizada.")
            break

        else:
            print("Opção inválida, por favor selecione novamente.")
            
            
main()
