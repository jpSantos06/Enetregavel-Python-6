
import re


class Cliente:
    """Representa um cliente do sistema bancário."""

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome não pode estar vazio.")
        self.__nome = valor.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str):
            raise ValueError("O e-mail deve ser um texto.")

        padrao = r"^[\w.+-]+@[\w-]+(?:\.[\w-]+)+$"

        if not re.fullmatch(padrao, valor):
            raise ValueError("Formato de e-mail inválido.")

        self.__email = valor

    def __str__(self):
        return f"Cliente: {self.nome} | E-mail: {self.email}"

    def __repr__(self):
        return f"Cliente(nome={self.nome!r}, email={self.email!r})"

    def __eq__(self, outro):
        if not isinstance(outro, Cliente):
            return NotImplemented
        return self.email.casefold() == outro.email.casefold()