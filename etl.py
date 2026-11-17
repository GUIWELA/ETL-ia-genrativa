import pandas as pd 

df = pd.read_csv("clientes.csv", skipinitialspace=True)

def gerar_mensagem(nome):
    return f"Olá {nome}, invista hoje e projete o seu futuro financeiro!"

df["Mensagem"] = df ["Nome"].apply(gerar_mensagem)

print(df)

df.to_csv("clientes_com_mensagem.csv", index=False)