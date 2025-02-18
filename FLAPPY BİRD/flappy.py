import pygame

# Pygame başlat
pygame.init()

# Ekran boyutu
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Klonu")

# FPS ve font ayarları
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# **Menü değişkenleri**
menu_active = True
game_active = False
settings_active = False
difficulty_active = False
info_active = False

# **Ses ayarları**
sound_enabled = True
music_enabled = True
animation_sound_enabled = True

# **Zorluk seviyeleri**
difficulty = "Orta"

# **Hitboxlar (Buton Alanları)**
button_start = pygame.Rect(100, 200, 200, 40)
button_settings = pygame.Rect(100, 250, 200, 40)
button_difficulty = pygame.Rect(100, 300, 200, 40)
button_info = pygame.Rect(100, 350, 200, 40)

# **Menü Gösterme Fonksiyonları**
def show_menu():
    screen.fill((50, 50, 50))
    title_text = font.render("FLAPPY BIRD", True, (255, 255, 0))
    pygame.draw.rect(screen, (100, 100, 100), button_start, border_radius=10)  # Hitbox göster
    pygame.draw.rect(screen, (100, 100, 100), button_settings, border_radius=10)
    pygame.draw.rect(screen, (100, 100, 100), button_difficulty, border_radius=10)
    pygame.draw.rect(screen, (100, 100, 100), button_info, border_radius=10)

    screen.blit(title_text, (SCREEN_WIDTH // 2 - 80, 100))
    screen.blit(font.render("1 - Başlat", True, (255, 255, 255)), (button_start.x + 60, button_start.y + 10))
    screen.blit(font.render("2 - Ayarlar", True, (255, 255, 255)), (button_settings.x + 60, button_settings.y + 10))
    screen.blit(font.render("3 - Zorluk", True, (255, 255, 255)), (button_difficulty.x + 60, button_difficulty.y + 10))
    screen.blit(font.render("4 - Oyun Bilgisi", True, (255, 255, 255)), (button_info.x + 40, button_info.y + 10))

    pygame.display.update()

# **Ana Döngü**
running = True
while running:
    if menu_active:
        show_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if menu_active:
                if event.key == pygame.K_1:
                    menu_active = False
                    game_active = True
                elif event.key == pygame.K_2:
                    menu_active = False
                    settings_active = True
                elif event.key == pygame.K_3:
                    menu_active = False
                    difficulty_active = True
                elif event.key == pygame.K_4:
                    menu_active = False
                    info_active = True
        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse tıklama algılama
            x, y = pygame.mouse.get_pos()
            if button_start.collidepoint(x, y):  # Başlat Butonu
                menu_active = False
                game_active = True
            elif button_settings.collidepoint(x, y):  # Ayarlar Butonu
                menu_active = False
                settings_active = True
            elif button_difficulty.collidepoint(x, y):  # Zorluk Butonu
                menu_active = False
                difficulty_active = True
            elif button_info.collidepoint(x, y):  # Oyun Bilgisi Butonu
                menu_active = False
                info_active = True

    pygame.display.update()
    clock.tick(30)

pygame.quit()
