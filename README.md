# 📊 Dashboard Multi-Paradigma: FastAPI + Dash

> **⚠️ Aviso Acadêmico:** Este é um projeto de cunho estritamente educacional, desenvolvido como material de apoio prático para turmas de Pós-Graduação. O objetivo é demonstrar conceitos arquiteturais e integração de tecnologias. **Não** é um código voltado para produção (carece de autenticação, testes automatizados e deploy configurado).

## 🎯 Sobre o Projeto
Este repositório demonstra a evolução de uma arquitetura web em Python. Ele substitui a abordagem tradicional (Flask + Streamlit) por uma stack mais moderna e performática, separando claramente o backend e o frontend:

1. **Backend (`api.py`):** Construído com **FastAPI**, servindo dados de forma rápida e com documentação automática (Swagger).
2. **Frontend (`dashboard.py`):** Construído com **Dash (Plotly)**, consumindo a API e gerando visualizações interativas e reativas baseadas em *callbacks*.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **FastAPI** & **Uvicorn** (Servidor Web ASGI)
* **Dash** & **Plotly** (Criação de interfaces web e gráficos)
* **Pandas** (Manipulação de dados)
* **Requests** (Consumo da API)

---

## 🚀 Como Executar Localmente

Para ver este projeto funcionando, você precisará rodar o Backend e o Frontend simultaneamente (em dois terminais separados).

### 1. Instale as dependências
Certifique-se de estar usando um ambiente virtual (venv) e instale os pacotes necessários:
```bash
pip install fastapi uvicorn dash pandas requests
```

### 2. Inicie a API (Terminal 1)
Navegue até a pasta do projeto e inicie o servidor do FastAPI:
```bash
uvicorn api:app --reload
```
*A API estará rodando em: `http://127.0.0.1:8000`*
*(Acesse `http://127.0.0.1:8000/docs` para ver a documentação interativa).*

### 3. Inicie o Dashboard (Terminal 2)
Abra uma **nova aba ou janela** no seu terminal, ative o ambiente virtual (se estiver usando) e rode a interface do Dash:
```bash
python dashboard.py
```
*O Dashboard estará acessível no seu navegador em: `http://127.0.0.1:8050`*

---
*Desenvolvido pelo Prof. Raphael para fins didáticos.*
