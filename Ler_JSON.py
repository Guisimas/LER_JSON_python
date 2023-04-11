# Importando biblioteca

import os
import pandas as pd
import pyodbc as pyodbc

# import pyodbc

# Criando variaveis
file = []
aux = []
aux2 = []
ins = []
bv = []
table = 0


# Conexao com o banco de dados
def conect_db(Driver, Server, DataBase, Username, Password):
    dados_cone = 'Driver={' + Driver + '};SERVER=' + Server + ';DATABASE=' + DataBase + ';Trusted_Connection=yes;UID=' + Username + ';PWD={' + Password + '}'

    conexao = pyodbc.connect(dados_cone)

    return conexao.cursor()


# pegar nome de todos os arquivos de uma determinada pastas
def ler_arquivos(path):
    file = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.json')]

    return file


# alterar tabela adicionando colunas
def insere_colunas(nomeTabela):
    for y in range(len(dt.columns)):
        if y < len(dt.columns) - 1:
            at = f"""ALTER TABLE dbo.{nomeTabela}
            ADD {aux[y + 1]} VARCHAR(8000)"""
            cursor.execute(at)
            cursor.commit()

    return print(f'tabela {nomeTabela} criada inserido {y + 1} colunas')


# criando insert e inserindo na tabela
def insert():
    #limpa array
    ins.clear()
    for n in range(len(aux2)):
        for tr in range(len(dt.columns)):
            tu = f'{aux2[n][tr]}'
            tn = tu.replace("'", " ")
            bv.append(tn)
        op = f'{a} {aux}'
        dr = op.replace("'", "")
        p = f'{dr} {b} {bv})'
        k = p.replace("[", "")
        l = k.replace("]", "")
        bv.clear()
        ins.append(l)

    for x in range(len(aux2)):
        it = ins[x]
        cursor.execute(it)
        cursor.commit()

    return print(f'inserido {x + 1} registros na tabela')


# armagena os nomes dos arquivos
print('Programa iniciado')
pasta = 'C:\\Nova pasta'
arq = ler_arquivos(pasta)

# Conectando com banco de dados
cursor = conect_db('SQL Server', '186.286.7.00', 'DW_AUX', 'guilherme_simas_ti', '*******************')

# inicia repeticao de leitura e insercao no banco
for table in range(len(arq)):
    # Limpa vetor
    aux.clear()
    aux2.clear()

    # le arquivo na pasta
    df = pd.read_json(fr'{pasta}\\{arq[table]}')

    # normalizando e realizando tratativas de dados nulos
    da = pd.DataFrame(df)
    dt = da.fillna("")

    # verifica se tem informação na tabela
    if dt.empty == False:

        # contar colunas da tabela e colocando em um vetor o nome das colunas
        for i in range(len(dt.columns)):
            aux.append(dt.columns[i])

        # conta as linhas e colocando as informações em um vertor
        for f in range(len(dt.to_numpy())):
            at = dt.iloc[f]
            aux2.append(at.to_numpy())

        # criando comandos SQL
        a = f"""INSERT INTO {arq[table].replace(".json", "")} ("""
        b = """) VALUES ("""
        c = f"""CREATE TABLE {arq[table].replace(".json", "")}({aux[0]} VARCHAR(8000))"""
        d = f"""DROP TABLE {arq[table].replace(".json", "")}"""

        try:

            # dropando tabela se existente
            cursor.execute(d)
        except pyodbc.ProgrammingError as erro:
            # criando tabela
            cursor.execute(c)
            cursor.commit()

            # insere_colunas na tabela
            insere_colunas(arq[table].replace(".json", ""))

            # chamando insert e inserindo registros na tabela

            insert()

        else:
            cursor.commit()

            # criando tabela
            cursor.execute(c)
            cursor.commit()

            # insere_colunas na tabela
            insere_colunas(arq[table].replace(".json", ""))

            # chamando insert e inserindo registros na tabela
            insert()

    else:
        print('não a dados')

print(f'foram criadas {table + 1} tabelas')
