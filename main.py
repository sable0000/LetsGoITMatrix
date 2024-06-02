import pygame
import random

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ARIA Owned This Site")

# Load and resize logo
logo = pygame.image.load('logo.png')
logo = pygame.transform.scale(logo, (500, 200))

# Font settings
font = pygame.font.Font(None, 12)  # Smaller font size

# Generate random character or number
def generate_character():
    char_code = random.randint(33, 126)  # ASCII range for characters and numbers
    return chr(char_code)

# Main loop
running = True
lines = []
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Add new characters
    if random.randint(0, 1) == 0 and len(lines) < 100:
        char = generate_character()
        lines.append({'char': char, 'pos_x': random.randint(0, screen.get_width()), 'offset_y': -1000, 'fade': random.randint(0, 255)})

    # Draw characters
    for line in lines:
        text_surface = font.render(line['char'], True, pygame.Color(0, 255, 0, line['fade']))  # Add fade effect
        screen.blit(text_surface, (line['pos_x'], line['offset_y']))
        line['offset_y'] += 5
        if line['offset_y'] >= screen.get_height():
            lines.remove(line)
        line['fade'] -= 1  # Reduce fade value
        if line['fade'] < 0:
            line['fade'] = 0

    # Draw resized logo
    screen.blit(logo, (150, 350))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
