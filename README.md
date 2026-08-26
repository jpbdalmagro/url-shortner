# 🔗 URL Shortener API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic" />
</p>

Uma API REST simples, rápida e eficiente para **encurtamento de links** e **rastreamento de acessos**, desenvolvida em Python com **FastAPI** e **SQLAlchemy**.

Este projeto foi construído para servir como base de portfólio, demonstrando conceitos essenciais de arquitetura modular, persistência de dados em banco relacional, validação de requisições e documentação automática de endpoints.

---

## ✨ Funcionalidades

- ✂️ **Encurtamento de URLs:** Gera códigos alfanuméricos curtos e únicos de 6 caracteres.
- 🚀 **Redirecionamento Automático:** Redireciona o usuário para a URL original com status HTTP `302 Found`.
- 📊 **Contador de Cliques:** Registra a quantidade total de acessos de cada link encurtado.
- 🕵️ **Logs de Acesso:** Salva histórico detalhado de cada clique, incluindo IP e `User-Agent`.
- 🛡️ **Validação de Dados:** Validação estrita de formato de URLs com Pydantic (`HttpUrl`).
- 📖 **Documentação Interativa:** Interface Swagger UI (`/docs`) e ReDoc (`/redoc`) prontas para testes.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** [Python 3.12+](https://www.python.org/)
* **Framework Web:** [FastAPI](https://fastapi.tiangolo.com/)
* **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Banco de Dados:** [SQLite](https://www.sqlite.org/) (leve e sem necessidade de configuração externa)
* **Validação & Serialização:** [Pydantic v2](https://docs.pydantic.dev/)

---

## 📁 Estrutura do Projeto

```text
url-shortener/
├── app/
│   ├── core/
│   │   └── utils.py          # Gerador de códigos curtos aleatórios
│   ├── database/
│   │   ├── connection.py     # Configuração da engine SQLite e SessionLocal
│   │   └── models.py         # Modelos de banco (URLItem e AccessLog)
│   ├── routers/
│   │   ├── redirect.py       # Rota pública de redirecionamento (/{short_code})
│   │   └── url.py            # Rotas da API (/urls/ e /urls/{short_code}/stats)
│   ├── schemas/
│   │   └── schemas.py        # Schemas Pydantic para validação e resposta
│   └── main.py               # Inicialização da aplicação e registro de rotas
├── requirements.txt          # Dependências do projeto
├── .gitignore
└── README.md
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.10 ou superior instalado.
- `pip` e `venv`.

### 1. Clonar o Repositório
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd url-shortener
```

### 2. Criar e Ativar o Ambiente Virtual
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows (Prompt / PowerShell)
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Iniciar o Servidor
```bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em `http://localhost:8000`.

---

## 📍 Endpoints da API

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `POST` | `/urls/` | Encurta uma URL longa |
| `GET` | `/{short_code}` | Redireciona para o link original e registra log |
| `GET` | `/urls/{short_code}/stats` | Retorna o total de cliques e dados do link |
| `GET` | `/docs` | Documentação interativa (Swagger UI) |
| `GET` | `/` | Health check da API |

---

### 📝 Exemplos de Uso

#### 1. Encurtar um Link
**Requisição:**
`POST /urls/`
```json
{
  "url": "https://www.google.com/search?q=fastapi"
}
```

**Resposta (`201 Created`):**
```json
{
  "original_url": "https://www.google.com/search?q=fastapi",
  "short_code": "k8X2aQ",
  "short_url": "http://localhost:8000/k8X2aQ",
  "created_at": "2026-08-26T14:55:00.000000"
}
```

#### 2. Consultar Estatísticas
**Requisição:**
`GET /urls/k8X2aQ/stats`

**Resposta (`200 OK`):**
```json
{
  "original_url": "https://www.google.com/search?q=fastapi",
  "clicks": 14,
  "created_at": "2026-08-26T14:55:00.000000"
}
```

---

## 📄 Licença

Distribuído sob a licença **MIT**. Veja `LICENSE` para mais informações.

---

<p align="center">
  Desenvolvido com ☕ e Python.
</p>
