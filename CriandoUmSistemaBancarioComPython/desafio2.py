import textwrap

def menu():
    menu = """\n
    ============= MENU =============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))

# positional only
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

# keyword only
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"\nOperação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso! \tSaldo atual: R$ {saldo:.2f}\n")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

# positional only e keyword only
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("\nNão foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo:\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nJá existe um usuário com esse CPF!")
        return 
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-yyyy): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print(f"\nUsuário {nome} cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print("\nUsuário não encontrado! É necessário cadastrar um usuário antes de criar uma conta.")
        return None
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    print(f"\nConta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}")
    return conta

def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    for conta in contas:
        linha = f"""\
        Agência: {conta['agencia']}
        Conta: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        CPF: {conta['usuario']['cpf']}
        """
        print("\n" + "=" * 40)
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
            if saldo == 0 or numero_saques >= LIMITE_SAQUES:
                print("\nOperação falhou! Saque está inativo devido ao saldo zero ou limite de saques atingido.")
                continue

            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                ) 
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Encerrando o sistema. Obrigado por usar nosso banco!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
