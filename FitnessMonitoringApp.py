import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
FPS = 30

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real-Time Fitness Monitoring App")

# Fonts
font = pygame.font.Font(None, 36)

# Colors
text_color = (0, 0, 0)

# User data
username = "JohnDoe"
heart_rate = 75
calories_burned = 120.5

def display_fitness_data():
    screen.fill(BACKGROUND_COLOR)

    # Display username
    text = font.render(f"Username: {username}", True, text_color)
    screen.blit(text, (20, 20))

    # Display heart rate
    text = font.render(f"Heart Rate: {heart_rate} bpm", True, text_color)
    screen.blit(text, (20, 60))

    # Display calories burned
    text = font.render(f"Calories Burned: {calories_burned:.2f} kcal", True, text_color)
    screen.blit(text, (20, 100))

def main():
    global heart_rate, calories_burned

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Simulate real-time updates
        heart_rate += random.randint(-5, 5)
        calories_burned += random.uniform(10, 20)

        # Display fitness data
        display_fitness_data()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()