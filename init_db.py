import sqlite3

conn = sqlite3.connect("database/fys.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS padarias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    bairro TEXT,
    vende_refrigerante INTEGER,
    vende_salgados INTEGER,
    fluxo INTEGER,
    espaco INTEGER,
    score INTEGER,
    recomendacao TEXT
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")