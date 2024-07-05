import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
HEART_COLOR = (255, 0, 0)
FPS = 30

# Heart properties
HEART_WIDTH = 50
HEART_HEIGHT = 50
HEART_X = WIDTH // 2 - HEART_WIDTH // 2
HEART_Y = HEIGHT // 2 - HEART_HEIGHT // 2
HEART_RATE = 75

# Clock for controlling the frame rate
clock = pygame.time.Clock()

def draw_heart(x, y):
    pygame.draw.polygon(screen, HEART_COLOR, [(x, y + HEART_HEIGHT // 4),
                                               (x + HEART_WIDTH // 2, y),
                                               (x + HEART_WIDTH, y + HEART_HEIGHT // 4),
                                               (x + HEART_WIDTH, y + HEART_HEIGHT // 2),
                                               (x + HEART_WIDTH // 2, y + HEART_HEIGHT),
                                               (x, y + HEART_HEIGHT // 2)])

def display_heart_rate():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Heart Rate: {HEART_RATE} bpm", True, (0, 0, 0))
    screen.blit(text, (10, 10))

def main():
    global HEART_RATE

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Simulate heart rate changes
        HEART_RATE += random.randint(-2, 2)

        # Draw background
        screen.fill(BACKGROUND_COLOR)

        # Draw heart
        draw_heart(HEART_X, HEART_Y)

        # Display heart rate
        display_heart_rate()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    # Create a window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Smart Health Monitoring System")

    main()