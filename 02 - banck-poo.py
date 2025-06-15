# CHALLENGE PROJECT
import textwrap

# Definindo as classes conforme o diagrama UML

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = [] # Lista de objetos Conta
        self.realiza_transacao = None # Será uma instância de Transacao

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")
        elif valor <= 0:
            print("\nOperação falhou! O valor informado é inválido.")
        else:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!")
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso!")
            return True
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Transacao:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        super().__init__(valor)

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(
                {"tipo": "Saque", "valor": self.valor}
            )
            return True
        return False

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__(valor)

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(
                {"tipo": "Depósito", "valor": self.valor}
            )
            return True
        return False

# Funções que interagem com as classes

def depositar(cliente):
    cpf_conta = input("Informe o CPF do titular da conta para depositar: ")
    conta = recuperar_conta_cliente(cliente, cpf_conta)
    
    if not conta:
        print("\nConta não encontrada!")
        return

    valor = float(input('Informe o valor do depósito: R$ '))
    transacao = Deposito(valor)
    
    if transacao.registrar(conta):
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {conta.numero}!")

def sacar(cliente):
    cpf_conta = input("Informe o CPF do titular da conta para sacar: ")
    conta = recuperar_conta_cliente(cliente, cpf_conta)
    
    if not conta:
        print("\nConta não encontrada!")
        return

    valor = float(input('Informe o valor do saque: R$ '))
    transacao = Saque(valor)

    if transacao.registrar(conta):
        print(f"Saque de R$ {valor:.2f} realizado com sucesso da conta {conta.numero}!")

def exibir_extrato(cliente):
    cpf_conta = input("Informe o CPF do titular da conta para visualizar o extrato: ")
    conta = recuperar_conta_cliente(cliente, cpf_conta)
    
    if not conta:
        print("\nConta não encontrada!")
        return

    print("\n" + "=" * 30)
    print("           EXTRATO")
    print("=" * 30)

    transacoes = conta.historico.transacoes

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            print(f"{transacao['tipo']}: R$ {transacao['valor']:.2f}")

    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("=" * 30)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    
    # Verifica se já existe um usuário com o CPF informado
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("\nCPF já cadastrado! Não é possível criar um novo usuário com este CPF.")
            return None

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/estado): ")

    novo_usuario = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    usuarios.append(novo_usuario)
    print("\nUsuário cadastrado com sucesso!")
    return novo_usuario

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do usuário para associar à conta: ")
    
    cliente_encontrado = None
    for cliente in clientes:
        if cliente.cpf == cpf:
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        nova_conta = ContaCorrente.nova_conta(cliente_encontrado, numero_conta)
        contas.append(nova_conta)
        cliente_encontrado.adicionar_conta(nova_conta)
        print("\nConta criada com sucesso!")
        return nova_conta
    else:
        print("\nUsuário não encontrado! Não é possível criar a conta.")
        return None

def listar_contas(contas):
    if not contas:
        print("\nNão há contas cadastradas.")
        return

    print("\n" + "=" * 30)
    print("           CONTAS CADASTRADAS")
    print("=" * 30)
    for conta in contas:
        print(textwrap.dedent(str(conta)))
        print("-" * 30)

def listar_usuarios(usuarios):
    if not usuarios:
        print("\nNão há usuários cadastrados.")
        return

    print("\n" + "=" * 30)
    print("           USUÁRIOS CADASTRADOS")
    print("=" * 30)
    for usuario in usuarios:
        line = f"""\
            Nome:\t\t{usuario.nome}
            CPF:\t\t{usuario.cpf}
            Nascimento:\t{usuario.data_nascimento}
            Endereço:\t{usuario.endereco}
        """
        print(textwrap.dedent(line))
        print("-" * 30)

def recuperar_conta_cliente(cliente, cpf):
    for conta in cliente.contas:
        if conta.cliente.cpf == cpf:
            return conta
    return None

def main():
    usuarios = []
    contas = []
    next_account_number = 1

    # Main menu for client operations
    def client_menu(user_client):
        menu_options = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        => """

        while True:
            option = input(textwrap.dedent(menu_options)).lower().strip()

            if option == 'd':
                depositar(user_client) # Passa o cliente logado
            elif option == 's':
                sacar(user_client) # Passa o cliente logado
            elif option == 'e':
                exibir_extrato(user_client) # Passa o cliente logado
            elif option == 'q':
                print("Obrigado por usar nosso caixa eletrônico!")
                return
            else:
                print("Opção inválida! Por favor, selecione uma opção válida.")

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
                    criar_usuario(usuarios)
                elif admin_option == 'nc':
                    new_account = criar_conta("0001", usuarios, contas)
                    if new_account:
                        next_account_number += 1 # Incrementa apenas se a conta foi criada com sucesso
                elif admin_option == 'lu':
                    listar_usuarios(usuarios)
                elif admin_option == 'lc':
                    listar_contas(contas)
                elif admin_option == 's':
                    print("\nSaindo do modo ADMIN.")
                    break
                else:
                    print("Opção inválida! Por favor, selecione uma opção válida.")

        elif role_option == 'c':
            account_options = """
            [e] Entrar
            [q] Sair
            =>"""

            while True:
                account_option = input(textwrap.dedent(account_options)).lower().strip()

                if account_option == 'e':
                    cpf_login = input("Informe o CPF para entrar na conta: ")
                    
                    user_client = None
                    for user in usuarios:
                        if user.cpf == cpf_login:
                            user_client = user
                            break
                    
                    if user_client:
                        print(f"\nBem-vindo(a), {user_client.nome}!")
                        client_menu(user_client) # Agora passa o objeto cliente
                    else:
                        print("\nUsuário não encontrado! Por favor, cadastre-se primeiro.")

                elif account_option == 'q':
                    print("\nSaindo do modo CLIENTE.")
                    break
                else:
                    print("Opção inválida! Por favor, selecione uma opção válida.")

        elif role_option == 'q':
            print("\nEncerrando o sistema bancário. Até mais!")
            break
        else:
            print("Opção inválida! Por favor, selecione uma opção válida.")


# Executa a função principal
if __name__ == "__main__":
    main()
