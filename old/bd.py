import sqlite3

# Conectar ao banco de dados (cria o arquivo se não existir)
conn = sqlite3.connect('times.db')
cursor = conn.cursor()

# Criar tabela de times se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS times
             (id INTEGER PRIMARY KEY, nome TEXT, pontos INTEGER, saldo_gols INTEGER)''')

# Exemplo de leitura de todos os times
cursor.execute("SELECT * FROM times")
times = cursor.fetchall()
for time in times:
    print(time)

# Fechar conexão com o banco de dados
conn.close()
