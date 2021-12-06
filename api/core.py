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


def uber (qualquercoisa):
    meuFile = pd.read_excel(qualquercoisa, engine='openpyxl')
    df_data = pd.DataFrame(data=meuFile)
    df_data.drop(df_data[df_data.Data == "TOTAL"].index, inplace=True)
    df_data.drop(df_data[df_data.Data == "MÊS TOTAL"].index, inplace=True)
    df_data.drop(df_data[df_data.Data.isnull()].index, inplace=True)
    variavel = df_data.groupby(pd.Grouper(key='Data',freq='M')).sum()
    variavel['Percentual'] = ((variavel['Ganhos do Dia'] - variavel['R$ Combustivel']) * 100) / variavel['R$ Combustivel']
    variavel = variavel[['Percentual']]
    variavel['Mes'] = variavel.index[:].month_name()
    variavel['Ano'] = variavel.index[:].year
    
    return(variavel)


def identificar (nomedoarquivo):
    cabecalhoUber = ['Data', 'Ganhos do Dia', 'km', 'corridas', 'R$  litro', 'R$ Combustivel', 'Lucro dia', 'Horas']
    cabecalhoML = ['N° NF-e', 'Data da tarifa', 'Número da tarifa', 'Detalhe', 'Descontado da operação', 'Status da tarifa', 'Tarifa estornada', 'Valor da tarifa', 'Valor da tarifa sem desconto', 'Valor del descuento', 'Motivo', 'Número de venda', 'Pagamento', 'Data de venda', 'Canal de vendas', 'Cliente', 'Quantidade vendida', 'Preço unitário', 'Valor da transação', 'Número de envio', 'Número da embalagem', 'Envio por conta do cliente', 'Número do anúncio', 'Título do anúncio', 'Tipo do anúncio', 'Categoria do anúncio', 'Código ML']

    meuFile = pd.read_excel(nomedoarquivo, engine='openpyxl')
    df_data = pd.DataFrame(data=meuFile)
    if (df_data.columns.values.tolist() == cabecalhoUber):
        print("lista do uber")
    else:
        if ((len(df_data.index)) > 5):
            if (df_data.loc[6].values.tolist() == cabecalhoML):
                print("Lista do ML")
            else:
                print("Lista personalizada")
        else:
            print("Lista personalizada")
            
    return df_data.columns.values
