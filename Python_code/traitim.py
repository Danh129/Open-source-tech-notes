import pygame
import math
import colorsys
import sys

# Khởi tạo pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("💖 Trái tim nhịp đập 💖")

clock = pygame.time.Clock()

def heart_points(scale, offset_x, offset_y):
    """Tạo danh sách điểm (x, y) cho hình trái tim."""
    points = []
    for t in range(0, 360, 2):
        rad = math.radians(t)
        x = 16 * math.sin(rad) ** 3
        y = 13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)
        x = offset_x + scale * x
        y = offset_y - scale * y
        points.append((x, y))
    return points

def draw_glow_heart(scale, color, pulse, layers=6):
    """Vẽ trái tim phát sáng với nhiều lớp."""
    for i in range(layers, 0, -1):
        alpha = int(255 / (i + 1))
        size = scale * (1 + i * 0.04)
        glow_color = (*color, alpha)
        draw_heart(size, glow_color, pulse, filled=True)

def draw_heart(scale, color, pulse, filled=True):
    """Vẽ trái tim chính."""
    heart = heart_points(scale * pulse, WIDTH//2, HEIGHT//2 + 30)
    surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    if filled:
        pygame.draw.polygon(surface, color, heart)
    else:
        pygame.draw.lines(surface, color, True, heart, 3)
    screen.blit(surface, (0, 0))

# Vòng lặp chính
running = True
t = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t += 0.05
    screen.fill((10, 10, 20))  

    # Tạo hiệu ứng nhịp đập
    pulse = 1 + 0.01 * math.sin(t * 2)

    # Hiệu ứng đổi màu neon (HSV -> RGB)
    hue = (math.sin(t * 0.5) + 1) / 2  # dao động giữa 0-1
    r, g, b = colorsys.hsv_to_rgb(hue * 0.97, 1, 1)
    color = (int(r * 255), int(g * 100 + 50), int(b * 255))

    # Vẽ trái tim phát sáng
    draw_glow_heart(13, color, pulse)
    draw_heart(13, (255, 0, 60), pulse)

    # Chữ ở dưới
    font = pygame.font.SysFont("Arial", 36, bold=True)
    text = font.render("Le Thanh Danh 💓", True, (255, 180, 200))
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT - 70))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
