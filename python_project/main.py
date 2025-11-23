#pgzero
import random

# Игровое окно
cell = Actor('border')
cell1 = Actor('floor')
cell2 = Actor("gold")
cell3 = Actor("diamond")
button1 = Actor("buttons33",(230, 210))
button2 = Actor("buttons33",(230, 280))
button3 = Actor("buttons33",(230, 350))
size_w = 9 # Ширина поля в клетках
size_h = 10 # Высота поля в клетках
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h

is_question = 0

win = 0
mode = "game"
colli = 0

TITLE = "Minecraft" # Заголовок окна игры
FPS = 30 # Количество кадров в секунду
my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 3, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 2, 1, 3, 1, 1, 0], 
          [0, 1, 1, 1, 2, 1, 1, 1, 0], 
          [0, 1, 3, 2, 1, 1, 3, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 3, 0], 
          [0, 1, 1, 3, 1, 1, 2, 1, 0], 
          [0, 2, 1, 1, 1, 1, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]] # Строка с атакой и здоровьем

char = Actor("stevee")
char.top = cell.height
char.left = cell.width
char.health = 1000
char.attack = 5

#Генерация врагов
enemies = []

for i in range(5):
    x = random.randint(1, 7) * cell.width
    y = random.randint(1, 7) * cell.height
    enemy = Actor("zombie", topleft = (x, y))
    enemy.health = random.randint(10, 20)
    enemy.attack = random.randint(5, 10)
    enemy.bonus = random.randint(0, 2)
    enemies.append(enemy)

lvl = 1

# Бонусы
hearts = []  
bombs = []
questions = []

questions.append({
    "text": "Как называется функция для рисования в PgZero?",
    "option1": "show()",
    "option2": "paint()",
    "option3": "draw()",
    "correct_answer": 3
})

questions.append({
    "text": "Как описать размер экрана?",
    "option1": "size",
    "option2": "WIDTH и HEIGHT",
    "option3": "screen_size",
    "correct_answer": 2
})

questions.append({
    "text": "Где создаются игровые спрайты?",
    "option1": "Actor()",
    "option2": "Player()",
    "option3": "Object()",
    "correct_answer": 1
})

questions.append({
    "text": "Как обновлять координаты объекта?",
    "option1": "update()",
    "option2": "draw()",
    "option3": "refresh()",
    "correct_answer": 1
})

questions.append({
    "text": "Что делает функция screen.clear()?",
    "option1": "Очищает экран",
    "option2": "Добавляет спрайт",
    "option3": "Воспроизводит звук",
    "correct_answer": 1
})

questions.append({
    "text": "Угадай цифру",
    "option1": "69",
    "option2": "1402",
    "option3": "2",
    "correct_answer": 3
})

questions.append({
    "text": "Как отобразить надпись на экране?",
    "option1": "show_text()",
    "option2": "screen.draw.text()",
    "option3": "print_on_screen()",
    "correct_answer": 2
})

questions.append({
    "text": "Что такое update() в PgZero?",
    "option1": "Система обновления PgZero",
    "option2": "Функция, вызываемая каждый кадр",
    "option3": "Модуль для обновлений",
    "correct_answer": 2
})

questions.append({
    "text": "Какой метод используется для рисования?",
    "option1": "show()",
    "option2": "draw()",
    "option3": "place()",
    "correct_answer": 2
})

current_question = {}

