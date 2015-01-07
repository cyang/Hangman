# Christopher Yang
# Please have internet connection before running

import random
import pygame
import re
import urllib2

number_of_tries = 6
constantNumberOfTries = number_of_tries
word = ''
dashes = ''
copy = ''

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 150, 0)
red = (255, 0 , 0)

quit_status = False
win = False
gameOverStatus = False
constantGameOverStatus = gameOverStatus

screen_width = 800
screen_height = 600

pygame.font.init()

font1 = pygame.font.SysFont("arial", 20)
font2 = pygame.font.SysFont("arial", 11)
font3 = pygame.font.SysFont("arial", 15)

class letter:
    def __init__(self):
        self.pressed = 0


def getWord():
    file_handle = open('wordList.txt')
    file_line_list = file_handle.readlines()

    number_of_lines = 0

    for line in file_line_list:
        number_of_lines += 1

    random_line = random.randrange(0,number_of_lines)

    file_handle.close()
    foundWord = file_line_list[random_line]

    returnWord = ''

    for char in foundWord:
        if char != '\n':
            returnWord += char

    return returnWord


def getHint(word):
    searching = word

    word = urllib2.urlopen("http://dictionary.reference.com/browse/" + searching + "?s=t")
    word = word.read()

    items=re.findall('<meta name="description" content="'+".*$",word,re.MULTILINE)

    for word in items:
        y=word.replace('<meta name="description" content="','')
        z=y.replace(' See more."/>','')
        m=re.findall('at Dictionary.com, a free online dictionary with pronunciation, synonyms and translation. Look it up now! "/>',z)
        if m==[]:
            hint = ""

            for char in range(0, len(z)):
                if z[char] == ',':
                    hint = z[char+2:]
                    break

            for char in range(0, len(hint)):
                if hint[char] == '<' or hint[char] == ':':
                    hint = hint[0:char]
                    break

            return hint


def titleScreen(quit_status):
    while not quit_status:

        game_screen.fill(white)

        titleMessage1 = font1.render("Welcome to Hangman!", True, (black))
        titleMessage2 = font2.render("Press any key to continue", True, (black))

        textrect1 = titleMessage1.get_rect()

        textrect1.centerx = game_screen.get_rect().centerx
        textrect1.centery = game_screen.get_rect().centery

        textrect2 = titleMessage1.get_rect()

        textrect2.centerx = game_screen.get_rect().centerx
        textrect2.centery = game_screen.get_rect().centery + 20

        game_screen.blit(titleMessage1, textrect1)
        game_screen.blit(titleMessage2, textrect2)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_status = True
                return quit_status
            elif event.type == pygame.KEYUP:
                quit_status = False
                return quit_status


