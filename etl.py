from google import genai

client = genai.Client()

import pandas as pd 

df = pd.read_csv("clientes.csv", skipinitialspace=True)

def gerar_mensagem(nome):
   resposta = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=f"Escreve uma mensagem curta (máximo 100 caracteres) para {nome}, cliente de um banco, sobre a importância de investir",
   )
   return resposta.text.strip()

df["Mensagem"] = df ["Nome"].apply(gerar_mensagem)

print(df)

df.to_csv("clientes_com_mensagem.csv", index=False)