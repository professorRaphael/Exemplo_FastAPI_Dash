from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random

app = FastAPI(title="API de Dados para o Dash")

class Venda(BaseModel):
    mes: str
    valor: float

# Dados simulados (no seu projeto original, isso viria de um CSV ou Banco)
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

@app.get("/dados-vendas", response_model=List[Venda])
async def obter_vendas():
    """Retorna dados de vendas simulados."""
    # Gerando dados aleatórios para o exemplo
    dados = [{"mes": m, "valor": random.uniform(1000, 5000)} for m in meses]
    return dados