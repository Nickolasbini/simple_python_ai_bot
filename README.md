# Primeira IA em Python 🐍🤖

Projeto de exemplo do vídeo **"Minha Primeira IA em Python"** - Código Prático.

Script simples em Python que se conecta a uma IA gratuita via [OpenRouter](https://openrouter.ai), ideal para quem está vindo de JavaScript/Node.js e quer dar os primeiros passos em Python.

## 📋 Pré-requisitos

- Python 3.10 ou superior instalado ([python.org/downloads](https://www.python.org/downloads/))
- Uma chave gratuita da API da [OpenRouter](https://openrouter.ai/keys)

## 🚀 Como rodar

1. Clone o repositório e entre na pasta:
```bash
git clone https://github.com/Nickolasbini/primeira_ia_python.git
cd primeira_ia_python
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Copie o arquivo de exemplo de variáveis de ambiente e cole sua chave:
```bash
copy .env.example .env
```
Depois abra o `.env` e cole sua chave da OpenRouter.

5. Rode os scripts:
```bash
python samples.py
python simple_ai.py
```

## 📁 Estrutura

```
primeira_ia_python/
├── samples.py           # Primeiros conceitos de Python (variáveis, listas, print)
├── simple_ai.py         # ChatBot com Ai
├── requirements.txt     # Dependências do projeto
├── .env.example         # Modelo do arquivo de variáveis de ambiente
└── README.md
```

## 🔗 Links

- Vídeo completo: [Minha Primeira IA em Python](https://youtu.be/2h422QJaq3M)
- Canal: [Código Prático](https://www.youtube.com/@codigopraticooficial)
- Agência: [Cervo Digital](https://cervodigital.com.br)
