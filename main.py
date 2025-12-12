import pygame
import sys

# --- CONSTANTES DE CONFIGURATION ---
WIDTH, HEIGHT = 800, 800  # Taille de la fenêtre
ROWS, COLS = 8, 8         # Dimensions de l'échiquier
SQUARE_SIZE = WIDTH // COLS  # Taille d'une case (100px)

# Couleurs RVB (Rouge, Vert, Bleu)
COLOR_LIGHT = (238, 238, 210)  # Couleur "blanc" (crème)
COLOR_DARK = (118, 150, 86)    # Couleur "noir" (vert classique chess.com)

class Game:
    def __init__(self) -> None:
        """Initialise Pygame et la fenêtre de jeu."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess AI - Python Project")
        self.clock = pygame.time.Clock() # Pour gérer les FPS

    def draw_board(self) -> None:
        """Dessine le damier 8x8 sur l'écran."""
        self.screen.fill(COLOR_LIGHT) # Fond clair par défaut
        
        for row in range(ROWS):
            for col in range(COLS):
                # Si la somme de row + col est impaire, c'est une case foncée
                if (row + col) % 2 == 1:
                    rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                    pygame.draw.rect(self.screen, COLOR_DARK, rect)

    def run(self) -> None:
        """Boucle principale du jeu."""
        running = True
        while running:
            # 1. Gestion des événements (Clavier, Souris, Fermeture)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # 2. Dessin
            self.draw_board()
            
            # 3. Mise à jour de l'affichage
            pygame.display.flip()
            self.clock.tick(60) # Limite à 60 FPS

        # Sortie propre
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()