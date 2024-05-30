import pygame
import numpy as np

# Inicializar o Pygame
pygame.init()
window_size = (600, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Rotating Cube")

# Definir os vértices do cubo
vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]])

# Definir as arestas do cubo
edges = np.array([[0, 1],
                  [1, 2],
                  [2, 3],
                  [3, 0],
                  [4, 5],
                  [5, 6],
                  [6, 7],
                  [7, 4],
                  [0, 4],
                  [1, 5],
                  [2, 6],
                  [3, 7]])

# Configurar a câmera
camera_distance = 5

# Configurar o ângulo de rotação
angle = 0

# Função para projetar os vértices 3D para 2D
def project(vertices, camera_distance, window_size):
    # Evitar divisão por zero
    with np.errstate(divide='ignore', invalid='ignore'):
        projected_vertices = vertices / (vertices[:, 2].reshape(-1, 1) + camera_distance)
        projected_vertices = projected_vertices[:, :2] * min(window_size) / 2
        projected_vertices += np.array(window_size) / 2
    
    # Substituir valores infinitos e NaN por zero
    projected_vertices = np.nan_to_num(projected_vertices)
    return projected_vertices.astype(int)

# Loop principal
running = True
clock = pygame.time.Clock()
FPS = 30
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpar a tela
    screen.fill((0, 0, 0))

    # Rotacionar os vértices
    rotation_matrix = np.array([[np.cos(angle), 0, np.sin(angle)],
                                [0, 1, 0],
                                [-np.sin(angle), 0, np.cos(angle)]])
    rotated_vertices = vertices.dot(rotation_matrix.T)

    # Projetar os vértices na tela 2D
    projected_vertices = project(rotated_vertices, camera_distance, window_size)

    # Desenhar as arestas
    for edge in edges:
        start, end = projected_vertices[edge]
        pygame.draw.line(screen, (255, 255, 255), start, end, 1)

    # Atualizar o ângulo de rotação
    angle += np.pi / 180
    if angle >= 2 * np.pi:
        angle -= 2 * np.pi

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
