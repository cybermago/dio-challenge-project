# CHALLENGE PROJECT
import textwrap
from tkinter import EXCEPTION

from mesonbuild.compilers.cpp import non_msvc_eh_options
from psutil import users


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

def withdraw(*,balance, value, extrato, limit, withdraw_count, withdraw_limit):
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

withdraw(balance=0, value=0, extrato='', limit=0, withdraw_count=5, withdraw_limit=1300)

def exibir_extrato(balance, /, *, extrato):
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

exibir_extrato(0, extrato=None)

contas = {
        'agencia': '0001',
        'number': None,
        'user': None
    }
def create_user(users):
    """
    Cadastra um novo usuário.

    Args:
        users (list): Lista de usuários cadastrados.

    Returns:
        dict: O novo usuário cadastrado ou None se o CPF já existe.
    """
    cpf = input("Informe o CPF (somente números): ")
    if any(user['cpf'] == cpf for user in users):
        print("\nCPF já cadastrado! Não é possível criar um novo usuário com este CPF.")
        return None

    name = input("Informe o nome completo: ")
    dob = input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input("Informe o endereço (logradouro, nº - bairro - cidade/estado): ")

    new_user = {"name": name, "dob": dob, "cpf": cpf, "address": address}
    users.append(new_user)
    print("\nUsuário cadastrado com sucesso!")
    return new_user

def create_account(agency, account_number, users, accounts):
    """
    Cria uma nova conta corrente para um usuário existente.

    Args:
        agency (str): Número da agência.
        account_number (int): Próximo número de conta disponível.
        users (list): Lista de usuários cadastrados.
        accounts (list): Lista de contas cadastradas.

    Returns:
        dict: A nova conta criada ou None se o usuário não for encontrado.
    """
    cpf = input("Informe o CPF do usuário para associar à conta: ")
    user_found = next((user for user in users if user['cpf'] == cpf), None)

    if user_found:
        new_account = {"agency": agency, "number": account_number, "user": user_found}
        accounts.append(new_account)
        print("\nConta criada com sucesso!")
        return new_account
    else:
        print("\nUsuário não encontrado! Não é possível criar a conta.")
        return None

def list_accounts(accounts):
    """
    Lista todas as contas cadastradas.
    """
    if not accounts:
        print("\nNão há contas cadastradas.")
        return

    print("\n" + "=" * 30)
    print("        CONTAS CADASTRADAS")
    print("=" * 30)
    for account in accounts:
        line = f"""\
            Agência:\t{account['agency']}
            C/C:\t\t{account['number']}
            Titular:\t{account['user']['name']}
        """
        print(textwrap.dedent(line))
        print("-" * 30)

def list_users(users):
    """
    Lista todos os usuários cadastrados.
    """
    if not users:
        print("\nNão há usuários cadastrados.")
        return

    print("\n" + "=" * 30)
    print("         USUÁRIOS CADASTRADOS")
    print("=" * 30)
    for user in users:
        line = f"""\
            Nome:\t\t{user['name']}
            CPF:\t\t{user['cpf']}
            Nascimento:\t{user['dob']}
            Endereço:\t{user['address']}
        """
        print(textwrap.dedent(line))
        print("-" * 30)

def main():
    """
    Função principal que gerencia o fluxo do sistema bancário.
    """
    LIMIT = 500
    WITHDRAW_LIMIT = 3
    AGENCY = "0001"

    users = []
    accounts = []
    next_account_number = 1

    # Main menu for client operations
    def client_menu(balance, extrato, withdraw_count):
        menu_options = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        => """

        while True:
            option = input(textwrap.dedent(menu_options)).lower().strip()

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
                exibir_extrato(balance, extrato=extrato)
            elif option == 'q':
                print("Obrigado por usar nosso caixa eletrônico!")
                return balance, extrato, withdraw_count  # Return updated values
            else:
                EXCEPTION

    role_options = """
    [a] ADMIN
    [c] CLIENTE
    [q] SAIR
    => """

    while True:
        role_option = input(textwrap.dedent(role_options)).lower().strip()

        if role_option == 'a':
            admin_options = """
            [nu] Novo Usuário
            [nc] Nova Conta
            [lu] Listar Usuários
            [lc] Listar Contas
            [s] Sair
            =>"""
            while True:
                admin_option = input(textwrap.dedent(admin_options)).lower().strip()

                if admin_option == 'nu':
                    create_user(users)
                elif admin_option == 'nc':
                    new_account = create_account(AGENCY, next_account_number, users, accounts)
                    if new_account:
                        next_account_number += 1
                elif admin_option == 'lu':
                    list_users(users)
                elif admin_option == 'lc':
                    list_accounts(accounts)
                elif admin_option == 's':
                    print("\nSaindo do modo ADMIN.")
                    break
                else:
                    EXCEPTION

        elif role_option == 'c':
            account_options = """
            [e] Entrar
            [q] Sair
            =>"""

            while True:
                account_option = input(textwrap.dedent(account_options)).lower().strip()

                if account_option == 'e':
                    cpf_login = input("Informe o CPF para entrar na conta: ")
                    account_found = None
                    for acc in accounts:
                        if acc['user']['cpf'] == cpf_login:
                            account_found = acc
                            break

                    if account_found:
                        print(f"\nBem-vindo(a), {account_found['user']['name']}!")
                        # Initialize balance, extrato, and withdraw_count for the session
                        # In a real system, these would be loaded from a database for the specific account
                        balance = 0
                        extrato = []
                        withdraw_count = 0
                        # Pass these to the client menu and update them after the session
                        balance, extrato, withdraw_count = client_menu(balance, extrato, withdraw_count)
                    else:
                        EXCEPTION
                elif account_option == 'q':
                    print("\nSaindo do modo CLIENTE.")
                    break
                else:
                    EXCEPTION

        elif role_option == 'q':
            print("\nEncerrando o sistema bancário. Até mais!")
            break
        else:
            EXCEPTION


# Executa a função principal
if __name__ == "__main__":
    main()
