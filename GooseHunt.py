from pygame import*
init()

width = 300
height = 600

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 102, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

mx = 0
my = 0

SIZE = (width, height)
screen = display.set_mode(SIZE)

rectPlay = Rect(width/4, height/4, width/2, height/6)
rectMiddle  = Rect(width/4, height/2, width/2, height/6)
rectQuit = Rect(width/4, height/(4/3), width/2, height/6) 

running = True

def MenuDraw():
    fontTitle = font.SysFont("Arial", width//16)	
    titleText = fontTitle.render("Goose Hunt", 1, WHITE)
    titleSize = fontTitle.size("Goose Hunt")
  
    fontMenu = font.SysFont("Arial", width//15)	
    menuText1 = fontMenu.render("Play Game", 1, BLACK)
    menuText2 = fontMenu.render("How to Play", 1, BLACK)
    menuText3 = fontMenu.render("Exit Game", 1, BLACK)
    text1Size = fontMenu.size("Play Game")
    text2Size = fontMenu.size("How to Play")
    text3Size = fontMenu.size("Exit Game")
    
    startRect = Rect(width/4, height/4, width/2, height/6)
    howRect  = Rect(width/4, height/2, width/2, height/6)
    exitRect = Rect(width/4, height/(4/3), width/2, height/6) 
    
    colMenu1 = WHITE
    colMenu2 = WHITE
    colMenu3 = WHITE   
     
    screen.blit(titleText, (width/2 - titleSize[0]/2, height/10 - titleSize[1]/2, titleSize[0], titleSize[1]))
    draw.rect(screen, colMenu1, startRect)
    screen.blit(menuText1, (width/2 - text1Size[0]/2, height/4 + height/10 - text1Size[1]/2, text1Size[0], text1Size[1]))
    draw.rect(screen, colMenu2, howRect)
    screen.blit(menuText2, (width/2 - text2Size[0]/2, height/2 + height/10 - text2Size[1]/2, text1Size[0], text1Size[1]))
    draw.rect(screen, colMenu3, exitRect)
    screen.blit(menuText3, (width/2 - text3Size[0]/2, height/(4/3) + height/10 - text3Size[1]/2, text1Size[0], text1Size[1]))   
    
while running:
    MenuDraw()
    display.flip()
    for evt in event.get():
        if evt.type == QUIT:
            running = False        
            
quit()