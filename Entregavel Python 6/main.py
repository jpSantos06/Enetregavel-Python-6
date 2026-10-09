from cliente import Cliente
from contas import Conta, ContaCorrente, ContaPoupanca


def demonstrar_sistema():
    print("===== SISTEMA BANCÁRIO ORIENTADO A OBJETOS =====\n")

    # Criar clientes
    clientes = [
        Cliente("Ana Silva", "ana@email.com"),
        Cliente("Bruno Costa", "bruno@email.com"),
        Cliente("Carla Souza", "carla@email.com"),
        Cliente("Daniel Lima", "daniel@email.com"),
        Cliente("Eva Santos", "eva@email.com"),
        Cliente("Felipe Rocha", "felipe@email.com"),
        Cliente("Gabriela Alves", "gabriela@email.com"),
        Cliente("Hugo Martins", "hugo@email.com"),
        Cliente("Ines Ferreira", "ines@email.com"),
        Cliente("Joao Pereira", "joao@email.com"),
    ]

    # Criar dez contas de diferentes tipos
    contas = [
        ContaCorrente("CC001", clientes[0], 1000),
        ContaPoupanca("CP002", clientes[1], 2000),
        ContaCorrente("CC003", clientes[2], 1500),
        ContaPoupanca("CP004", clientes[3], 3000),
        ContaCorrente("CC005", clientes[4], 500),
        ContaPoupanca("CP006", clientes[5], 2500),
        ContaCorrente("CC007", clientes[6], 800),
        ContaPoupanca("CP008", clientes[7], 4000),
        ContaCorrente("CC009", clientes[8], 1200),
        ContaPoupanca("CP010", clientes[9], 3500),
    ]

    # Demonstração de __str__ e __repr__
    print("--- Clientes ---")
    for cliente in clientes:
        print(cliente)

    print("\n--- Contas cadastradas ---")
    for conta in contas:
        print(conta)

    print("\n--- Demonstração de polimorfismo ---")

    # A mesma chamada produz resultados diferentes
    # conforme o tipo de conta.
    for conta in contas:
        rendimento = conta.calcular_rendimento()
        print(
            f"{conta.numero} | "
            f"Tipo: {conta.__class__.__name__} | "
            f"Rendimento: €{rendimento:.2f}"
        )

    print("\n--- Depósitos e saques ---")

    contas[0].depositar(200)
    print(f"Saldo após depósito: €{contas[0].saldo:.2f}")

    contas[0].sacar(100)
    print(f"Saldo após saque e taxa: €{contas[0].saldo:.2f}")

    print("\n--- Ordenação por saldo ---")
    for conta in sorted(contas):
        print(f"{conta.numero}: €{conta.saldo:.2f}")

    print("\n--- Testes de exceções ---")

    # E-mail inválido
    try:
        Cliente("Utilizador Inválido", "email-sem-arroba")
    except ValueError as erro:
        print(f"Erro de cliente: {erro}")

    # Saldo inicial negativo
    try:
        ContaCorrente("CC999", clientes[0], -100)
    except ValueError as erro:
        print(f"Erro de saldo: {erro}")

    # Saque acima do saldo
    try:
        contas[4].sacar(100000)
    except ValueError as erro:
        print(f"Erro de saque: {erro}")

    # Tentativa de instanciar a classe abstrata
    try:
        Conta("CX000", clientes[0], 100)
    except TypeError as erro:
        print(f"Erro de classe abstrata: {erro}")

    # Taxa inválida
    try:
        contas[0].taxa_saque = 2
    except ValueError as erro:
        print(f"Erro de taxa: {erro}")

    print("\n--- Comparação de objetos ---")
    print(f"Primeira conta: {contas[0]!r}")
    print(f"Contas com mesmo número são iguais: {contas[0] == contas[0]}")
    print(f"Primeira conta tem saldo menor que a segunda: {contas[0] < contas[1]}")

    print("\n===== FIM DA DEMONSTRAÇÃO =====")


if __name__ == "__main__":
    demonstrar_sistema()