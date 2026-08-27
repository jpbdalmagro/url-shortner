# URL Shortener API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.12" />
  <img src="https://img.shields.io/badge/FastAPI-0.141-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" />
  <img src="https://img.shields.io/badge/SQLite-3-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Pydantic-2.13-E92063?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic" />
</p>

Aplicação web completa para **encurtamento de links** e **rastreamento de métricas de acesso**, desenvolvida com arquitetura modular em **Python**, utilizando o framework **FastAPI**, persistência relacional com **SQLAlchemy** e interface de usuário integrada em Vanilla HTML/CSS.

Este projeto foi concebido para compor portfólio técnico, demonstrando boas práticas de desenvolvimento de APIs RESTful, separação de responsabilidades em camadas, validação estrita de dados e integração frontend-backend.

---

## Funcionalidades

- **Encurtamento de URLs:** Geração de códigos alfanuméricos curtos e aleatórios de 6 caracteres.
- **Prevenção de Duplicidade:** Reutilização automática de códigos caso a mesma URL longa já tenha sido cadastrada anteriormente.
- **Redirecionamento HTTP:** Resolução do código encurtado com redirecionamento automático (`302 Found`).
- **Métricas de Uso:** Contagem em tempo real de acessos por link.
- **Auditoria de Acessos:** Registro detalhado de histórico com data/hora, endereço IP de origem e `User-Agent`.
- **Interface Web Integrada:** Painel responsivo em tema *Dark Glassmorphism* com feedback visual e cópia para a área de transferência em um clique.
- **Documentação Interativa:** Geração automática de documentação via Swagger UI (`/docs`) e ReDoc (`/redoc`).

---

## Tecnologias e Ferramentas

| Componente | Tecnologia | Finalidade |
| :--- | :--- | :--- |
| **Backend Framework** | FastAPI | Construção de endpoints assíncronos e roteamento |
| **Linguagem** | Python 3.12+ | Lógica de negócio e manipulação de dados |
| **Servidor ASGI** | Uvicorn | Execução e gerenciamento de processos da aplicação |
| **ORM** | SQLAlchemy 2.0 | Modelagem e mapeamento objeto-relacional |
| **Banco de Dados** | SQLite | Armazenamento relacional local |
| **Validação e Tipagem** | Pydantic v2 | Schemas de entrada, saída e validação de URLs |
| **Frontend** | HTML5, CSS3, JavaScript (Fetch API) | Interface de usuário sem dependências externas |

---

## Uso de Inteligência Artificial no Desenvolvimento

Com o objetivo de manter a transparência profissional em projetos de portfólio, documenta-se a utilização de ferramentas de Inteligência Artificial generativa nas seguintes etapas do ciclo de vida do software:

1. **Mentoria e Pair Programming na API:**
   - Apoio na discussão e definição da arquitetura em camadas (`routers`, `schemas`, `database`, `core`).
   - Resolução de dúvidas conceituais sobre o ciclo de vida do SQLAlchemy, injeção de dependências (`Depends(get_db)`) e prevenção de erros de roteamento (tratamento de rotas com parâmetros dinâmicos vs. rotas estáticas).

2. **Desenvolvimento da Interface Web (Frontend):**
   - Prototipação conceitual e geração do código da interface em página única (`index.html`), aplicando estética moderna com CSS puro (*Glassmorphism*, animações fluidas e suporte a responsividade).
   - Criação do favicon vetorial (`favicon.svg`) personalizado para o projeto.

3. **Documentação Técnica:**
   - Estruturação e redação deste documento (`README.md`), garantindo clareza técnica e padronização para apresentação em portfólio.

---

## Estrutura do Projeto

```text
url-shortener/
├── app/
│   ├── core/
│   │   └── utils.py          # Utilitários de geração de códigos alfanuméricos
│   ├── database/
│   │   ├── connection.py     # Inicialização da engine e gerenciamento de sessões do SQLite
│   │   └── models.py         # Entidades relacionais (URLItem e AccessLog)
│   ├── routers/
│   │   ├── redirect.py       # Rota pública de resolução e redirecionamento (/{short_code})
│   │   └── url.py            # Endpoints da API para criação e consulta (/urls/)
│   ├── schemas/
│   │   └── schemas.py        # Schemas de validação e serialização Pydantic
│   ├── static/
│   │   ├── favicon.svg       # Favicon vetorial da aplicação
│   │   └── index.html        # Interface de usuário SPA (Single Page Application)
│   └── app.py                # Ponto de entrada, montagem de arquivos estáticos e rotas
├── requirements.txt          # Dependências do projeto
├── .gitignore                # Arquivos e pastas ignorados pelo controle de versão
└── README.md                 # Documentação do repositório
```

---

## Como Executar Localmente

### Pré-requisitos
- Python 3.10 ou superior
- Gerenciador de pacotes `pip`

### 1. Clonar o Repositório
```bash
git clone https://github.com/jpbdalmagro/url-shortner.git
cd url-shortener
```

### 2. Configurar o Ambiente Virtual
```bash
# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
# No Linux/macOS:
source venv/bin/activate

# No Windows:
.\venv\Scripts\activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar o Servidor
```bash
uvicorn app.app:app --reload
```

A aplicação estará acessível nos seguintes endereços:
- **Interface Web:** [http://localhost:8000](http://localhost:8000)
- **Documentação Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Documentação ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Endpoints da API

### Tabela de Rotas

| Método | Endpoint | Descrição | Status HTTP |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Serve a interface web | `200 OK` |
| `POST` | `/urls/` | Cria ou recupera um link encurtado | `201 Created` |
| `GET` | `/{short_code}` | Redireciona para o destino e registra log de acesso | `302 Found` |
| `GET` | `/urls/{short_code}/stats` | Retorna contagem de cliques e metadados | `200 OK` |
| `GET` | `/favicon.ico` | Serve o ícone da aplicação | `200 OK` |

---

### Exemplos de Requisições

#### Encurtar uma URL
- **Endpoint:** `POST /urls/`
- **Corpo da Requisição:**
```json
{
  "url": "https://fastapi.tiangolo.com/tutorial/bigger-applications/"
}
```
- **Resposta (`201 Created`):**
```json
{
  "original_url": "https://fastapi.tiangolo.com/tutorial/bigger-applications/",
  "short_code": "a8B2xK",
  "short_url": "http://localhost:8000/a8B2xK",
  "created_at": "2026-08-26T21:00:00.000000"
}
```

#### Consultar Estatísticas de um Link
- **Endpoint:** `GET /urls/a8B2xK/stats`
- **Resposta (`200 OK`):**
```json
{
  "original_url": "https://fastapi.tiangolo.com/tutorial/bigger-applications/",
  "clicks": 5,
  "created_at": "2026-08-26T21:00:00.000000"
}
```

---

## Licença

Este projeto está sob a licença [MIT](LICENSE).
