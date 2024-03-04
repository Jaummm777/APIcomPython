import requests
import pandas as pd
from datetime import datetime

api_token = "PRIVATE_TOKEN"

base_url = "https://api.tiny.com.br/api2/contas.receber.pesquisa.php"
start_date = datetime.strptime("09/10/2023", "%d/%m/%Y").strftime("%Y-%m-%d")
end_date = datetime.strptime("20/10/2024", "%d/%m/%Y").strftime("%Y-%m-%d")

all_contas_data = []

pagina_atual = 1
numero_paginas = 66


while pagina_atual <= numero_paginas:

    params = {
        'token': api_token,
        'formato': 'json',
        'data_ini_vencimento': start_date,
        'data_fim_vencimento': end_date,
        'pagina': pagina_atual
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:

        data = response.json()


        numero_paginas = data['retorno']['numero_paginas']


        contas_list = data['retorno']['contas']


        for conta in contas_list:
            all_contas_data.append(conta['conta'])

        pagina_atual += 1
    else:
        print(f"Erro ao buscar dados na página {pagina_atual}: {response.status_code}")
        break


df = pd.DataFrame(all_contas_data)


df.to_csv('contas_a_receber_completo.csv', index=False)

print(
    f"Dados importados e salvos com sucesso no arquivo 'contas_a_receber_completo.csv'. Total de páginas processadas: {pagina_atual - 1}")