import os
import subprocess
import webbrowser

# Caminho completo do arquivo
html_path = os.path.abspath("index.html")

print(f"Abrindo: {html_path}")

# Tentar abrir com o navegador padrão
try:
    webbrowser.open(f"file://{html_path}")
    print("Arquivo aberto no navegador!")
except Exception as e:
    print(f"Erro ao abrir no navegador: {e}")
    
    # Tentar abrir com o programa padrão
    try:
        os.startfile(html_path)
        print("Arquivo aberto com programa padrão!")
    except Exception as e2:
        print(f"Erro ao abrir arquivo: {e2}")
        print("Abra manualmente o arquivo index.html")

print("\nPara converter para PDF:")
print("1. Pressione Ctrl + P")
print("2. Selecione 'Salvar como PDF'")
print("3. Configure: A4, Margens mínimas")
print("4. Desmarque cabeçalhos e rodapés")
print("5. Salve o arquivo")
