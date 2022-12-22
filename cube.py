import pygame
import numpy as np

# Set up the Pygame window
pygame.init()
window_size = (600, 600)
screen = pygame.display.set_mode(window_size)

# Define the vertices of the cube
vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]])

# Define the edges of the cube
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

# Set up the camera
fov = np.pi / 2
camera_distance = 2

# Set up the rotation angle
angle = 0

while True:
    # Clear the screen
    screen.fill((0, 0, 0))

    # Rotate the vertices
    rotated_vertices = vertices.dot(np.array([[np.cos(angle), 0, np.sin(angle)],
                                              [0, 1, 0],
                                              [-np.sin(angle), 0, np.cos(angle)]]))

    # Project the vertices onto the 2D screen
    projected_vertices = rotated_vertices / rotated_vertices[:, 2:] * camera_distance

    # Draw the edges
    for edge in edges:
        start = (int(round(projected_vertices[edge[0]][0] + window_size[0] / 2)), int(round(projected_vertices[edge[0]][1] + window_size[1] / 2)))
        end = (int(round(projected_vertices[edge[1]][0] + window_size[0] / 2)), int(round(projected_vertices[edge[1]][1] + window_size[1] / 2)))
        pygame.draw.line(screen, (255, 255, 255), start, end, 1)

    # Update the rotation angle
    angle += np.pi / 180

    # Update the screen
    pygame.display.flip()
