import pygame
import random

pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Solitaire")

# Define geometric shapes
card_width = 50
card_height = 80
card_color = (255, 255, 255)
card_border_color = (0, 0, 0)

circle_radius = 10
circle_color = (255, 0, 0)

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.rect = pygame.Rect(0, 0, card_width, card_height)
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.face_up = True

    def draw(self):
        pygame.draw.rect(screen, card_color, self.rect)
        pygame.draw.rect(screen, card_border_color, self.rect, 2)

        if self.face_up:
            pygame.draw.circle(screen, circle_color, self.rect.center, circle_radius)

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        return None

def main():
    deck = Deck()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((0, 128, 0))

        # Draw cards
        card = deck.draw_card()
        if card:
            card.draw()

        # Update screen
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

