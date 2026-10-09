# Sistema Bancário Orientado a Objetos em Python
1. Descrição do projeto

Este projeto implementa um sistema bancário simples em Python, aplicando os principais conceitos da Programação Orientada a Objetos (POO).

O sistema permite representar clientes, contas correntes e contas poupança, realizar depósitos e saques, calcular rendimentos e demonstrar o tratamento de erros.

2. Objetivos
Criar classes e instanciar objetos.
Aplicar encapsulamento com @property.
Utilizar herança e super().
Implementar uma classe abstrata com ABC e @abstractmethod.
Demonstrar polimorfismo.
Implementar métodos especiais, como __str__, __repr__, __eq__ e __lt__.
Tratar entradas inválidas com try/except.
3. Tecnologias utilizadas
Python 3
Módulo abc
Módulo decimal
Módulo re
Git e GitHub

Não é necessário instalar bibliotecas externas.

4. Estrutura do projeto
sistema-bancario-poo/
├── main.py
├── cliente.py
├── contas.py
└── README.md

5. Diagrama de classes
classDiagram
    class Cliente {
        -str nome
        -str email
        +nome property
        +email property
        +__str__()
        +__repr__()
        +__eq__(outro)
    }

    class Conta {
        <<abstract>>
        -str numero
        -Cliente cliente
        -Decimal saldo
        +depositar(valor)
        +sacar(valor)
        +calcular_rendimento()*
        +calcular_taxa(valor)*
        +__str__()
        +__repr__()
        +__eq__(outro)
        +__lt__(outro)
    }

    class ContaCorrente {
        -Decimal taxa_saque
        +calcular_rendimento()
        +calcular_taxa(valor)
    }

    class ContaPoupanca {
        -Decimal taxa_rendimento
        +calcular_rendimento()
        +calcular_taxa(valor)
    }

    Conta <|-- ContaCorrente
    Conta <|-- ContaPoupanca
    Cliente "1" <-- "0..*" Conta : titular

6. Justificativa da modelagem
Classe Cliente

Armazena o nome e o e-mail do titular da conta. As propriedades validam os dados antes de os guardar.

Classe abstrata Conta

Define os atributos e comportamentos comuns às contas bancárias, como número, titular, saldo, depósito e saque.

A classe é abstrata porque não deve ser instanciada diretamente. Cada tipo de conta deve implementar os métodos abstratos de rendimento e taxa.

Classe ContaCorrente

Herda de Conta e utiliza super().__init__() para reaproveitar o construtor da classe mãe.

Neste exemplo, a conta corrente não gera rendimento e aplica uma taxa de saque configurável.

Classe ContaPoupanca

Também herda de Conta, mas calcula um rendimento sobre o saldo. Não aplica taxa de saque neste exemplo.

Herança e composição

A herança foi escolhida porque uma conta corrente e uma conta poupança são tipos de conta bancária.

A composição foi utilizada para associar uma conta a um objeto Cliente, pois uma conta possui um titular. O cliente é criado separadamente e passado para o construtor da conta.

7. Encapsulamento com @property

As propriedades permitem consultar atributos privados e validar alterações.

Nome: não aceita texto vazio.
E-mail: verifica o formato através de uma expressão regular.
Saldo: é consultado por uma propriedade sem setter público; as operações de depósito, saque e rendimento controlam as alterações.
Taxa de saque: não pode ser negativa nem superior a 100%.
Taxa de rendimento: não pode ser negativa nem superior a 100%.
Valores monetários: são convertidos para Decimal, rejeitando valores inválidos e não finitos.

Essas validações ajudam a impedir que os objetos assumam estados inconsistentes.

8. Polimorfismo

O método calcular_rendimento() está definido na classe abstrata e implementado nas classes filhas.

Na conta corrente, o rendimento é zero. Na conta poupança, o rendimento é calculado a partir do saldo e da taxa configurada.

O programa percorre uma lista de contas e chama o mesmo método em objetos de tipos diferentes:

for conta in contas:
    rendimento = conta.calcular_rendimento()
    print(rendimento)


O comportamento depende da classe concreta do objeto.

9. Métodos especiais
__init__: inicializa os objetos.
__str__: apresenta uma descrição amigável.
__repr__: fornece uma representação orientada à depuração.
__eq__: compara clientes pelo e-mail ou contas pelo número.
__lt__: permite ordenar contas pelo saldo com sorted().
10. Tratamento de exceções

O programa utiliza try/except para capturar erros, como:

E-mail inválido.
Saldo inicial negativo.
Saque superior ao saldo disponível.
Tentativa de instanciar uma classe abstrata.
Definição de taxas fora dos limites permitidos.

As exceções tornam o programa mais robusto e permitem apresentar mensagens compreensíveis ao utilizador.

11. Testes e demonstração

O arquivo main.py cria dez clientes e dez contas, misturando contas correntes e contas poupança.

A demonstração inclui:

Exibição dos clientes e das contas.
Cálculo polimórfico de rendimentos.
Depósitos e saques.
Ordenação por saldo.
Comparação de objetos.
Testes de entradas inválidas e exceções.
12. Como executar
Instale o Python 3.
Coloque os arquivos main.py, cliente.py e contas.py na mesma pasta.
Abra o terminal nessa pasta.
Execute:
python main.py


Se o sistema utilizar o comando python3, execute:

python3 main.py

13. Conclusão

O projeto demonstra os principais conceitos de Programação Orientada a Objetos em Python, incluindo abstração, encapsulamento, herança, polimorfismo, métodos especiais e tratamento de exceções.

A separação em módulos facilita a manutenção, a leitura e a reutilização do código, enquanto o README documenta as decisões de modelagem e o funcionamento do sistema.
