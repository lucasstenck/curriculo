#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conversor de Currículo HTML para PDF
Autor: Lucas Stenck de Oliveira
Descrição: Converte o currículo HTML em PDF mantendo o design original
"""

import os
import sys
from pathlib import Path
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

def convert_html_to_pdf(html_path, output_path=None):
    """
    Converte arquivo HTML para PDF mantendo o design original
    
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
        
        # Configurar fontes
        font_config = FontConfiguration()
        
        # Ler o arquivo HTML
        with open(html_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Criar objeto HTML
        html_doc = HTML(string=html_content, base_url=os.path.dirname(html_path))
        
        # Configurar CSS para impressão
        css_content = """
        @page {
            size: A4;
            margin: 0.5cm;
        }
        
        body {
            font-family: 'Inter', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
        }
        
        .container {
            max-width: none;
            margin: 0;
            display: flex;
            background: white;
            box-shadow: none;
            border-radius: 0;
            overflow: hidden;
        }
        
        .left-column {
            width: 35%;
            background: #2c3e50 !important;
            color: white !important;
            padding: 30px;
            position: relative;
        }
        
        .right-column {
            width: 65%;
            padding: 40px;
            background: white !important;
            color: black !important;
        }
        
        .profile-image {
            width: 150px;
            height: 150px;
            margin: 0 auto 20px;
            border-radius: 50%;
            overflow: hidden;
            border: 4px solid rgba(255, 255, 255, 0.2);
        }
        
        .profile-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .name {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 5px;
            letter-spacing: 1px;
            color: white;
        }
        
        .title {
            font-size: 16px;
            color: #bdc3c7;
            font-weight: 400;
        }
        
        .age {
            font-size: 14px;
            color: #95a5a6;
            font-weight: 400;
            margin-top: 5px;
        }
        
        .contact-section h3,
        .skills-section h3,
        .education-section h3 {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 15px;
            color: #ecf0f1;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
        }
        
        .contact-item {
            display: flex;
            align-items: center;
            margin-bottom: 12px;
            font-size: 14px;
        }
        
        .contact-item i {
            width: 20px;
            margin-right: 10px;
            color: #3498db;
        }
        
        .contact-item a {
            color: #ecf0f1;
            text-decoration: none;
        }
        
        .skill-category h4 {
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 8px;
            color: #3498db;
        }
        
        .skill-category li {
            font-size: 13px;
            margin-bottom: 5px;
            padding-left: 15px;
            position: relative;
        }
        
        .skill-category li::before {
            content: "•";
            color: #3498db;
            position: absolute;
            left: 0;
        }
        
        .education-item h4 {
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 5px;
            color: #ecf0f1;
        }
        
        .education-item p {
            font-size: 13px;
            color: #bdc3c7;
        }
        
        .summary-section h3,
        .experience-section h3,
        .projects-section h3 {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 15px;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
        }
        
        .summary-section p {
            font-size: 14px;
            line-height: 1.7;
            margin-bottom: 15px;
            color: #555;
        }
        
        .experience-item {
            margin-bottom: 25px;
            padding-bottom: 20px;
            border-bottom: 1px solid #ecf0f1;
        }
        
        .experience-item:last-child {
            border-bottom: none;
        }
        
        .experience-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }
        
        .experience-header h4 {
            font-size: 16px;
            font-weight: 600;
            color: #2c3e50;
        }
        
        .period {
            font-size: 12px;
            color: #7f8c8d;
            background: #ecf0f1;
            padding: 4px 8px;
            border-radius: 4px;
        }
        
        .company {
            font-size: 14px;
            color: #3498db;
            font-weight: 500;
            margin-bottom: 10px;
        }
        
        .experience-item li {
            font-size: 13px;
            margin-bottom: 5px;
            padding-left: 15px;
            position: relative;
            color: #555;
        }
        
        .experience-item li::before {
            content: "▸";
            color: #3498db;
            position: absolute;
            left: 0;
        }
        
        .portfolio-link {
            text-align: center;
            margin-top: 15px;
        }
        
        .portfolio-btn {
            display: inline-flex;
            align-items: center;
            background: #3498db;
            color: white;
            text-decoration: none;
            padding: 12px 24px;
            border-radius: 25px;
            font-weight: 600;
            font-size: 14px;
            box-shadow: 0 2px 8px rgba(52, 152, 219, 0.3);
        }
        
        .portfolio-btn i {
            margin-right: 8px;
            font-size: 16px;
        }
        
        /* Garantir que as cores sejam impressas */
        * {
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
        """
        
        # Criar CSS
        css = CSS(string=css_content, font_config=font_config)
        
        # Gerar PDF
        html_doc.write_pdf(
            output_path,
            stylesheets=[css],
            font_config=font_config
        )
        
        print(f"✅ PDF gerado com sucesso: {output_path}")
        return str(output_path)
        
    except Exception as e:
        print(f"❌ Erro ao converter para PDF: {str(e)}")
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
    
    # Converter para PDF
    result = convert_html_to_pdf(html_path, output_path)
    
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

if __name__ == "__main__":
    # Verificar dependências
    try:
        import weasyprint
    except ImportError:
        print("❌ WeasyPrint não encontrado!")
        print("📦 Instale com: pip install weasyprint")
        sys.exit(1)
    
    main()