def drawHangMan(number_of_tries, gameOverStatus):
    middleOfTorso = (screen_width/2 + 77.5 ,screen_height/2 - 60)
    endOfTorso = (screen_width/2 + 77.5 ,screen_height/2 + 34)

    leftArmPoint = (450, screen_height/2)
    rightArmPoint = (500, screen_height/2)

    leftLegPoint = (450, screen_height/2 + 100)
    rightLegPoint = (500, screen_height/2 + 100)


    if number_of_tries == 6:
        base = pygame.draw.rect(game_screen, black, (screen_width/2 - 75 ,screen_height/2 + 150, 200, 5), 0)
        scaffold = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 + 150, 5, -300), 0)
        hinge = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 - 155, 100, 5) , 0)
        rope = pygame.draw.rect(game_screen, black, (screen_width/2 + 75 ,screen_height/2 -155, 5, 25) , 0)

    elif number_of_tries == 5:
        base = pygame.draw.rect(game_screen, black, (screen_width/2 - 75 ,screen_height/2 + 150, 200, 5), 0)
        scaffold = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 + 150, 5, -300), 0)
        hinge = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 - 155, 100, 5) , 0)
        rope = pygame.draw.rect(game_screen, black, (screen_width/2 + 75 ,screen_height/2 -155, 5, 25) , 0)

        head = pygame.draw.circle(game_screen, red, (screen_width/2 + 77, screen_height/2 - 110), 25, 5)

    elif number_of_tries == 4:
        base = pygame.draw.rect(game_screen, black, (screen_width/2 - 75 ,screen_height/2 + 150, 200, 5), 0)
        scaffold = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 + 150, 5, -300), 0)
        hinge = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 - 155, 100, 5) , 0)
        rope = pygame.draw.rect(game_screen, black, (screen_width/2 + 75 ,screen_height/2 -155, 5, 25) , 0)

        head = pygame.draw.circle(game_screen, red, (screen_width/2 + 77, screen_height/2 - 110), 25, 5)
        torso = pygame.draw.rect(game_screen, red, (screen_width/2 + 75 ,screen_height/2 - 85, 5, 125), 0)

    elif number_of_tries == 3:
        base = pygame.draw.rect(game_screen, black, (screen_width/2 - 75 ,screen_height/2 + 150, 200, 5), 0)
        scaffold = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 + 150, 5, -300), 0)
        hinge = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 - 155, 100, 5) , 0)
        rope = pygame.draw.rect(game_screen, black, (screen_width/2 + 75 ,screen_height/2 -155, 5, 25) , 0)

        head = pygame.draw.circle(game_screen, red, (screen_width/2 + 77, screen_height/2 - 110), 25, 5)
        torso = pygame.draw.rect(game_screen, red, (screen_width/2 + 75 ,screen_height/2 - 85, 5, 125), 0)

        pygame.draw.line(game_screen, red, middleOfTorso, leftArmPoint, 5)

    elif number_of_tries == 2:
        base = pygame.draw.rect(game_screen, black, (screen_width/2 - 75 ,screen_height/2 + 150, 200, 5), 0)
        scaffold = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 + 150, 5, -300), 0)
        hinge = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 - 155, 100, 5) , 0)
        rope = pygame.draw.rect(game_screen, black, (screen_width/2 + 75 ,screen_height/2 -155, 5, 25) , 0)

        head = pygame.draw.circle(game_screen, red, (screen_width/2 + 77, screen_height/2 - 110), 25, 5)
        torso = pygame.draw.rect(game_screen, red, (screen_width/2 + 75 ,screen_height/2 - 85, 5, 125), 0)

        pygame.draw.line(game_screen, red, middleOfTorso, leftArmPoint, 5)
        pygame.draw.line(game_screen, red, middleOfTorso, rightArmPoint, 5)

    elif number_of_tries == 1:
        base = pygame.draw.rect(game_screen, black, (screen_width/2 - 75 ,screen_height/2 + 150, 200, 5), 0)
        scaffold = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 + 150, 5, -300), 0)
        hinge = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 - 155, 100, 5) , 0)
        rope = pygame.draw.rect(game_screen, black, (screen_width/2 + 75 ,screen_height/2 -155, 5, 25) , 0)

        head = pygame.draw.circle(game_screen, red, (screen_width/2 + 77, screen_height/2 - 110), 25, 5)
        torso = pygame.draw.rect(game_screen, red, (screen_width/2 + 75 ,screen_height/2 - 85, 5, 125), 0)

        pygame.draw.line(game_screen, red, middleOfTorso, leftArmPoint, 5)
        pygame.draw.line(game_screen, red, middleOfTorso, rightArmPoint, 5)

        pygame.draw.line(game_screen, red, endOfTorso, leftLegPoint, 5)

    elif number_of_tries == 0:
        base = pygame.draw.rect(game_screen, black, (screen_width/2 - 75 ,screen_height/2 + 150, 200, 5), 0)
        scaffold = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 + 150, 5, -300), 0)
        hinge = pygame.draw.rect(game_screen, black, (screen_width/2 - 25 ,screen_height/2 - 155, 100, 5) , 0)
        rope = pygame.draw.rect(game_screen, black, (screen_width/2 + 75 ,screen_height/2 -155, 5, 25) , 0)

        head = pygame.draw.circle(game_screen, red, (screen_width/2 + 77, screen_height/2 - 110), 25, 5)
        torso = pygame.draw.rect(game_screen, red, (screen_width/2 + 75 ,screen_height/2 - 85, 5, 125), 0)

        pygame.draw.line(game_screen, red, middleOfTorso, leftArmPoint, 5)
        pygame.draw.line(game_screen, red, middleOfTorso, rightArmPoint, 5)

        pygame.draw.line(game_screen, red, endOfTorso, leftLegPoint, 5)
        pygame.draw.line(game_screen, red, endOfTorso, rightLegPoint, 5)


        gameOverStatus = True
        return gameOverStatus