def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()  
            elif my_map[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw() 

#Отрисовка
def draw():
    if mode == 'game':
        screen.fill("#2f3542")
        map_draw()
        char.draw()
        screen.draw.text("HP:", center=(25, 455), color = 'white', fontsize = 20)
        screen.draw.text(char.health, center=(75, 455), color = 'white', fontsize = 20)
        screen.draw.text("AP:", center=(375, 455), color = 'white', fontsize = 20)
        screen.draw.text(char.attack, center=(425, 455), color = 'white', fontsize = 20)
        for i in range(len(enemies)):
            enemies[i].draw()
            #Отрисовка здоровья врага
            screen.draw.text(enemies[i].health, center=(enemies[i].x + 5, enemies[i].y - 35), color='white', fontsize=18)
            screen.draw.text(enemies[i].attack, center=(enemies[i].x - 20, enemies[i].y - 35), color='red', fontsize=18)
        
            #отрисовка бонусов
        for i in range(len(hearts)):
            hearts[i].draw()
        for i in range(len(bombs)):
            bombs[i].draw()
        screen.draw.text("Level: " + str(lvl), center=(225, 455), color='yellow', fontsize=18)

        if is_question == 1:
            screen.draw.text(current_question["text"], center=(230, 150), color='white', fontsize=20)
            button1.draw()
            screen.draw.text(current_question["option1"], center=(230, 210), color='black', fontsize=19)
            button2.draw()
            screen.draw.text(current_question["option2"], center=(230, 280), color='black', fontsize=19)
            button3.draw()
            screen.draw.text(current_question["option3"], center=(230, 350), color='black', fontsize=19)
        #Окно победы или поражения    
    elif mode == "end":
        screen.fill("#2f3542")
        if win == 1:
            screen.draw.text("Победа!", center=(WIDTH/2, HEIGHT/2), color = 'white', fontsize = 46)
        else:
            screen.draw.text("Поражение!", center=(WIDTH/2, HEIGHT/2), color = 'white', fontsize = 46)
#Управление
def on_key_down(key):
    global colli
    if is_question == 1:
        return
    old_x = char.x
    old_y = char.y
    if keyboard.right and char.x + cell.width < WIDTH - cell.width:
        char.x += cell.width
        char.image = 'stevee'
    elif keyboard.left and char.x - cell.width > cell.width:
        char.x -= cell.width
        char.image = 'stevee'
    elif keyboard.down and char.y + cell.height < HEIGHT - cell.height*2:
        char.y += cell.height
    elif keyboard.up and char.y - cell.height > cell.height:
        char.y -= cell.height

        #Столкновение с врагами
    enemy_index = char.collidelist(enemies)
    if enemy_index != -1:
        char.x = old_x
        char.y = old_y
        colli = 1
        enemy = enemies[enemy_index]
        enemy.health -= char.attack
        char.health -= enemy.attack
        if enemy.health <= 0:
            #Добавление бонусов
            if enemy.bonus == 1:
                heart = Actor('heart')
                heart.pos = enemy.pos
                hearts.append(heart)
            elif enemy.bonus == 2:
                bomb = Actor('stevee')
                bomb.pos = enemy.pos
                bombs.append(bomb)
            enemies.pop(enemy_index)



def update(dt):
    global enemies
    if is_question == 0:
        victory()
        for i in range(len(hearts)):
            if char.colliderect(hearts[i]):
                char.health += 15
                hearts.pop(i)
                break
        for i in range(len(bombs)):
            if char.colliderect(bombs[i]):
                enemies = []
                bombs.pop(i)
                break
#Логика победы или поражения
def victory():
    global mode, win, lvl, is_question, current_question
    if enemies == [] and char.health > 0 and is_question == 0:
        is_question = 1
        current_question = random.choice(questions)
    elif char.health <= 0:
        mode = "end"
        win = -1

def on_mouse_down(button, pos):
    global is_question, mode, win, lvl, enemies
    if is_question == 0:
        return
    answer = 0
    if button == mouse.LEFT:
        if button1.collidepoint(pos):
            answer = 1
        elif button2.collidepoint(pos):
            answer = 2
        elif button3.collidepoint(pos):
            answer = 3
        if answer == 0:
            return
        if answer == current_question["correct_answer"]:
            is_question = 0
            lvl += 1
            for i in range(5):
                x = random.randint(1, 7) * cell.width
                y = random.randint(1, 7) * cell.height
                enemy = Actor("zombie", topleft=(x, y))
                enemy.health = random.randint(10, 20)
                enemy.attack = random.randint(5, 10)
                enemy.bonus = random.randint(0, 3)
                enemies.append(enemy)
        else:
            is_question = 0
            mode = "end"
            win = -1