# Script Unificador de Código para Projetos Unity

Este é um script Python de utilidade projetado para desenvolvedores Unity. Sua principal função é varrer a pasta `Assets` de um projeto, encontrar todos os scripts C# (`.cs`), e consolidá-los em um único arquivo de texto (`.txt`).

O objetivo é facilitar a revisão de código, a análise de projetos e, principalmente, a entrada de múltiplos scripts em ferramentas de Inteligência Artificial que possuem limite de arquivos por vez.

## Funcionalidades

* **Busca Recursiva:** O script pesquisa todos os arquivos `.cs` dentro da pasta `Assets` e de todas as suas subpastas.
* **Arquivo de Saída Único e Versionado:** Consolida todos os scripts encontrados em um único arquivo `.txt`, criando uma nova versão a cada execução (ex: `AllScripts0001.txt`, `AllScripts0002.txt`) para não sobrescrever o histórico.
* **Índice Automático:** Gera um índice numerado e em ordem alfabética no início do arquivo de saída, listando todos os scripts que foram incluídos.
* **Delimitadores Claros:** Cada script no arquivo final é encapsulado com marcadores de início e fim para fácil identificação (ex: `----- Início Script "MeuScript.cs" -----`).
* **Tratamento de Codificação:** Possui um sistema de fallback para ler arquivos salvos em diferentes codificações de caracteres (UTF-8 e Latin-1), evitando erros de leitura comuns no Windows.

## Como Usar

1.  **Localização:** Salve o script `unificar_scripts_unity.py` na **pasta raiz** do seu projeto Unity.

    ```
    MeuProjetoUnity/
    ├── Assets/
    ├── Library/
    ├── ProjectSettings/
    └── unificar_scripts_unity.py   <-- SALVE O SCRIPT AQUI
    ```

2.  **Execução:** Dê um duplo clique no arquivo `unificar_scripts_unity.py`. Uma janela de terminal aparecerá brevemente para executar o processo.

3.  **Resultado:** Uma nova pasta chamada **`AllScripts_CS`** será criada na raiz do seu projeto. Dentro dela, você encontrará o arquivo `.txt` gerado com todos os scripts unificados.

## Pré-requisitos

* Python 3.x instalado no Windows.

## Personalização

O script possui variáveis de configuração no topo do arquivo que podem ser facilmente modificadas para alterar o nome da pasta de saída, o nome base do arquivo gerado, etc.

```python
# --- CONFIGURAÇÕES ---
PASTA_SAIDA = "AllScripts_CS"
NOME_BASE_ARQUIVO_SAIDA = "AllScripts"
PASTA_RAIZ_BUSCA = "Assets"
EXTENSAO_ALVO = "*.cs"
# ---------------------
