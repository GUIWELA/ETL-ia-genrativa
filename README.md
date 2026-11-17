# ETL com IA Generativa

Pipeline ETL em Python que lê clientes de um CSV, gera uma mensagem personalizada para cada um e guarda o resultado num novo ficheiro.

## Como funciona

- **Extração**: leitura do 'clientes.csv' com pandas
- **Transformação**: criação de uma mensagem por cliente
- **Carregamento**: gravação em 'clientes_com_mensagem.csv'

## Como correr

    pip install pandas
    python etl.py
