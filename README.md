# GoDJE

Aplicativo Streamlit para visualizar o Diário da Justiça Eletrônico (DJE) do Tribunal de Justiça de Roraima (TJRR).

## Descrição

Este app acessa o site oficial do DJE (diario.tjrr.jus.br) e permite buscar e visualizar PDFs do DJE de diferentes formas:
- **Dia atual**: Busca o DJE da data corrente.
- **Mais recente disponível**: Encontra automaticamente o último DJE publicado (nos últimos 30 dias).
- **Selecionar data específica**: Permite escolher uma data manualmente via seletor.

Se o DJE estiver disponível, ele é exibido inline na página e oferece uma opção de download.

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

- Para "Dia atual" ou "Selecionar data específica": Constrói a URL do PDF no formato `https://diario.tjrr.jus.br/dpj/dpj-YYYYMMDD.pdf` e faz download.
- Para "Mais recente disponível": Inicia da data atual e decrementa dia a dia até encontrar um PDF disponível (limite de 30 dias para trás).
- Exibe o PDF usando um iframe HTML embutido e oferece botão de download.
- Trata erros de rede e status HTTP não-200 com mensagens apropriadas.