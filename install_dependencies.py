#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instalador de Dependências para Conversor de PDF
Autor: Lucas Stenck de Oliveira
"""

import subprocess
import sys
import os

def install_package(package):
    """Instala um pacote usando pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    """Função principal de instalação"""
    
    print("📦 Instalador de Dependências - Conversor de PDF")
    print("=" * 50)
    
    # Lista de dependências
    packages = [
        "weasyprint>=60.0",
        "pathlib2>=2.3.7"
    ]
    
    print("🔍 Verificando dependências...")
    
    # Verificar se pip está disponível
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
    except subprocess.CalledProcessError:
        print("❌ pip não encontrado!")
        print("💡 Instale o pip primeiro")
        return
    
    # Instalar cada pacote
    for package in packages:
        print(f"📦 Instalando {package}...")
        
        if install_package(package):
            print(f"✅ {package} instalado com sucesso!")
        else:
            print(f"❌ Falha ao instalar {package}")
            return
    
    print("\n🎉 Todas as dependências foram instaladas!")
    print("💡 Agora você pode executar: python convert_to_pdf.py")

if __name__ == "__main__":
    main()
