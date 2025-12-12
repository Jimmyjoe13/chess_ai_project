import sys
import pygame
import chess

def check_environment() -> None:
    """
    Vérifie l'installation des bibliothèques critiques et affiche leurs versions.
    """
    print(f"✅ Python Version: {sys.version.split()[0]}")
    
    # 1. Vérification de Pygame
    try:
        pygame.init()
        print(f"✅ Pygame Version: {pygame.version.ver}")
        print("   -> Pygame initialisé avec succès.")
        pygame.quit()
    except Exception as e:
        print(f"❌ Erreur critique Pygame : {e}")
        sys.exit(1)

    # 2. Vérification de Python-Chess
    try:
        board = chess.Board()
        print(f"✅ Python-Chess Version: {chess.__version__}")
        print(f"   -> Test logique échiquier : {board.fen()}")
    except Exception as e:
        print(f"❌ Erreur critique Python-Chess : {e}")
        sys.exit(1)

    print("\n🚀 Tout est prêt ! L'environnement est correctement configuré.")

if __name__ == "__main__":
    check_environment()