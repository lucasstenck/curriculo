#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conversor de Currículo HTML para PDF (Versão Simples)
Autor: Lucas Stenck de Oliveira
Descrição: Converte o currículo HTML em PDF usando pdfkit
"""

import os
import sys
import subprocess
from pathlib import Path

def check_wkhtmltopdf():
    """Verifica se o wkhtmltopdf está instalado"""
    try:
        result = subprocess.run(['wkhtmltopdf', '--version'], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def install_wkhtmltopdf():
    """Instruções para instalar wkhtmltopdf"""
    print("❌ wkhtmltopdf não encontrado!")
    print("\n📦 Para instalar no Windows:")
    print("1. Baixe de: https://wkhtmltopdf.org/downloads.html")
    print("2. Instale o executável")
    print("3. Adicione ao PATH do sistema")
    print("\n💡 Ou use o comando:")
    print("winget install wkhtmltopdf")
    return False

def convert_html_to_pdf_pdfkit(html_path, output_path=None):
    """
    Converte arquivo HTML para PDF usando pdfkit
    
    Args:
        html_path (str): Caminho para o arquivo HTML
        output_path (str): Caminho de saída do PDF (opcional)
    
    Returns:
        str: Caminho do arquivo PDF gerado
    """
    
    try:
        # Verificar se o arquivo HTML existe
        if not os.path.exists(html_path):
            raise FileNotFoundError(f"Arquivo HTML não encontrado: {html_path}")
        
        # Definir caminho de saída se não fornecido
        if output_path is None:
            html_file = Path(html_path)
            output_path = html_file.with_suffix('.pdf')
        
        print(f"🔄 Convertendo {html_path} para PDF...")
        
        # Configurar opções do wkhtmltopdf
        options = {
            'page-size': 'A4',
            'margin-top': '0.5cm',
            'margin-right': '0.5cm',
            'margin-bottom': '0.5cm',
            'margin-left': '0.5cm',
            'encoding': 'UTF-8',
            'no-outline': None,
            'enable-local-file-access': None,
            'print-media-type': None,
            'javascript-delay': '1000'
        }
        
        # Converter para PDF
        import pdfkit
        pdfkit.from_file(html_path, output_path, options=options)
        
        print(f"✅ PDF gerado com sucesso: {output_path}")
        return str(output_path)
        
    except Exception as e:
        print(f"❌ Erro ao converter para PDF: {str(e)}")
        return None

def convert_html_to_pdf_browser(html_path, output_path=None):
    """
    Converte arquivo HTML para PDF usando navegador (fallback)
    
    Args:
        html_path (str): Caminho para o arquivo HTML
        output_path (str): Caminho de saída do PDF (opcional)
    
    Returns:
        str: Caminho do arquivo PDF gerado
    """
    
    try:
        # Verificar se o arquivo HTML existe
        if not os.path.exists(html_path):
            raise FileNotFoundError(f"Arquivo HTML não encontrado: {html_path}")
        
        # Definir caminho de saída se não fornecido
        if output_path is None:
            html_file = Path(html_path)
            output_path = html_file.with_suffix('.pdf')
        
        print(f"🔄 Convertendo {html_path} para PDF usando navegador...")
        
        # Abrir o arquivo HTML no navegador padrão
        import webbrowser
        webbrowser.open(f"file://{os.path.abspath(html_path)}")
        
        print("📄 Arquivo HTML aberto no navegador")
        print("💡 Para gerar PDF:")
        print("1. Pressione Ctrl + P")
        print("2. Selecione 'Salvar como PDF'")
        print("3. Escolha o local e nome do arquivo")
        print("4. Clique em 'Salvar'")
        
        return None
        
    except Exception as e:
        print(f"❌ Erro ao abrir no navegador: {str(e)}")
        return None

def main():
    """Função principal"""
    
    print("📄 Conversor de Currículo HTML para PDF")
    print("=" * 50)
    
    # Caminho do arquivo HTML
    html_path = r"file:///C:/Users/lucas/Desktop/curriculo/index.html"
    
    # Converter caminho file:// para caminho local
    if html_path.startswith("file:///"):
        html_path = html_path.replace("file:///", "")
        html_path = html_path.replace("/", "\\")
    
    # Verificar se o arquivo existe
    if not os.path.exists(html_path):
        print(f"❌ Arquivo não encontrado: {html_path}")
        print("💡 Certifique-se de que o caminho está correto")
        return
    
    # Caminho de saída
    output_path = html_path.replace(".html", "_curriculo.pdf")
    
    # Tentar usar pdfkit primeiro
    try:
        import pdfkit
        
        if check_wkhtmltopdf():
            result = convert_html_to_pdf_pdfkit(html_path, output_path)
        else:
            print("⚠️ wkhtmltopdf não encontrado, tentando instalar...")
            install_wkhtmltopdf()
            result = None
            
    except ImportError:
        print("⚠️ pdfkit não encontrado, usando método alternativo...")
        result = convert_html_to_pdf_browser(html_path, output_path)
    
    if result:
        print(f"\n🎉 Conversão concluída!")
        print(f"📁 Arquivo PDF: {result}")
        print(f"📏 Tamanho: {os.path.getsize(result) / 1024:.1f} KB")
        
        # Abrir o arquivo PDF (opcional)
        try:
            import subprocess
            import platform
            
            if platform.system() == "Windows":
                os.startfile(result)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", result])
            else:  # Linux
                subprocess.run(["xdg-open", result])
                
            print("🔍 PDF aberto automaticamente")
        except:
            print("💡 Abra o PDF manualmente para visualizar")
    else:
        print("❌ Falha na conversão")
        print("💡 Use o método manual: abra o HTML no navegador e imprima como PDF")

if __name__ == "__main__":
    main()
