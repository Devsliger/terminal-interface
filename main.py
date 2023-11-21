import pygame
import sys

pygame.init()

# Define constants for window size and colors
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Interface")


# Define constants for text rendering
LINE_HEIGHT = 30
PROMPT_X = 10  # X-coordinate for the '>' symbol
PROMPT_Y = 10  # Y-coordinate for the '>' symbol

# Create Pygame font object
font = pygame.font.Font(None, 24)


# Function to handle the main game loop
def main():

    # Initialize variables for input and history
    input_text = ''
    history = []



    # Main game loop
    run = True

    while run:
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Add the current input to the history when the Enter key is pressed
                    history.append('> ' + input_text)

                    # Process the input_text here for your game logic
                    # For now, let's just print it to the console
                    print(input_text)

                    # Clear the input_text for the next input
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    # Remove the last character when the Backspace key is pressed
                    input_text = input_text[:-1]
                else:
                    # Append the unicode character to the input_text
                    input_text += event.unicode

        # Fill the screen with a black background
        WIN.fill("black")

        # Display the history of inputs, showing the last 10 lines
        y = PROMPT_Y
        for line in history[-10:]:
            text_surface = font.render(line, True, "white")
            WIN.blit(text_surface, (PROMPT_X, y))
            y += LINE_HEIGHT

        # Display the current input_text with the command prompt
        input_surface = font.render('> ' + input_text, True, "white")
        WIN.blit(input_surface, (PROMPT_X, y))

        # Update the display
        pygame.display.flip()




# Entry point for the script
if __name__ == '__main__':
    main()


