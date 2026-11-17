# ETL com IA Generativa

Pipeline ETL em Python que lê clientes de um CSV, gera uma mensagem personalizada para cada um e guarda o resultado num novo ficheiro.

## Como funciona

- **Extração**: leitura do 'clientes.csv' com pandas
- **Transformação**: criação de uma mensagem por cliente, usando o Google Gemini
- **Carregamento**: gravação em 'clientes_com_mensagem.csv'

## Como correr

1. Instala as bibliotecas:

    pip install pandas google-gemini

2. Cria uma chave google AI Studio e guarda-a numa variável de ambiente:

    $env:GEMINI_API_KEY="A_TUA_CHAVE"

3. Corre o programa:    
   
    python etl.py
