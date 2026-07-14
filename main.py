from pathlib import Path
downloads = Path.home() / "Downloads"
pastas = {
    ".png":"Fotos",
    ".jpg":"Fotos",
    ".jpeg":"Fotos",
    ".pdf":"Documentos",
    ".mp3":"Músicas",
    ".mp4":"Vídeos"
}

for arquivo in downloads.iterdir():
    extensao = arquivo.suffix
    if extensao in pastas:
        print(f"{arquivo.name} -> {pastas[extensao]}")
    elif arquivo.is_dir():
        print(f"{arquivo.name} é um diretório")
    else:
        print(f"a estenção '{arquivo.suffix}' do arquivo {arquivo.name} não está nos meus dicionários")
