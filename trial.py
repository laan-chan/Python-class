import pygame # type: ignore
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 50)

# Game variables
number_to_guess = random.randint(1, 100)
input_box = pygame.Rect(200, 150, 200, 50)
user_input = ""
feedback = "Guess a number between 1 and 100"
attempts = 0

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw input box
    pygame.draw.rect(screen, BLUE, input_box, 2)

    # Render text
    title = large_font.render("Guess the Number", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

    text_surface = font.render(user_input, True, BLACK)
    screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
    feedback_surface = font.render(feedback, True, GREEN if "correct" in feedback else RED if "Try" in feedback else BLACK)
    screen.blit(feedback_surface, (WIDTH // 2 - feedback_surface.get_width() // 2, 250))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    guess = int(user_input)
                    attempts += 1
                    if guess < number_to_guess:
                        feedback = "Too low! Try again."
                    elif guess > number_to_guess:
                        feedback = "Too high! Try again."
                    else:
                        feedback = f"Correct! You guessed it in {attempts} attempts."
                except ValueError:
                    feedback = "Please enter a valid number."
                user_input = ""  # Reset input after pressing Enter
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
