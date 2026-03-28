# dashboard.py
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import requests

app = Dash(__name__)

# URL da nossa API FastAPI
API_URL = "http://127.0.0.1:8000/dados-vendas"

# --- 1. LAYOUT (A "Cara" do Dashboard) ---
app.layout = html.Div(children=[
    html.H1(children='Dashboard Multi-Paradigma (Dash + FastAPI)', style={'textAlign': 'center'}),
    html.Div(children='Consumindo dados dinâmicos do backend via API.', style={'textAlign': 'center'}),
    # O componente dcc.Graph vai segurar o nosso gráfico do Plotly
    dcc.Graph(id='grafico-vendas'),
    # Um botão para atualizar os dados manualmente
    html.Button('Atualizar Dados', id='btn-atualizar', n_clicks=0, style={'display': 'block', 'margin': '20px auto'})
])


# --- 2. CALLBACKS (A "Lógica" de interatividade) ---
# Aqui dizemos: "Quando o botão for clicado (Input), atualize a figura do gráfico (Output)"
@app.callback(
    Output('grafico-vendas', 'figure'),
    Input('btn-atualizar', 'n_clicks')
)
def atualizar_grafico(n_clicks):
    try:
        # Faz a requisição para o nosso FastAPI
        resposta = requests.get(API_URL)
        resposta.raise_for_status() # Verifica se deu erro HTTP
        dados = resposta.json()
        
        # Converte para Pandas DataFrame
        df = pd.DataFrame(dados)
        
        # Cria o gráfico com Plotly Express
        fig = px.bar(df, x='mes', y='valor', 
                     title='Vendas por Mês',
                     labels={'mes': 'Mês', 'valor': 'Faturamento (R$)'},
                     color='valor',
                     color_continuous_scale='Viridis')
        return fig
        
    except requests.exceptions.RequestException as e:
        # Retorna um gráfico vazio com mensagem de erro se a API estiver fora
        return px.bar(title=f"Erro ao conectar com a API: {e}")

if __name__ == '__main__':
    app.run(debug=True, port=8050)