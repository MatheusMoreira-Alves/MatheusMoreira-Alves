from src.database.connection import connect

# Salva o DataFrame em uma tabela do banco de dados;
def save_to_database(df, database):

    # Obtém uma conexão com o banco de dados;
    database = connect()

    # Obtém os nomes das colunas do DataFrame;
    columns = list(df.columns)

    # Monta a string de criação da tabela, substituindo os nomes das colunas;
    string_creation_table = 'CREATE TABLE microdados_filtrados ('
    string_creation_table += ', '.join([column +
                                       ' TEXT' for column in columns])
    string_creation_table += ')'

    cur = database.cursor()
    cur.execute('DROP TABLE IF EXISTS microdados_filtrados')

    # Executa a query de criação da tabela;
    cur.execute(string_creation_table)

    # Insere os dados do DataFrame na tabela;
    for row in df.itertuples():
        values = tuple(row[1:])
        cur.execute(
            'INSERT INTO microdados_filtrados VALUES {}'.format(values))

    # Realiza o push das alterações no banco de dados;
    database.commit()

    # Fecha a conexão com o banco de dados;
    database.close()
