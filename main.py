import pygame

def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((500, 500))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        SCREEN.fill((0, 255, 0))
        pygame.display.flip()

main()