def mainGame(dashes, number_of_tries, gameOverStatus, quit_status):
    count = 0
    countSpace = 0
    incorrect = ''

    word = getWord()

    hint = getHint(word)

    number_of_dashes = len(word)
    for dash in range(0, number_of_dashes):
       dashes += " _"

    a = letter()
    b = letter()
    c = letter()
    d = letter()
    e = letter()
    f = letter()
    g = letter()
    h = letter()
    i = letter()
    j = letter()
    k = letter()
    l = letter()
    m = letter()
    n = letter()
    o = letter()
    p = letter()
    q = letter()
    r = letter()
    s = letter()
    t = letter()
    u = letter()
    v = letter()
    w = letter()
    x = letter()
    y = letter()
    z = letter()

    while not quit_status:

        game_screen.fill(white)

        if countSpace == 0:
            game_screen.blit(font2.render("Press spacebar for a hint", True, (black)),(30,50))

        else:
            game_screen.blit(font2.render("hint: " + hint, True, (black)),(30,50))

        game_screen.blit(font1.render("Guess this word: ", True, (black)),(30, screen_height-50))
        game_screen.blit(font1.render("Number of tries left: %d" % number_of_tries, True, (black)),(30,30))
        game_screen.blit(font1.render(dashes, True, (black)),(200,screen_height-50))

        game_screen.blit(font1.render("Incorrect letters: " + incorrect, True, (red)),(30,60))

        if count == 0:
            game_screen.blit(font2.render("Press a letter case to guess the word!", True, (black)), (30, screen_height-20))

        if checkwin(dashes, word):
            quit_status = gameWon(quit_status, word)
            return quit_status


        if gameOverStatus == True:
            quit_status = gameOver(quit_status)
            return quit_status

        gameOverStatus = drawHangMan(number_of_tries, gameOverStatus)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit_status = True
                return quit_status
            elif event.type == pygame.KEYUP:
                count += 1
                if event.key == pygame.K_SPACE:
                    countSpace += 1

                elif event.key == pygame.K_a:
                    if a.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'a', dashes, copy, number_of_tries, incorrect)
                        a.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_b:
                    if b.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'b', dashes, copy, number_of_tries, incorrect)
                        b.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_c:
                    if c.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'c', dashes, copy, number_of_tries, incorrect)
                        c.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_d:
                    if d.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'d', dashes, copy, number_of_tries, incorrect)
                        d.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_e:
                    if e.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'e', dashes, copy, number_of_tries, incorrect)
                        e.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_f:
                    if f.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'f', dashes, copy, number_of_tries, incorrect)
                        f.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_g:
                    if g.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'g', dashes, copy, number_of_tries, incorrect)
                        g.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_h:
                    if h.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'h', dashes, copy, number_of_tries, incorrect)
                        h.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_i:
                    if i.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'i', dashes, copy, number_of_tries, incorrect)
                        i.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_j:
                    if j.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'j', dashes, copy, number_of_tries, incorrect)
                        j.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_k:
                    if k.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'k', dashes, copy, number_of_tries, incorrect)
                        k.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_l:
                    if l.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'l', dashes, copy, number_of_tries, incorrect)
                        l.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_m:
                    if m.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'m', dashes, copy, number_of_tries, incorrect)
                        m.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_n:
                    if n.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'n', dashes, copy, number_of_tries, incorrect)
                        n.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_o:
                    if o.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'o', dashes, copy, number_of_tries, incorrect)
                        o.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_p:
                    if p.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'p', dashes, copy, number_of_tries, incorrect)
                        p.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_q:
                    if q.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'q', dashes, copy, number_of_tries, incorrect)
                        q.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_r:
                    if r.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'r', dashes, copy, number_of_tries, incorrect)
                        r.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_s:
                    if s.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'s', dashes, copy, number_of_tries, incorrect)
                        s.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_t:
                    if t.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'t', dashes, copy, number_of_tries, incorrect)
                        t.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_u:
                    if u.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'u', dashes, copy, number_of_tries, incorrect)
                        u.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_v:
                    if v.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'v', dashes, copy, number_of_tries, incorrect)
                        v.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_w:
                    if w.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'w', dashes, copy, number_of_tries, incorrect)
                        w.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_x:
                    if x.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'x', dashes, copy, number_of_tries, incorrect)
                        x.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_y:
                    if y.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'y', dashes, copy, number_of_tries, incorrect)
                        y.pressed += 1
                    else:
                        pass
                elif event.key == pygame.K_z:
                    if z.pressed == 0:
                        dashes, number_of_tries, incorrect = checkLetters(word,'z', dashes, copy, number_of_tries, incorrect)
                        z.pressed += 1
                    else:
                        pass


                pygame.display.update()


