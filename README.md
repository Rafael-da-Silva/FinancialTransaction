# FinancialTransaction

Neste projeto, foram utilizados os seguintes padrões de projeto e princípios de design:

## Padrão Observer
O padrão Observer foi implementado para permitir que várias partes do sistema observem e reajam a eventos, como a notificação de transações bem-sucedidas ou canceladas. O Logger atua como o sujeito observável, enquanto o ConsoleLogger atua como o observador que recebe notificações.

## Princípio SOLID
Vários princípios do SOLID são aplicados no projeto:

- **Single Responsibility Principle (SRP)**: As classes têm responsabilidades únicas e bem definidas, como AccountRepository para operações de conta, Logger para registro de eventos e TransactionUseCase para manipulação de transações.

- **Open/Closed Principle (OCP)**: O código é projetado para ser extensível sem modificação. Você pode adicionar novos observadores, manipuladores ou classes relacionadas sem modificar o código existente.

- **Liskov Substitution Principle (LSP)**: As classes derivadas, como ConsoleLogger, podem ser substituídas pelas classes base, como Observer, sem causar problemas.

- **Interface Segregation Principle (ISP)**: Interfaces são projetadas de forma coesa e com métodos relevantes apenas para seus observadores.

## Padrão de Repositório
O padrão de repositório é implementado na classe AccountRepository, que isola a lógica de acesso aos dados das contas, tornando-a independente de como os dados são armazenados.

## Padrão de Injeção de Dependência
O princípio de injeção de dependência é aplicado ao passar as dependências (por exemplo, AccountRepository e Logger) para as classes que delas dependem (por exemplo, TransactionUseCase). Isso torna o código mais testável e flexível.

## Padrão de Comando
O TransactionUseCase age como um manipulador de comandos que executa transações. Ele decide como executar uma transação com base em regras de negócios.

## Clean Architecture
Este projeto segue os princípios do Clean Architecture, que organiza o código em camadas bem definidas, promovendo a separação de responsabilidades e a flexibilidade do sistema. As principais camadas incluem:

- **Entidades (Entities)**: Contêm as entidades de domínio do sistema, como Account e Transaction.

- **Casos de Uso (Use Cases)**: Representam as funcionalidades principais do sistema e contêm a lógica de negócios, como TransactionUseCase.

- **Interface de Usuário (UI)**: Pode ser adicionada para interagir com o usuário.

- **Controladores (Controllers)**: Controlam as interações da interface de usuário.

- **Frameworks e Drivers**: Detalhes de implementação específicos, como bancos de dados.

- **Infraestrutura (Infrastructure)**: Detalhes de implementação de baixo nível, como acesso a recursos externos.

A estrutura do Clean Architecture promove a separação de responsabilidades, facilita a testabilidade, permite a substituição de componentes sem afetar outros e mantém uma clara dependência das camadas internas para as externas.

## Pontos Fortes

- Separação de Responsabilidades: A implementação segue os princípios do SOLID, com responsabilidades bem definidas para cada classe. As classes são coesas e têm funções específicas.

- Padrão de Projeto Observer: A implementação utiliza o padrão Observer para notificar observadores sobre eventos, como o registro de log. Isso permite a extensibilidade ao adicionar novos observadores sem modificar o código existente.

- Validade Avançada: A implementação realiza validações detalhadas, verificando se as contas de origem e destino existem, se os valores da transação são válidos e se não há campos nulos na transação.

- Log Centralizado: A classe LoggerService fornece um mecanismo centralizado para registro de log em todo o projeto, facilitando o gerenciamento e a consistência das mensagens de log.

- Singleton: A classe LoggerService é implementada como um singleton, garantindo que haja apenas uma instância global do logger em todo o projeto.

- Injeção de Dependência: A injeção de dependência é utilizada para fornecer instâncias necessárias, como LoggerService, às classes que delas dependem. Isso torna o código mais testável e flexível.

- Tratamento de Erros: A implementação trata erros adequadamente, registrando mensagens de erro no log quando ocorrem situações problemáticas, como transações canceladas.

- Testabilidade: A estrutura do código facilita a escrita de testes unitários para as diferentes partes do sistema, garantindo a confiabilidade e robustez do software.

- Tipagem Forte: A utilização de anotações de tipo (typing hints) ajuda a melhorar a legibilidade e a manutenção do código Python.

- Linguagem de Alto Nível: O código está escrito em uma linguagem de alto nível (Python), o que torna a implementação mais acessível e legível.

- Documentação e Comentários: A implementação contém comentários que explicam a lógica e o propósito de várias partes do código, facilitando a compreensão e a manutenção.

- Segurança e Consistência: A adição de validações de segurança, como a verificação de campos nulos, ajuda a garantir a consistência dos dados e evita erros inesperados.

- Padrões de Projeto: A implementação segue padrões de projeto como Singleton, Observer e Injeção de Dependência, o que melhora a organização e a manutenibilidade do código.
