import os
import requests
import sys

# Nouvelle source fiable (Chess.com CDN - Style "Neo")
BASE_URL = "https://images.chesscomfiles.com/chess-themes/pieces/neo/150/"
ASSETS_DIR = os.path.join("assets", "images")

# Mapping : Clé utilisée dans notre code -> Nom du fichier sur le serveur
# w=white, b=black
# p=pawn, r=rook, n=knight, b=bishop, q=queen, k=king
PIECES = {
    "bP": "bp.png", "bR": "br.png", "bN": "bn.png", "bB": "bb.png", "bQ": "bq.png", "bK": "bk.png",
    "wP": "wp.png", "wR": "wr.png", "wN": "wn.png", "wB": "wb.png", "wQ": "wq.png", "wK": "wk.png"
}

def setup_images():
    # 1. Création du dossier si nécessaire
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)
        print(f"📁 Dossier créé : {ASSETS_DIR}")

    print("⬇️  Démarrage du téléchargement depuis Chess.com...")
    
    for local_name, remote_name in PIECES.items():
        # Chemin du fichier final (ex: assets/images/wP.png)
        # Note: On garde le nom local 'wP.png' pour correspondre à notre code main.py
        file_path = os.path.join(ASSETS_DIR, f"{local_name}.png")
        url = BASE_URL + remote_name

        # On télécharge toujours pour être sûr d'avoir la bonne version
        try:
            print(f"   ⏳ Téléchargement de {local_name}...", end="\r")
            response = requests.get(url)
            response.raise_for_status() # Lève une erreur si 404
            
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"   ✅ {local_name}.png téléchargé avec succès.   ")
            
        except Exception as e:
            print(f"\n   ❌ Erreur CRITIQUE sur {local_name} : {e}")
            sys.exit(1) # On arrête tout si une image manque

    print("\n🚀 Assets installés ! Tu peux lancer 'python main.py'.")

if __name__ == "__main__":
    setup_images()