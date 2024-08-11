import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# 설정
width, height, depth = 8, 8, 8
cube_size = 1.0
color_levels = 16
rgb_array = np.zeros((width, height, depth, 3), dtype=np.uint8)
slider_width = 200
slider_height = 20
slider_x = 50
slider_y = 50
slider_gap = 30

# 슬라이더 색상
slider_background_color = (100, 100, 100)
slider_color = (200, 0, 0)

def draw_cube(x, y, z, color):
    """주어진 좌표에 큐브를 그립니다."""
    glBegin(GL_QUADS)
    
    # Front face
    glColor3f(*color)
    glVertex3f(x - cube_size / 2, y - cube_size / 2, z + cube_size / 2)
    glVertex3f(x + cube_size / 2, y - cube_size / 2, z + cube_size / 2)
    glVertex3f(x + cube_size / 2, y + cube_size / 2, z + cube_size / 2)
    glVertex3f(x - cube_size / 2, y + cube_size / 2, z + cube_size / 2)
    
    # Back face
    glVertex3f(x - cube_size / 2, y - cube_size / 2, z - cube_size / 2)
    glVertex3f(x + cube_size / 2, y - cube_size / 2, z - cube_size / 2)
    glVertex3f(x + cube_size / 2, y + cube_size / 2, z - cube_size / 2)
    glVertex3f(x - cube_size / 2, y + cube_size / 2, z - cube_size / 2)
    
    # Top face
    glVertex3f(x - cube_size / 2, y + cube_size / 2, z - cube_size / 2)
    glVertex3f(x + cube_size / 2, y + cube_size / 2, z - cube_size / 2)
    glVertex3f(x + cube_size / 2, y + cube_size / 2, z + cube_size / 2)
    glVertex3f(x - cube_size / 2, y + cube_size / 2, z + cube_size / 2)
    
    # Bottom face
    glVertex3f(x - cube_size / 2, y - cube_size / 2, z - cube_size / 2)
    glVertex3f(x + cube_size / 2, y - cube_size / 2, z - cube_size / 2)
    glVertex3f(x + cube_size / 2, y - cube_size / 2, z + cube_size / 2)
    glVertex3f(x - cube_size / 2, y - cube_size / 2, z + cube_size / 2)
    
    # Right face
    glVertex3f(x + cube_size / 2, y - cube_size / 2, z - cube_size / 2)
    glVertex3f(x + cube_size / 2, y + cube_size / 2, z - cube_size / 2)
    glVertex3f(x + cube_size / 2, y + cube_size / 2, z + cube_size / 2)
    glVertex3f(x + cube_size / 2, y - cube_size / 2, z + cube_size / 2)
    
    # Left face
    glVertex3f(x - cube_size / 2, y - cube_size / 2, z - cube_size / 2)
    glVertex3f(x - cube_size / 2, y + cube_size / 2, z - cube_size / 2)
    glVertex3f(x - cube_size / 2, y + cube_size / 2, z + cube_size / 2)
    glVertex3f(x - cube_size / 2, y - cube_size / 2, z + cube_size / 2)
    
    glEnd()

def draw_axes():
    """좌표계 축을 그립니다."""
    glBegin(GL_LINES)
    
    # X축 (빨간색)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-width / 2, 0, 0)
    glVertex3f(width / 2, 0, 0)
    
    # Y축 (초록색)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0, -height / 2, 0)
    glVertex3f(0, height / 2, 0)
    
    # Z축 (파란색)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0, 0, -depth / 2)
    glVertex3f(0, 0, depth / 2)
    
    glEnd()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(-width / 2, -height / 2, -depth / 2 - 5)
    
    draw_axes()  # 좌표계 그리기
    
    for x in range(width):
        for y in range(height):
            for z in range(depth):
                color = (rgb_array[x, y, z] / 15.0).tolist()
                draw_cube(x, y, z, color)
    
    pygame.display.flip()

def set_color(x, y, z, r, g, b):
    """지정된 위치의 색상을 변경합니다."""
    if 0 <= x < width and 0 <= y < height and 0 <= z < depth:
        rgb_array[x, y, z] = [r, g, b]

def draw_slider(surface, x, y, width, height, value, min_value, max_value):
    """슬라이더를 그립니다."""
    pygame.draw.rect(surface, slider_background_color, (x, y, width, height))
    slider_pos = x + int((value - min_value) / (max_value - min_value) * (width - height))
    pygame.draw.rect(surface, slider_color, (slider_pos, y, height, height))

def main():
    global slider_r_value, slider_g_value, slider_b_value, current_x, current_y, current_z

    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D Color Picker")
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)
    
    # 슬라이더 초기화
    slider_r_value, slider_g_value, slider_b_value = 0, 0, 0
    current_x, current_y, current_z = 0, 0, 0
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (slider_x <= x <= slider_x + slider_width and
                    slider_y <= y <= slider_y + slider_height):
                    slider_r_value = int((x - slider_x) / (slider_width - slider_height) * 15)
                elif (slider_x <= x <= slider_x + slider_width and
                      slider_y + slider_height + slider_gap <= y <= slider_y + 2 * slider_height + slider_gap):
                    slider_g_value = int((x - slider_x) / (slider_width - slider_height) * 15)
                elif (slider_x <= x <= slider_x + slider_width and
                      slider_y + 2 * slider_height + 2 * slider_gap <= y <= slider_y + 3 * slider_height + 2 * slider_gap):
                    slider_b_value = int((x - slider_x) / (slider_width - slider_height) * 15)
                else:
                    # OpenGL 3D 좌표 시스템에서 클릭 처리
                    # 3D 좌표와 2D 화면 좌표를 매핑하는 것은 복잡할 수 있습니다.
                    # 대안으로는 간단하게 클릭한 도트의 좌표를 업데이트
                    x = int((x - 50) / (200 / width))
                    y = int((y - 50) / (200 / height))
                    if 0 <= x < width and 0 <= y < height:
                        set_color(x, y, current_z, slider_r_value, slider_g_value, slider_b_value)
            elif event.type == MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    if (slider_x <= x <= slider_x + slider_width and
                        slider_y <= y <= slider_y + slider_height):
                        slider_r_value = int((x - slider_x) / (slider_width - slider_height) * 15)
                    elif (slider_x <= x <= slider_x + slider_width and
                          slider_y + slider_height + slider_gap <= y <= slider_y + 2 * slider_height + slider_gap):
                        slider_g_value = int((x - slider_x) / (slider_width - slider_height) * 15)
                    elif (slider_x <= x <= slider_x + slider_width and
                          slider_y + 2 * slider_height + 2 * slider_gap <= y <= slider_y + 3 * slider_height + 2 * slider_gap):
                        slider_b_value = int((x - slider_x) / (slider_width - slider_height) * 15)
        
        draw_scene()
        
        # 슬라이더 그리기
        surface = pygame.display.get_surface()
        draw_slider(surface, slider_x, slider_y, slider_width, slider_height, slider_r_value, 0, 15)
        draw_slider(surface, slider_x, slider_y + slider_height + slider_gap, slider_width, slider_height, slider_g_value, 0, 15)
        draw_slider(surface, slider_x, slider_y + 2 * slider_height + 2 * slider_gap, slider_width, slider_height, slider_b_value, 0, 15)
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()
