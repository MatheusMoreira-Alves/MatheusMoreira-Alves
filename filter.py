# Filtra o DataFrame para manter apenas os valores que é necessário para a inserção no banco de dados;
def filter_dataframe(df):

    print('Filtrando as linhas por município...')
    df = df.loc[df['Municipio'] == 'CARIACICA'].copy()

    print('Preenchendo os valores NaN...')
    df.fillna('', inplace=True)

    print('Filtrando as linhas por data de óbito...')
    df = df.loc[df['DataObito'] != ''].copy()

    print('Filtrando as linhas por comorbidade de tabagismo...')
    df = df.loc[df['ComorbidadeTabagismo'] == 'Sim'].copy()

    print('Filtrando as linhas por óbito causado pelo COVID-19...')
    df = df.loc[df['Evolucao'] == 'Óbito pelo COVID-19'].copy()

    print('Redefinindo o índice do DataFrame...')
    df.reset_index(drop=True, inplace=True)

    return df
