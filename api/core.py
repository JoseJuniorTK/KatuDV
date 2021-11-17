import pandas as pd

def mercadolivre(filename):

    my_file = pd.read_excel(filename, engine='openpyxl')
    df_data = pd.DataFrame(data=my_file)
    df_data.columns = df_data.iloc[6]
    df_data.drop(df_data.index[[0, 1, 2, 3, 4, 5, 6]], inplace=True)
    teste = df_data.drop_duplicates(subset=['Número de venda'])
    vendas = teste.groupby('Título do anúncio').size().reset_index(name='Q. de vendas')
    vendas = vendas.rename({'Título do anúncio': 'Info1', 'Q. de vendas': 'Info2'}, axis=1)
    dfd3 = vendas

    return dfd3
