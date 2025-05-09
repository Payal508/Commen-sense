import pygame

# Initialize pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Greeting Teachers")

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set the font and size
font = pygame.font.Font(None, 72)

# Create a text surface with the message "Hello teachers"
text = font.render("Hello teachers", True, white)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Draw the text surface on the screen
    screen.blit(text, (250, 200))

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
