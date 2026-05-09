# GoDJE

Aplicativo Streamlit para visualizar o Diário da Justiça Eletrônico (DJE) do Tribunal de Justiça de Roraima (TJRR).

## Descrição

Este app acessa o site oficial do DJE (diario.tjrr.jus.br) e permite visualizar PDFs do DJE de forma moderna e intuitiva:
- **DJE Disponível**: Automaticamente mostra o DJE do dia atual, ou o mais recente se não houver.
- **Buscar Data Específica**: Permite escolher uma data manualmente via seletor.

A interface utiliza cards modernos para uma experiência visual aprimorada. O PDF é visualizado externamente via link, sem exibição inline.

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

- **Verificação de Disponibilidade**: Usa requisições HEAD para checar se o PDF existe sem baixar o conteúdo.
- **Busca Automática**: Prioriza o dia atual; se indisponível, busca o mais recente nos últimos 30 dias.
- **Seleção Manual**: Permite escolher qualquer data passada e verifica disponibilidade.
- **Visualização**: Botão "VISUALIZAR DJE" abre o PDF em uma nova aba do navegador.
- **Interface Moderna**: Utiliza CSS customizado para cards com sombras e bordas arredondadas.