def get_menu(saldo, numero_saques, limite_saques):
    sacar_text = "[s] Sacar"
    if saldo == 0 or numero_saques >= limite_saques:
        sacar_text = "[s] Sacar (Inativo)"
    return f"""

[d] Depositar
{sacar_text}
[e] Extrato
[q] Sair

=> """

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, limite_saques):
    if saldo == 0 or numero_saques >= limite_saques:
        print("Operação falhou! Saque está inativo devido ao saldo zero ou limite de saques atingido.")
        return saldo, extrato, numero_saques

    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {saldo:.2f}\n")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def imprimir_extrato(extrato, saldo):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(get_menu(saldo, numero_saques, LIMITE_SAQUES))

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
        elif opcao == "e":
            imprimir_extrato(extrato, saldo)
        elif opcao == "q":
            print("Encerrando o sistema. Obrigado por usar nosso banco!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
