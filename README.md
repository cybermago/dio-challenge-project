# Desafio de Sistema Bancário em Python

## Visão Geral do Projeto

Fomos contratados por um grande banco para desenvolver um novo sistema bancário. A primeira versão deste sistema visa modernizar as operações existentes e será implementada utilizando a linguagem Python.

## Objetivo Geral

O objetivo principal é criar um sistema bancário simples que permita as seguintes operações:

* **Depositar**
* **Sacar**
* **Visualizar Extrato**

## Detalhes das Operações

### 1. Operação de Depósito

* Deve ser possível depositar valores positivos na conta bancária.
* Nesta versão V1, o sistema funcionará com **apenas um usuário**. Portanto, não é necessário se preocupar com a identificação de agência e conta bancária.
* Todos os depósitos devem ser armazenados em uma variável para posterior exibição na operação de extrato.

### 2. Operação de Saque

* O sistema deve permitir a realização de **3 saques diários**.
* O limite máximo por saque é de **R$ 500,00**.
* Caso o usuário não tenha saldo suficiente em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
* Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### 3. Operação de Extrato

* Esta operação deve listar todos os depósitos e saques realizados na conta.
* Ao final da listagem, deve ser exibido o saldo atual da conta.
* Os valores (depósitos, saques e saldo) devem ser exibidos utilizando o formato `R$ xxx.xx`.
    * **Exemplo:** `1500.45 = R$ 1500.45`
---
