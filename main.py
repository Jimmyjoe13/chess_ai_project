import pygame
import sys
import os
import chess

# --- CONSTANTES ---
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

COLOR_LIGHT = (238, 238, 210)
COLOR_DARK = (118, 150, 86)

class Game:
    def __init__(self) -> None:
        """Initialise le jeu, le plateau logique et les assets."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess AI")
        self.clock = pygame.time.Clock()
        
        # 1. Logique : Création du plateau avec python-chess
        # Cela place automatiquement les pièces en position de départ
        self.board = chess.Board()
        
        # 2. Visuel : Chargement des images
        self.images = {}
        self._load_assets()

    def _load_assets(self) -> None:
        """Charge les images des pièces dans un dictionnaire."""
        pieces = ['bP', 'bR', 'bN', 'bB', 'bQ', 'bK', 
                  'wP', 'wR', 'wN', 'wB', 'wQ', 'wK']
        
        for piece in pieces:
            path = os.path.join("assets", "images", f"{piece}.png")
            try:
                # On charge l'image et on la redimensionne à la taille de la case
                image = pygame.image.load(path)
                self.images[piece] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
            except FileNotFoundError:
                print(f"❌ Image manquante : {path}. As-tu lancé setup_assets.py ?")
                sys.exit(1)

    def draw_board(self) -> None:
        """Dessine l'échiquier (cases vides)."""
        for row in range(ROWS):
            for col in range(COLS):
                color = COLOR_LIGHT if (row + col) % 2 == 0 else COLOR_DARK
                pygame.draw.rect(self.screen, color, 
                               (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self) -> None:
        """Dessine les pièces selon l'état actuel de self.board."""
        # On parcourt les 64 cases de l'échiquier logique
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            
            if piece:
                # python-chess stocke les pièces sous forme d'objet (ex: Piece.from_symbol('P'))
                # Nous convertissons cela en notre format de nom de fichier (ex: 'wP')
                # piece.symbol() renvoie 'P' (blanc) ou 'p' (noir)
                symbol = piece.symbol()
                
                # Astuce : Majuscule = Blanc, Minuscule = Noir dans la notation FEN standard
                if symbol.isupper():
                    img_key = f"w{symbol}"
                else:
                    img_key = f"b{symbol.upper()}"
                
                # Conversion des coordonnées logiques (0-63) en (x, y) pixels
                # chess.square_file(0) -> 0 (colonne a), chess.square_rank(0) -> 0 (ligne 1)
                # Attention : Dans Pygame, (0,0) est en haut à gauche. 
                # Dans les échecs, le rang 1 est en BAS. Il faut inverser l'axe Y.
                col = chess.square_file(square)
                row = 7 - chess.square_rank(square) 
                
                self.screen.blit(self.images[img_key], 
                               (col * SQUARE_SIZE, row * SQUARE_SIZE))

    def run(self) -> None:
        """Boucle principale."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Ordre de rendu important : d'abord le plateau, puis les pièces par-dessus
            self.draw_board()
            self.draw_pieces()
            
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()