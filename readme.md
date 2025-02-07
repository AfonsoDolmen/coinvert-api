# Coinvert API

## Sobre o Projeto

O Coinvert API é uma aplicação desenvolvida com FastAPI que permite a conversão de uma moeda para várias outras. A API foi integrada à Alpha Vantage para fornecer cotações de moedas de forma precisa e atualizada.

## Funcionalidades

- Conversão de moedas em tempo real.
- Processamento assíncrono para requisições rápidas e eficientes.
- Integração com a API da Alpha Vantage.

## Tecnologias Utilizadas

- **FastAPI:** Framework moderno e eficiente para desenvolvimento de APIs.
- **Alpha Vantage API:** Fonte externa para dados de cotação de moedas.

## Como Executar o Projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/coinvert-api.git
   cd coinvert-api
   ```

2. Crie um ambiente virtual e ative

    **Linux / MacOS**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

    **Windows**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. Instale as dependências
    ```bash
    pip install -r requirements.txt
    ```

4. Incie o servidor
    ```bash
    python .\main.py
    ```

    Acesse a documentação interativa em http://localhost:8000/docs

## Conclusão

O desenvolvimento do Coinvert API consolidou meu aprendizado com FastAPI e mostrou as diversas possibilidades ao integrar APIs externas. Espero que este projeto seja úteis para estudos e aprimoramento em desenvolvimento backend.