import pygame
import math

# Inicializa Pygame
pygame.init()

# Tamaño de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colores
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuentes
font = pygame.font.SysFont('arial', 100)

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Función para dibujar un corazón
def draw_heart(x, y, size):
    # Dibuja el corazón usando el método de las ecuaciones paramétricas
    for t in range(0, 360, 1):
        t_rad = math.radians(t)
        x_offset = 16 * math.sin(t_rad) ** 3
        y_offset = 13 * math.cos(t_rad) - 5 * math.cos(2 * t_rad) - 2 * math.cos(3 * t_rad) - math.cos(4 * t_rad)
        
        # Escalado y desplazamiento
        pygame.draw.circle(screen, RED, (int(x + x_offset * size), int(y - y_offset * size)), 1)

# Función para dibujar el corazón con la "J" en el centro
def draw_heart_with_j(x, y, size):
    # Dibuja el corazón
    draw_heart(x, y, size)
    
    # Renderiza la letra "J"
    text = font.render('J', True, WHITE)
    
    # Centra la letra "J" en el corazón
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

# Bucle principal
running = True
while running:
    screen.fill(BLACK)  # Limpiar la pantalla

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar el corazón con la "J" en el centro
    draw_heart_with_j(screen_width // 2, screen_height // 2, 10)

    pygame.display.flip()  # Actualizar la pantalla

    clock.tick(60)  # 60 FPS

# Cerrar Pygame
pygame.quit()
