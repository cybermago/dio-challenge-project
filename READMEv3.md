Com certeza! As imagens indicam que o projeto será atualizado para uma versão mais robusta, utilizando Programação Orientada a Objetos (POO) e modelagem UML para o sistema bancário. Com base nisso, aqui está uma atualização do seu README, incorporando as informações das imagens e o conceito de POO:

---

# Desafio de Sistema Bancário em Python

## Visão Geral do Projeto

Fomos contratados por um grande banco para desenvolver um novo sistema bancário. A primeira versão deste sistema visa modernizar as operações existentes e será implementada utilizando a linguagem Python, com foco em Programação Orientada a Objetos (POO) e um modelo de classes UML.

## Objetivo Geral

O objetivo principal é iniciar a modelagem de um sistema bancário em POO, adicionando classes para clientes e operações bancárias. O código deve seguir o modelo de classes UML fornecido, que inclui as seguintes operações:

* **Depositar**
* **Sacar**
* **Visualizar Extrato**

## Detalhes das Operações (V1 - Revisitada com POO)

Nesta etapa, o foco é a implementação inicial das operações, com a estrutura de classes definida no diagrama UML.

### 1. Operação de Depósito

* Deve ser possível depositar valores positivos na conta bancária.
* Todos os depósitos devem ser armazenados em uma variável (ou atributo de classe) para posterior exibição na operação de extrato.

### 2. Operação de Saque

* O sistema deve permitir a realização de **3 saques diários**.
* O limite máximo por saque é de **R$ 500,00**.
* Caso o usuário não tenha saldo suficiente em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
* Todos os saques devem ser armazenados em uma variável (ou atributo de classe) e exibidos na operação de extrato.

### 3. Operação de Extrato

* Esta operação deve listar todos os depósitos e saques realizados na conta.
* Ao final da listagem, deve ser exibido o saldo atual da conta.
* Os valores (depósitos, saques e saldo) devem ser exibidos utilizando o formato `R$ xxx.xx`.
    * **Exemplo:** `1500.45 = R$ 1500.45`

---

## Próximos Passos (V2 - Aprimoramento e Modularização com Funções e Classes)

Para aprimorar o sistema, a versão 2 trará as seguintes melhorias e novas funcionalidades, com o código mais modularizado através do uso de funções e a incorporação de classes para clientes e contas.

### Novas Funções e Estrutura de Classes

1.  **Atualizar a implementação do sistema bancário** para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML apresentado.

2.  **Criar Usuário (Cliente)**
    * O programa deve armazenar os usuários em uma lista de objetos `PessoaFisica` ou `Cliente`.
    * Um usuário (`PessoaFisica`) é composto por: `nome`, `data de nascimento`, `cpf` e `endereço`.
    * O endereço deve ser uma string com o formato: `logradouro, nro - bairro - cidade/sigla estado`.
    * Deve ser armazenado **somente os números do CPF**.
    * Não podemos cadastrar 2 usuários com o mesmo CPF.

3.  **Criar Conta Corrente**
    * O programa deve armazenar contas em uma lista de objetos `ContaCorrente`.
    * Uma conta é composta por: `agência`, `número da conta` e `usuário` (referência a um objeto `Cliente` ou `PessoaFisica`).
    * O número da conta é sequencial, iniciando em 1.
    * O número da agência é fixo: `"0001"`.
    * O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.

4.  **Desafio Extra:** Após concluir a modelagem das classes e a criação dos métodos, atualizar os métodos que tratam as opções do menu para funcionarem com as classes modeladas.

---
