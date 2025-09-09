#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abrir Currículo no Navegador para Conversão Manual
Autor: Lucas Stenck de Oliveira
"""

import os
import webbrowser
import subprocess
import platform

def main():
    """Função principal"""
    
    print("📄 Abrindo Currículo no Navegador")
    print("=" * 40)
    
    # Caminho do arquivo HTML
    html_path = r"C:\Users\lucas\Desktop\curriculo\index.html"
    
    # Verificar se o arquivo existe
    if not os.path.exists(html_path):
        print(f"❌ Arquivo não encontrado: {html_path}")
        print("💡 Certifique-se de que o caminho está correto")
        return
    
    print(f"📁 Abrindo: {html_path}")
    
    try:
        # Abrir no navegador padrão
        webbrowser.open(f"file://{os.path.abspath(html_path)}")
        
        print("✅ Currículo aberto no navegador!")
        print("\n💡 Para converter para PDF:")
        print("1. Pressione Ctrl + P")
        print("2. Selecione 'Salvar como PDF'")
        print("3. Configure as opções:")
        print("   - Formato: A4")
        print("   - Margens: Mínimas")
        print("   - Escala: Ajustar à página")
        print("   - Desmarque cabeçalhos e rodapés")
        print("4. Escolha o local e nome do arquivo")
        print("5. Clique em 'Salvar'")
        
        # Tentar abrir o arquivo diretamente também
        try:
            if platform.system() == "Windows":
                os.startfile(html_path)
                print("\n🔍 Arquivo também aberto com o programa padrão")
        except:
            pass
            
    except Exception as e:
        print(f"❌ Erro ao abrir no navegador: {str(e)}")
        print("💡 Tente abrir manualmente o arquivo index.html")

if __name__ == "__main__":
    main()
