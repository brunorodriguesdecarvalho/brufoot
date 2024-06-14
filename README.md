# BruFoot

## Sobre

- Trata-se de um simulador de gerenciamento de times de futebol.
- A intenção é usar esse jogo como forma de aprender técnicas relacionadas a inteligência artificial.

## Requisitos

Uma lista de requisitos para guiar o desenvolvimento do jogo a longo prazo.

### Requisitos Funcionais Elementares

1. [ ] Cadastro de Times
    - [ ] O jogo deve permitir criação, leitura, atualização e exclusão de times e seus respectivos atributos.
    - [ ] O jogo deve ter uma interface para adicionar, editar ou remover times.
    - [ ] Os atributos dos times devem ser persistidos em um banco de dados SQLite.
2. [ ] Cadastro de Jogadores
    - [ ] O jogo deve permitir criação, leitura, atualização e exclusão de jogadores e seus respectivos atributos.
    - [ ] O jogo deve ter uma interface para adicionar, editar ou remover jogadores.
    - [ ] Os atributos dos jogadores devem ser persistidos em um banco de dados SQLite.
3. [ ] Simulação de Partidas
    - [ ] O jogo deve simular partidas entre dois times com base nas habilidades dos jogadores e nas táticas escolhidas.
    - [ ] O jogo deve permitir que os resultados das partidas sejam salvos em um banco de dados SQLite e retomados em um momento posterior.
4. [ ] Gerenciamento de Táticas
    - [ ] O sistema deve permitir que o usuário defina táticas de jogo para seus times, incluindo formações e estratégias de ataque e defesa.
5. [ ] Gerenciamento de Liga
    - [ ] O sistema deve permitir a criação e gerenciamento de ligas, com tabelas de classificação, rodadas e resultados de partidas.

### Requisitos Funcionais Avançados (Uso de IA)
1. [ ] Sistema de Recomendação de Jogadores
    - [ ] A IA do jogo deve sugerir jogadores para contratação com base nas necessidades do time e no desempenho histórico dos jogadores.
2. [ ] Análise de Desempenho Pós-Jogo
    - [ ] A IA do jogo deve fornecer uma análise detalhada do desempenho dos jogadores e do time após cada partida.

## Requisitos Não Funcionais

### Usabilidade
- A interface do usuário deve ser simples e fácil de usar.

### Desempenho
- O jogo deve ser capaz de simular cada tempo de uma partida de futebol em 45 segundos. 

### Confiabilidade
- O sistema deve garantir que os dados não sejam corrompidos e que a simulação de partidas seja consistente.

### Portabilidade
- O sistema deve ser compatível com Windows.

### Segurança
- O jogo deve ser executado localmente e não ter qualquer tipo de conexão com a internet.
- O jogo não deve salvar nenhum tipo de dado do usuário que possa ser utilizado na identificação, exceto o nome do jogador. 