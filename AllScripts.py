import os
import glob
import re

# --- CONFIGURAÇÕES ---
# Pasta onde os arquivos unificados serão salvos. Será criada na raiz do projeto.
PASTA_SAIDA = "AllScripts_CS"

# O nome base para os arquivos de saída versionados.
NOME_BASE_ARQUIVO_SAIDA = "AllScripts"

# Pasta raiz onde a busca por scripts .cs será feita.
PASTA_RAIZ_BUSCA = "Assets"

# Extensão dos arquivos a serem encontrados.
EXTENSAO_ALVO = "*.cs"
# ---------------------

def obter_proximo_numero_versao(diretorio, base_nome):
    """
    Verifica o diretório de saída para encontrar o número da última versão
    e retorna o próximo número de versão a ser usado.
    """
    os.makedirs(diretorio, exist_ok=True)
    numeros_versao = [0]
    padrao = re.compile(f"^{re.escape(base_nome)}(\\d{{4}})\\.txt$")
    
    for nome_arquivo in os.listdir(diretorio):
        match = padrao.match(nome_arquivo)
        if match:
            numeros_versao.append(int(match.group(1)))
            
    proximo_numero = max(numeros_versao) + 1
    return proximo_numero

def unificar_scripts_recursivo():
    """
    Busca recursivamente todos os arquivos .cs dentro da pasta 'Assets',
    lê seu conteúdo e os une em um único arquivo de saída versionado.
    """
    # Define o caminho de busca para encontrar .cs em 'Assets' e subpastas.
    # O padrão '/**/' é o que ativa a busca recursiva.
    caminho_busca = os.path.join(PASTA_RAIZ_BUSCA, '**', EXTENSAO_ALVO)
    
    # Executa a busca e obtém uma lista de caminhos completos (ex: 'Assets/Scripts/Player.cs')
    arquivos_cs_com_caminho = glob.glob(caminho_busca, recursive=True)

    if not arquivos_cs_com_caminho:
        print(f"Nenhum arquivo .cs encontrado dentro da pasta '{PASTA_RAIZ_BUSCA}'.")
        print("Certifique-se de que este script está na pasta raiz do seu projeto Unity.")
        input("Pressione Enter para sair...")
        return

    # Ordena a lista de arquivos em ordem alfabética pelo caminho completo.
    arquivos_cs_com_caminho.sort()

    # Obtém o nome do arquivo de saída versionado.
    numero_versao = obter_proximo_numero_versao(PASTA_SAIDA, NOME_BASE_ARQUIVO_SAIDA)
    nome_arquivo_saida = f"{NOME_BASE_ARQUIVO_SAIDA}{numero_versao:04d}.txt"
    caminho_completo_saida = os.path.join(PASTA_SAIDA, nome_arquivo_saida)

    # Abre o arquivo de saída para escrita.
    with open(caminho_completo_saida, 'w', encoding='utf-8') as arquivo_saida:
        # --- 1. CABEÇALHO COM A LISTA DE ARQUIVOS ---
        arquivo_saida.write("="*80 + "\n")
        arquivo_saida.write("ÍNDICE DE SCRIPTS C# COMPILADOS (do projeto Unity)\n")
        arquivo_saida.write("="*80 + "\n\n")
        
        for i, caminho_completo in enumerate(arquivos_cs_com_caminho):
            # Extrai apenas o nome base do arquivo (ex: 'Player.cs') do caminho completo.
            nome_arquivo_base = os.path.basename(caminho_completo)
            arquivo_saida.write(f"{i+1}. {nome_arquivo_base}\n")
            
        arquivo_saida.write("\n\n")
        
        # --- 2. INSTRUÇÃO DE LEITURA (mesma de antes) ---
        arquivo_saida.write("="*80 + "\n")
        arquivo_saida.write("INSTRUÇÕES DE LEITURA\n")
        arquivo_saida.write("="*80 + "\n\n")
        texto_instrucao = (
            "Cada script individual está separado pelas marcações abaixo. "
            "Cada separação representa um script individual e deve ser tratada dessa forma quando a leitura for feita.\n\n"
        )
        arquivo_saida.write(texto_instrucao)
        arquivo_saida.write('----- Início Script "NomeDoScript.cs" -----\n')
        arquivo_saida.write("... conteúdo do script C# ...\n")
        arquivo_saida.write('----- Final Script "NomeDoScript.cs" -----\n\n')
        arquivo_saida.write("="*80 + "\n\n\n")

        # --- 3. CONTEÚDO DOS ARQUIVOS ---
        for caminho_arquivo_entrada in arquivos_cs_com_caminho:
            # Extrai o nome base novamente para usar nos marcadores.
            nome_arquivo_base = os.path.basename(caminho_arquivo_entrada)
            
            arquivo_saida.write(f'----- Início Script "{nome_arquivo_base}" -----\n\n')
            
            conteudo = ""
            try:
                # Tenta ler com UTF-8
                with open(caminho_arquivo_entrada, 'r', encoding='utf-8', errors='strict') as f_in:
                    conteudo = f_in.read()
            except UnicodeDecodeError:
                # Se falhar, tenta ler com 'latin-1' (fallback para encodings do Windows)
                try:
                    with open(caminho_arquivo_entrada, 'r', encoding='latin-1') as f_in:
                        conteudo = f_in.read()
                except Exception as e:
                    conteudo = f"ERRO AO LER O ARQUIVO APÓS FALLBACK: {e}"
            except Exception as e:
                conteudo = f"ERRO INESPERADO AO LER O ARQUIVO: {e}"

            arquivo_saida.write(conteudo)
            
            arquivo_saida.write("\n\n")
            arquivo_saida.write(f'----- Final Script "{nome_arquivo_base}" -----\n\n\n')
            
    print(f"✅ Processo concluído! Os arquivos .cs foram unificados em '{caminho_completo_saida}'.")
    input("Pressione Enter para sair...")

if __name__ == "__main__":
    unificar_scripts_recursivo()