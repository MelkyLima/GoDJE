# GoDJE

Aplicativo Streamlit para visualizar o Diário da Justiça Eletrônico (DJE) do dia atual do Tribunal de Justiça de Roraima (TJRR).

## Descrição

Este app acessa o site oficial do DJE (diario.tjrr.jus.br) e busca o PDF correspondente à data atual. Se o DJE estiver disponível, ele é exibido inline na página e oferece uma opção de download.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas: Streamlit, Requests

## Instalação e Execução

1. Clone ou baixe os arquivos do projeto.
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Execute o aplicativo:
   ```
   streamlit run app.py
   ```

O app será aberto no navegador padrão.

## Funcionamento Técnico

- Obtém a data atual usando `datetime.now()`.
- Constrói a URL do PDF no formato: `https://diario.tjrr.jus.br/dpj/dpj-YYYYMMDD.pdf`
- Faz uma requisição GET para baixar o PDF.
- Se bem-sucedido (status 200), exibe o PDF usando um iframe HTML e oferece download.
- Caso contrário, mostra uma mensagem de erro.

## Notas

- O site do TJRR pode não ter DJE para todos os dias (feriados, fins de semana, etc.).
- Certifique-se de ter uma conexão com a internet para acessar o site.