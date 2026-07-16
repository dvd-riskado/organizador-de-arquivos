import shutil as sht
from pathlib import Path

Downloads = Path.home() / "Downloads"

pastas = {
    ".png":"Imagens",
    ".jpg":"Imagens",
    ".jpeg":"Imagens",
    ".pdf":"Documentos",
    ".mp3":"Músicas",
    ".mp4":"Vídeos"
}

def mover():
    print("Movendo arquivos...")

    for arquivo in Downloads.iterdir():
        extensao = arquivo.suffix
        destino = Path.home() / pastas[extensao]
        if extensao in pastas:
            print(f"Movendo '{arquivo.name}'...")
            sht.move(arquivo, destino)
            print("Movido!")
            print("")
        elif arquivo.is_dir():
            print(f"{arquivo.name} é um diretório. Não será movido")
            print("")
        else:
            print(f"a estenção '{arquivo.suffix}' do arquivo {arquivo.name} não está nos meus dicionários")
            print("Partindo para o próximo documento...")
            print("")

def escolha():
    for arquivo in Downloads.iterdir():
        extensao = arquivo.suffix
        if extensao in pastas:
            print(f"- '{arquivo.name}' -> {pastas[extensao]}")
        elif arquivo.is_dir():
            print(f"- '{arquivo.name}' é uma pasta")
        else:
            print(f"- '{arquivo.name}' -> '{extensao}' não está no dicionário")

mover()