def checkLetters(word, letter, dashes, copy, number_of_tries, incorrect):
    doesContain = False

    for char in range(0, len(word)):
        if word[char] == letter:
            copy += " " + letter
            doesContain = True
        else:
            copy += " " + dashes[(char*2)+1]

    if doesContain == False:
        number_of_tries -= 1
        incorrect += letter
        incorrect += ' '

    return copy, number_of_tries, incorrect


def checkwin(dashes, word):
    removeSpaces = ''
    for char in range(0, len(dashes)):
        if dashes[char] != " ":
            removeSpaces += dashes[char]

    if word == removeSpaces:
        return True
    else:
        return False


def gameOver(quit_status):

    while not quit_status:
        game_screen.fill(white)

        gameOverMessage1 = font1.render("Game Over", True, (red))
        gameOverMessage2 = font2.render("Press any key to replay!", True, (black))

        textrect1 = gameOverMessage1.get_rect()
        textrect2 = gameOverMessage2.get_rect()


        textrect1.centerx = game_screen.get_rect().centerx
        textrect1.centery = game_screen.get_rect().centery

        textrect2.centerx = game_screen.get_rect().centerx
        textrect2.centery = game_screen.get_rect().centery + 20


        game_screen.blit(gameOverMessage1, textrect1)
        game_screen.blit(gameOverMessage2, textrect2)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_status = True
                return quit_status
            elif event.type == pygame.KEYUP:
                return


def gameWon(quit_status, word):
    while not quit_status:
        game_screen.fill(white)

        gameWinMessage1 = font1.render("You Win!", True, (green))
        gameWinMessage2 = font3.render("Word guessed: " + word, True, (black))
        gameWinMessage3 = font2.render("Press any key to replay!", True, (black))

        textrect1 = gameWinMessage1.get_rect()
        textrect2 = gameWinMessage1.get_rect()
        textrect3 = gameWinMessage1.get_rect()

        textrect1.centerx = game_screen.get_rect().centerx
        textrect1.centery = game_screen.get_rect().centery

        textrect2.centerx = game_screen.get_rect().centerx - 20
        textrect2.centery = game_screen.get_rect().centery + 20

        textrect3.centerx = game_screen.get_rect().centerx - 20
        textrect3.centery = game_screen.get_rect().centery + 37


        game_screen.blit(gameWinMessage1, textrect1)
        game_screen.blit(gameWinMessage2, textrect2)
        game_screen.blit(gameWinMessage3, textrect3)


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_status = True
                return quit_status
            elif event.type == pygame.KEYUP:
                return


def mainLoop():
    quit_status = False
    quit_status = titleScreen(quit_status)

    while not quit_status:
        quit_status = mainGame(dashes, number_of_tries, gameOverStatus, quit_status)

    pygame.quit()


pygame.init()
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Hangman')

mainLoop()