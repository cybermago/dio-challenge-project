# CHALLENGE PROJECT
def deposit(balance, value, extrato):
    """
    Realiza um depósito na conta.

    Args:
        balance (float): Saldo atual da conta.
        value (float): Valor a ser depositado.
        extrato (list): Lista de transações (extrato).

    """
    if value > 0:
        balance += value
        extrato.append(f"Depósito: R$ {value:.2f}")
        print(f"Depósito de R$ {value:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor do depósito deve ser positivo.")
    return balance, extrato

def withdraw(balance, value, extrato, limit, withdraw_count, withdraw_limit):
    """
    Realiza um saque da conta.

    Args:
        balance (float): Saldo atual da conta.
        value (float): Valor a ser sacado.
        extrato (list): Lista de transações (extrato).
        limit (float): Limite máximo por saque.
        withdraw_count (int): Contador de saques realizados.
        withdraw_limit (int): Limite máximo de saques diários.

    Returns:
        tuple: Novo saldo, extrato atualizado e contador de saques.
    """

    if value > balance:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif value > limit:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limit:.2f}.")
    elif withdraw_count >= withdraw_limit:
        print("Operação falhou! Número máximo de saques diários excedido.")
    elif value <= 0:
        print("Operação falhou! O valor do saque deve ser positivo.")
    else:
        balance -= value
        extrato.append(f"Saque: R$ {value:.2f}")
        withdraw_count += 1
        print(f"Saque de R$ {value:.2f} realizado com sucesso!")

    return balance, extrato, withdraw_count

def exibir_extrato(balance, extrato):
    """
    Exibe o extrato da conta.

    Args:
        balance (float): Saldo atual da conta.
        extrato (list): Lista de transações (extrato).
    """
    print("\n" + "=" * 30)
    print("           EXTRATO")
    print("=" * 30)

    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transaction in extrato:
            print(transaction)

    print(f"\nSaldo: R$ {balance:.2f}")
    print("=" * 30)

def main():
    """
    Função principal que gerencia o fluxo do caixa eletrônico.
    """
    menu_options = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    balance = 0
    LIMIT = 500
    extrato = []
    withdraw_count = 0
    WITHDRAW_LIMIT = 3

    while True:
        option = input(menu_options).lower().strip()

        if option == 'd':
            value = float(input('Informe o valor do depósito: R$ '))
            balance, extrato = deposit(balance, value, extrato)
        elif option == 's':
            value = float(input('Informe o valor do saque: R$ '))
            balance, extrato, withdraw_count = withdraw(
                balance=balance,
                value=value,
                extrato=extrato,
                limit=LIMIT,
                withdraw_count=withdraw_count,
                withdraw_limit=WITHDRAW_LIMIT
            )
        elif option == 'e':
            exibir_extrato(balance, extrato)
        elif option == 'q':
            print("Obrigado por usar nosso caixa eletrônico!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")

# Executa a função principal
if __name__ == "__main__":
    main()
