from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation


def converter_valor(valor):
    """Converte um valor para Decimal e rejeita entradas inválidas."""
    if isinstance(valor, bool):
        raise ValueError("O valor monetário é inválido.")

    try:
        resultado = Decimal(str(valor))
    except (InvalidOperation, ValueError):
        raise ValueError("Informe um valor monetário válido.")

    if not resultado.is_finite():
        raise ValueError("O valor deve ser um número finito.")

    return resultado.quantize(Decimal("0.01"))


class Conta(ABC):
    """Classe abstrata que define o comportamento comum das contas."""

    def __init__(self, numero, cliente, saldo=0):
        if not isinstance(numero, str) or not numero.strip():
            raise ValueError("O número da conta é obrigatório.")

        from cliente import Cliente

        if not isinstance(cliente, Cliente):
            raise TypeError("A conta deve estar associada a um Cliente.")

        self.__numero = numero.strip()
        self.__cliente = cliente
        self.__saldo = Decimal("0.00")

        saldo_inicial = converter_valor(saldo)
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")

        self.__saldo = saldo_inicial

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        valor = converter_valor(valor)

        if valor <= 0:
            raise ValueError("O depósito deve ser maior que zero.")

        self.__saldo += valor

    def sacar(self, valor):
        valor = converter_valor(valor)

        if valor <= 0:
            raise ValueError("O saque deve ser maior que zero.")

        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente.")

        taxa = self.calcular_taxa(valor)
        total = valor + taxa

        if total > self.__saldo:
            raise ValueError("Saldo insuficiente para o saque e a taxa.")

        self.__saldo -= total

    def _adicionar_rendimento(self, valor):
        """Método interno para creditar rendimentos."""
        valor = converter_valor(valor)

        if valor < 0:
            raise ValueError("O rendimento não pode ser negativo.")

        self.__saldo += valor

    @abstractmethod
    def calcular_rendimento(self):
        """Calcula o rendimento de acordo com o tipo de conta."""
        pass

    @abstractmethod
    def calcular_taxa(self, valor):
        """Calcula a taxa de saque de acordo com o tipo de conta."""
        pass

    def __str__(self):
        return (
            f"{self.__class__.__name__} | Conta: {self.numero} | "
            f"Titular: {self.cliente.nome} | Saldo: €{self.saldo:.2f}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"numero={self.numero!r}, "
            f"cliente={self.cliente!r}, saldo={self.saldo!r})"
        )

    def __eq__(self, outro):
        if not isinstance(outro, Conta):
            return NotImplemented
        return self.numero == outro.numero

    def __lt__(self, outro):
        if not isinstance(outro, Conta):
            return NotImplemented
        return self.saldo < outro.saldo


class ContaCorrente(Conta):
    """Conta corrente com taxa de saque de 1%."""

    def __init__(self, numero, cliente, saldo=0, taxa_saque=Decimal("0.01")):
        super().__init__(numero, cliente, saldo)
        self.taxa_saque = taxa_saque

    @property
    def taxa_saque(self):
        return self.__taxa_saque

    @taxa_saque.setter
    def taxa_saque(self, valor):
        valor = converter_valor(valor)

        if valor < 0 or valor > 1:
            raise ValueError("A taxa deve estar entre 0 e 1.")

        self.__taxa_saque = valor

    def calcular_rendimento(self):
        # Conta corrente não gera rendimento neste exemplo.
        return Decimal("0.00")

    def calcular_taxa(self, valor):
        valor = converter_valor(valor)
        return (valor * self.taxa_saque).quantize(Decimal("0.01"))


class ContaPoupanca(Conta):
    """Conta poupança com rendimento de 0,5%."""

    def __init__(
        self, numero, cliente, saldo=0,
        taxa_rendimento=Decimal("0.005")
    ):
        super().__init__(numero, cliente, saldo)
        self.taxa_rendimento = taxa_rendimento

    @property
    def taxa_rendimento(self):
        return self.__taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, valor):
        valor = converter_valor(valor)

        if valor < 0 or valor > 1:
            raise ValueError("O rendimento deve estar entre 0 e 1.")

        self.__taxa_rendimento = valor

    def calcular_rendimento(self):
        rendimento = (
            self.saldo * self.taxa_rendimento
        ).quantize(Decimal("0.01"))

        self._adicionar_rendimento(rendimento)
        return rendimento

    def calcular_taxa(self, valor):
        # Neste exemplo, a poupança não cobra taxa de saque.
        return Decimal("0.00")
    