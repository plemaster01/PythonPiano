import pygame
import piano_lists as pl
from pygame import mixer

pygame.init()
pygame.mixer.set_num_channels(50)

font = pygame.font.Font('assets/Terserah.ttf', 48)
medium_font = pygame.font.Font('assets/Terserah.ttf', 28)
small_font = pygame.font.Font('assets/Terserah.ttf', 16)
real_small_font = pygame.font.Font('assets/Terserah.ttf', 10)
fps = 60
timer = pygame.time.Clock()
WIDTH = 52 * 35
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
white_sounds = []
black_sounds = []
active_whites = []
active_blacks = []
left_oct = 4
right_oct = 5

left_hand = pl.left_hand
right_hand = pl.right_hand
piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels

for i in range(len(white_notes)):
    white_sounds.append(mixer.Sound(f'assets\\notes\\{white_notes[i]}.wav'))

for i in range(len(black_notes)):
    black_sounds.append(mixer.Sound(f'assets\\notes\\{black_notes[i]}.wav'))

pygame.display.set_caption("Pete's Python Piano")


def draw_piano(whites, blacks):
    white_rects = []
    for i in range(52):
        rect = pygame.draw.rect(screen, 'white', [i * 35, HEIGHT - 300, 35, 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i * 35, HEIGHT - 300, 35, 300], 2, 2)
        key_label = small_font.render(white_notes[i], True, 'black')
        screen.blit(key_label, (i * 35 + 3, HEIGHT - 20))
    skip_count = 0
    last_skip = 2
    skip_track = 2
    black_rects = []
    for i in range(36):
        rect = pygame.draw.rect(screen, 'black', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 0, 2)
        for q in range(len(blacks)):
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(screen, 'green', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 2, 2)
                    blacks[q][1] -= 1

        key_label = real_small_font.render(black_labels[i], True, 'white')
        screen.blit(key_label, (25 + (i * 35) + (skip_count * 35), HEIGHT - 120))
        black_rects.append(rect)
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1

    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, 'green', [j * 35, HEIGHT - 100, 35, 100], 2, 2)
            whites[i][1] -= 1

    return white_rects, black_rects, whites, blacks


