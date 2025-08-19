from pathlib import Path
import subprocess
import os


# Dossier contenant les fichiers AVI à convertir
input_directory = "./videos"  # Modifiez ce chemin si nécessaire
output_directory = "./converted"

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_directory, exist_ok=True)

# Options de conversion : H.264 pour la vidéo, AAC pour l'audio
def convert_avi_to_mp4(input_path, output_path):
    command = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", "libx264",
        "-preset", "faster",         # pour un bon compromis qualité/temps
        "-crf", "23",              # facteur de qualité (plus bas = meilleure qualité)
        "-c:a", "aac",
        "-b:a", "128k",
        "-movflags", "+faststart", # pour un démarrage rapide sur le web/mobile
        "-y",
        "-loglevel", "error",
        "-stats",
        output_path
    ]
    try:
        print(f"Conversion de '{Path(input_path).name}'...")
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"[✘] Échec de la conversion : {input_path}")

# Parcours des fichiers AVI
for filename in os.listdir(input_directory):
    if filename.lower().endswith(".avi"):
        input_path = os.path.join(input_directory, filename)
        output_filename = os.path.splitext(filename)[0] + ".mp4"
        output_path = os.path.join(output_directory, output_filename)
        convert_avi_to_mp4(input_path, output_path)
