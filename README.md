# FinancialTransaction

## Descrição do Projeto

O projeto FinancialTransaction é uma implementação Python de um sistema de transações financeiras que segue as melhores práticas de programação, princípios SOLID e utiliza padrões de projeto para fornecer uma solução robusta e extensível. Esse sistema permite a realização de transações financeiras entre contas, com validações avançadas, registro de eventos e flexibilidade para adicionar novos recursos.

## Princípios e Padrões de Projeto

Neste projeto, aplicamos vários princípios e padrões de projeto, incluindo:

- **Padrão Observer**: Implementamos o padrão Observer para permitir que várias partes do sistema observem e reajam a eventos, como a notificação de transações bem-sucedidas ou canceladas. O Logger atua como o sujeito observável, enquanto o ConsoleLogger atua como o observador que recebe notificações.

- **Princípios SOLID**: Vários princípios do SOLID são aplicados no projeto:
  - **Princípio da Responsabilidade Única (SRP)**: Cada classe tem uma única responsabilidade bem definida, como AccountRepository para operações de conta, Logger para registro de eventos e TransactionUseCase para manipulação de transações.
  - **Princípio Aberto/Fechado (OCP)**: O código é projetado para ser extensível sem modificação. Você pode adicionar novos observadores, manipuladores ou classes relacionadas sem modificar o código existente.
  - **Princípio de Substituição de Liskov (LSP)**: As classes derivadas, como ConsoleLogger, podem ser substituídas pelas classes base, como Observer, sem causar problemas.
  - **Princípio de Segregação de Interface (ISP)**: As interfaces são projetadas de forma coesa, contendo métodos relevantes apenas para seus observadores.

- **Padrão de Repositório**: Implementamos o padrão de repositório na classe AccountRepository, que isola a lógica de acesso aos dados das contas, tornando-a independente de como os dados são armazenados.

- **Padrão de Injeção de Dependência**: Aplicamos o princípio de injeção de dependência ao passar as dependências (por exemplo, AccountRepository e Logger) para as classes que delas dependem (por exemplo, TransactionUseCase). Isso torna o código mais testável e flexível.

- **Padrão de Comando**: O TransactionUseCase age como um manipulador de comandos que executa transações. Ele decide como executar uma transação com base em regras de negócios.

- **Princípio de Responsabilidade Única**: As classes são projetadas com responsabilidades únicas e bem definidas, promovendo a coesão e facilitando a manutenção.

- **Princípio da Inversão de Dependência**: O código segue o princípio da inversão de dependência, onde depende de abstrações em vez de implementações concretas. Por exemplo, TransactionUseCase depende de interfaces (AccountRepository e Logger) em vez de implementações concretas.

## Componentes Principais

### 1. AccountRepository (repositories/account_repository.py)

O AccountRepository é responsável por armazenar os saldos das contas e fornece métodos para acessar e atualizar esses saldos. Ele utiliza um dicionário para manter o mapeamento de IDs de contas para saldos.

**Vantagens**:

- **Abstração de Dados**: O AccountRepository isola a lógica de acesso aos dados das contas, tornando-o independente de como os dados são armazenados. Isso facilita a troca de fontes de dados, como bancos de dados, sem afetar o restante do código.
- **Facilidade de Testes**: Como a lógica de acesso aos dados é encapsulada, é mais fácil escrever testes unitários para o código que depende do repositório de contas.

### 2. Logger (logger/logger.py)

O Logger é uma classe abstrata que implementa o padrão Observer. Ele permite que observadores, como o ConsoleLogger, sejam anexados para receber notificações quando eventos ocorrem.

**Vantagens**:

- **Desacoplamento**: O padrão Observer permite que o código que gera eventos (no caso, transações bem-sucedidas ou canceladas) esteja desacoplado dos observadores. Isso significa que você pode adicionar ou remover observadores sem alterar o código do emissor de eventos.
- **Flexibilidade**: Você pode facilmente estender o sistema para adicionar outros tipos de observadores, como registradores de eventos em arquivo, notificações por email, etc.

### 3. TransactionUseCase (use_cases/transaction_use_case.py)

O TransactionUseCase é o componente central do projeto. Ele lida com a lógica de execução das transações e atualização dos saldos das contas.

**Vantagens**:

- **Separação de Responsabilidades**: O TransactionUseCase cumpre o princípio de responsabilidade única e concentra-se na lógica de execução de transações. Ele delega a lógica de registro de eventos e manipulação de saldo a outros componentes.
- **Injeção de Dependência**: Ele aceita as dependências (um repositório de contas e um logger) como parâmetros no construtor, seguindo o princípio de injeção de dependência, tornando-o mais flexível e testável.
- **Testabilidade**: A lógica de execução de transações é isolada em uma classe independente, o que facilita a escrita de testes unitários para essa funcionalidade específica.

## Pontos Fortes do Projeto

O projeto FinancialTransaction apresenta diversos pontos fortes:

- **Separação de Responsabilidades**: A implementação segue os princípios do SOLID, com responsabilidades bem definidas para cada classe. As classes são coesas e têm funções específicas.
- **Padrão de Projeto Observer**: A implementação utiliza o padrão Observer para notificar observadores sobre eventos, como o registro de log. Isso permite a extensibilidade ao adicionar novos observadores sem modificar o código existente.
- **Validação Avançada**: A implementação realiza validações detalhadas, verificando se as contas de origem e destino existem, se os valores da transação são válidos e se não há campos nulos na transação.
- **Log Centralizado**: A classe LoggerService fornece um mecanismo centralizado para registro de log em todo o projeto, facilitando o gerenciamento e a consistência das mensagens de log.
- **Singleton**: A classe LoggerService é implementada como um singleton, garantindo que haja apenas uma instância global do logger em todo o projeto.
- **Injeção de Dependência**: A injeção de dependência é utilizada para fornecer instâncias necessárias, como LoggerService, às classes que delas dependem. Isso torna o código mais testável e flexível.
- **Tratamento de Erros**: A implementação trata erros adequadamente, registrando mensagens de erro no log quando ocorrem situações problemáticas, como transações canceladas.
- **Testabilidade**: A estrutura do código facilita a escrita de testes unitários para as diferentes partes do sistema, garantindo a confiabilidade e robustez do software.
- **Tipagem Forte**: A utilização de anotações de tipo (typing hints) ajuda a melhorar a legibilidade e a manutenção do código Python.
- **Linguagem de Alto Nível**: O código está escrito em uma linguagem de alto nível (Python), o que torna a implementação mais acessível e legível.
- **Documentação e Comentários**: A implementação contém comentários que explicam a lógica e o propósito de várias partes do código, facilitando a compreensão e a manutenção.
- **Segurança e Consistência**: A adição de validações de segurança, como a verificação de campos nulos, ajuda a garantir a consistência dos dados e evita erros inesperados.
- **Padrões de Projeto**: A implementação segue padrões de projeto como Singleton, Observer e Injeção de Dependência, o que melhora a organização e a manutenibilidade do código.

## Como Executar o Projeto

Para executar o projeto, siga as instruções abaixo:

1. Clone o repositório para o seu ambiente local.
2. Certifique-se de que você possui o Python instalado em seu sistema.
3. Navegue até o diretório raiz do projeto.
4. Execute o script `main.py` para executar o programa.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request com melhorias ou novos recursos.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