def draw_hands(rightOct, leftOct, rightHand, leftHand):
    # left hand
    pygame.draw.rect(screen, 'dark gray', [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, 'black', [(leftOct * 245) - 175, HEIGHT - 60, 245, 30], 4, 4)
    text = small_font.render(leftHand[0], True, 'white')
    screen.blit(text, ((leftOct * 245) - 165, HEIGHT - 55))
    text = small_font.render(leftHand[2], True, 'white')
    screen.blit(text, ((leftOct * 245) - 130, HEIGHT - 55))
    text = small_font.render(leftHand[4], True, 'white')
    screen.blit(text, ((leftOct * 245) - 95, HEIGHT - 55))
    text = small_font.render(leftHand[5], True, 'white')
    screen.blit(text, ((leftOct * 245) - 60, HEIGHT - 55))
    text = small_font.render(leftHand[7], True, 'white')
    screen.blit(text, ((leftOct * 245) - 25, HEIGHT - 55))
    text = small_font.render(leftHand[9], True, 'white')
    screen.blit(text, ((leftOct * 245) + 10, HEIGHT - 55))
    text = small_font.render(leftHand[11], True, 'white')
    screen.blit(text, ((leftOct * 245) + 45, HEIGHT - 55))
    text = small_font.render(leftHand[1], True, 'black')
    screen.blit(text, ((leftOct * 245) - 148, HEIGHT - 55))
    text = small_font.render(leftHand[3], True, 'black')
    screen.blit(text, ((leftOct * 245) - 113, HEIGHT - 55))
    text = small_font.render(leftHand[6], True, 'black')
    screen.blit(text, ((leftOct * 245) - 43, HEIGHT - 55))
    text = small_font.render(leftHand[8], True, 'black')
    screen.blit(text, ((leftOct * 245) - 8, HEIGHT - 55))
    text = small_font.render(leftHand[10], True, 'black')
    screen.blit(text, ((leftOct * 245) + 27, HEIGHT - 55))
    # right hand
    pygame.draw.rect(screen, 'dark gray', [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 0, 4)
    pygame.draw.rect(screen, 'black', [(rightOct * 245) - 175, HEIGHT - 60, 245, 30], 4, 4)
    text = small_font.render(rightHand[0], True, 'white')
    screen.blit(text, ((rightOct * 245) - 165, HEIGHT - 55))
    text = small_font.render(rightHand[2], True, 'white')
    screen.blit(text, ((rightOct * 245) - 130, HEIGHT - 55))
    text = small_font.render(rightHand[4], True, 'white')
    screen.blit(text, ((rightOct * 245) - 95, HEIGHT - 55))
    text = small_font.render(rightHand[5], True, 'white')
    screen.blit(text, ((rightOct * 245) - 60, HEIGHT - 55))
    text = small_font.render(rightHand[7], True, 'white')
    screen.blit(text, ((rightOct * 245) - 25, HEIGHT - 55))
    text = small_font.render(rightHand[9], True, 'white')
    screen.blit(text, ((rightOct * 245) + 10, HEIGHT - 55))
    text = small_font.render(rightHand[11], True, 'white')
    screen.blit(text, ((rightOct * 245) + 45, HEIGHT - 55))
    text = small_font.render(rightHand[1], True, 'black')
    screen.blit(text, ((rightOct * 245) - 148, HEIGHT - 55))
    text = small_font.render(rightHand[3], True, 'black')
    screen.blit(text, ((rightOct * 245) - 113, HEIGHT - 55))
    text = small_font.render(rightHand[6], True, 'black')
    screen.blit(text, ((rightOct * 245) - 43, HEIGHT - 55))
    text = small_font.render(rightHand[8], True, 'black')
    screen.blit(text, ((rightOct * 245) - 8, HEIGHT - 55))
    text = small_font.render(rightHand[10], True, 'black')
    screen.blit(text, ((rightOct * 245) + 27, HEIGHT - 55))


def draw_title_bar():
    instruction_text = medium_font.render('Up/Down Arrows Change Left Hand', True, 'black')
    screen.blit(instruction_text, (WIDTH - 500, 10))
    instruction_text2 = medium_font.render('Left/Right Arrows Change Right Hand', True, 'black')
    screen.blit(instruction_text2, (WIDTH - 500, 50))
    img = pygame.transform.scale(pygame.image.load('assets/logo.png'), [150, 150])
    screen.blit(img, (-20, -30))
    title_text = font.render('Python Programmable Piano!', True, 'white')
    screen.blit(title_text, (298, 18))
    title_text = font.render('Python Programmable Piano!', True, 'black')
    screen.blit(title_text, (300, 20))


run = True
while run:
    left_dict = {'Z': f'C{left_oct}',
                 'S': f'C#{left_oct}',
                 'X': f'D{left_oct}',
                 'D': f'D#{left_oct}',
                 'C': f'E{left_oct}',
                 'V': f'F{left_oct}',
                 'G': f'F#{left_oct}',
                 'B': f'G{left_oct}',
                 'H': f'G#{left_oct}',
                 'N': f'A{left_oct}',
                 'J': f'A#{left_oct}',
                 'M': f'B{left_oct}'}

    right_dict = {'R': f'C{right_oct}',
                  '5': f'C#{right_oct}',
                  'T': f'D{right_oct}',
                  '6': f'D#{right_oct}',
                  'Y': f'E{right_oct}',
                  'U': f'F{right_oct}',
                  '8': f'F#{right_oct}',
                  'I': f'G{right_oct}',
                  '9': f'G#{right_oct}',
                  'O': f'A{right_oct}',
                  '0': f'A#{right_oct}',
                  'P': f'B{right_oct}'}
    timer.tick(fps)
    screen.fill('gray')
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
    draw_hands(right_oct, left_oct, right_hand, left_hand)
    draw_title_bar()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            black_key = False
            for i in range(len(black_keys)):
                if black_keys[i].collidepoint(event.pos):
                    black_sounds[i].play(0, 1000)
                    black_key = True
                    active_blacks.append([i, 30])
            for i in range(len(white_keys)):
                if white_keys[i].collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0, 3000)
                    active_whites.append([i, 30])
        if event.type == pygame.TEXTINPUT:
            if event.text.upper() in left_dict:
                if left_dict[event.text.upper()][1] == '#':
                    index = black_labels.index(left_dict[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                else:
                    index = white_notes.index(left_dict[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])
            if event.text.upper() in right_dict:
                if right_dict[event.text.upper()][1] == '#':
                    index = black_labels.index(right_dict[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                else:
                    index = white_notes.index(right_dict[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if right_oct < 8:
                    right_oct += 1
            if event.key == pygame.K_LEFT:
                if right_oct > 0:
                    right_oct -= 1
            if event.key == pygame.K_UP:
                if left_oct < 8:
                    left_oct += 1
            if event.key == pygame.K_DOWN:
                if left_oct > 0:
                    left_oct -= 1

    pygame.display.flip()
pygame.quit()
