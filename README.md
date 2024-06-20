# BruFoot

## Sobre

- Trata-se de um simulador de gerenciamento de times de futebol.
- A intenção é usar esse jogo como forma de aprender técnicas relacionadas a inteligência artificial.


## Requisitos

Uma lista de requisitos para guiar o desenvolvimento do jogo a longo prazo.


### Requisitos Funcionais Elementares

1. Menus
    - Menu Inicial
        - [X] O jogo deve sempre começar por um menu inicial, com opções para o jogador escolher o que fazer.
        - [X] O jogo deve sempre inicializar com a tela maximizada.
        - [ ] O menu inicial deve ter as opções de jogar e personalizar.
            - [X] O jogo deve ir para o menu de personalização quando o jogador humano escolher a opção "personalizar".
            - [ ] O jogo deve ser iniciado quando o jogador humano escolher a opção "jogar".
    - Menu Personalizar
        - [X] O menu personalizar deve ter a opção de Editar Times
            - [X] O jogo deve permitir a criação de times
            - [X] O jogo deve permitir a visualização de times criados como tabela com barra de rolagem.
            - [X] O jogo deve permitir a exclusão de times com base no ID
            - [X] O jogo deve permitir a alteração de times cadastrados.
            - [ ] Os atributos iniciais de um time devem ser:
                - [X] Nome (not null  - string)
                - [ ] País (not null - string)
                    - [ ] O jogo deve permitir a escolha do país através de uma lista de países.
                - [ ] Estado (string)
                    - [ ] O jogo não deve permitir informar o estado se o país não for Brasil.
                    - [ ] O jogo deve permitir a escolha do estado se o país for Brasil.
                - [ ] Cidade (string)
                    - [ ] O jogo não deve permitir informar a cidade se o país não for Brasil.
                    - [ ] O jogo deve permitir a escolha da cidade de acordo com o estado selecionado.
                - [X] Nível Início (not null - integer, de 0 a 100)
                - [ ] Estádio (id do estádio)
                    - [ ] O jogo deve permitir a escolha de um estádio previamente cadastrado, exibindo nome e gravando o id do estádio.
                - [X] Cor Primária (not null - rgb)
                - [X] Cor Secundária (not null - rgb)
                - [ ] Técnico (id do técnico)
                    - [ ] O jogo deve permitir a escolha de um técnioc previamente cadastrado, exibindo nome e gravando o id do técnico.
        - [ ] O menu personalizar deve ter a opção de Editar Jogadores
            - [ ] O jogo deve permitir a criação de jogadores
            - [ ] O jogo deve permitir a visualização de jogadores criados como tabela com barra de rolagem.
            - [ ] O jogo deve permitir a exclusão de jogadores com base no ID
            - [ ] O jogo deve permitir a alteração de jogadores cadastrados.
            - [ ] Os atributos iniciais de um jogador devem ser:
                - [ ] Nome (not null  - string)
                - [ ] País (not null - string)
                - [ ] Idade (not null - integer, de 0 a 100)
                - [ ] Nível Início (not null - integer, de 0 a 100)
                - [ ] Posição (not null string)
        - [ ] O menu personalizar deve ter a opção de Editar Campeonatos
        - [ ] O menu personalizar deve ter a opção de Editar Estádios
2. Gerenciamento de Times
    - [ ] O jogo deve permitir criação, leitura, atualização e exclusão de times e seus respectivos atributos.
    - [ ] O jogo deve ter uma interface para adicionar, editar ou remover times.
    - [ ] Os atributos dos times devem ser persistidos em um banco de dados SQLite.
3. Gerenciamento de Jogadores
    - [ ] O jogo deve permitir criação, leitura, atualização e exclusão de jogadores e seus respectivos atributos.
    - [ ] O jogo deve ter uma interface para adicionar, editar ou remover jogadores.
    - [ ] Os atributos dos jogadores devem ser persistidos em um banco de dados SQLite.
    - [ ] O jogo deve 
4. Simulação de Partidas
    - [ ] O jogo deve simular partidas entre dois times com base nas habilidades dos jogadores e nas táticas escolhidas.
    - [ ] O jogo deve permitir que os resultados das partidas sejam salvos em um banco de dados SQLite e retomados em um momento posterior.
    - [ ] O jogo deve permitir a inclusão, atualização e exclusão de resultados de partidas, para futura utilização pela IA. 
5. Gerenciamento de Táticas
    - [ ] O jogo deve permitir que o usuário defina táticas de jogo para seus times, incluindo formações e estratégias de ataque e defesa.
6. Gerenciamento de Campeonatos
    - [ ] O jogo deve permitir a criação e gerenciamento de campeonatos e seus respectivos atributos.
7. Mercado da bola
    - [ ] O jogo deve permitir que os jogadores tenham um salário definido e que seja possível propor uma alteração de salário ao jogador.
    - [ ] O jogo deve permitir que os jogadores possam ser comprados, vendidos ou leiloados, com base no preço de mercado.
8. Gestão do Estádio e da Bilheteria
    - [ ] O jogo deve permitir que os clubes recebam após cada jogo uma receita de ingressos. 
    - [ ] O jogador humano deve poder escolher o preço dos ingressos. 


### Requisitos Funcionais Avançados (Uso de IA)
1. [ ] Simulação de Lesões e Suspensões
    - [ ] A IA deve simular eventos imprevistos, como lesões e suspensões de jogadores.
    - [ ] A IA deve sugerir medidas corretivas, como mudanças táticas ou contratações de jogadores de reposição diante desses eventos imprevistos.
2. [ ] Análise de Desempenho Pós-Jogo
    - [ ] A IA do jogo deve fornecer uma análise detalhada do desempenho dos jogadores e do time após cada partida.
    - [ ] Com base nessa análise, a IA deve sugerir mudanças táticas ou de treinamento para melhorar o desempenho futuro da equipe.
3. [ ] Sistema de Recomendação de Jogadores
    - [ ] A IA do jogo deve sugerir jogadores para contratação com base nas necessidades do time e no desempenho histórico dos jogadores.
4. [ ] Simulação de jogo aprimorada pela IA
    - [ ] A IA deve considerar não apenas as habilidades individuais dos jogadores, mas também a química da equipe, a forma física dos jogadores e as condições de jogo (por exemplo, se estão jogando em casa ou fora de casa, se é uma fase eliminatória ou se está perdendo ou se é um campeonato importante ou só um amistoso). 
    - [ ] A IA deve reagir de forma inteligente às ações dos jogadores humanos, e às mudandas na dinâmica do jogo. Por exemplo alterações de jogadores e da tática de jogo. 
5. [ ] Simulação aprimorada de bilheteria
    - [ ] A IA deve simular a quantidade de espectadores no estádio com base na capacidade, preço, performance recente do time e importância do campeonato, bem como ao histórico de espectadores.
     - [ ] Para times reais, a IA deve considerar o histórico de público real de jogos reais para poder 


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