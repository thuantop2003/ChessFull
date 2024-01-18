import pygame as pg
import chesspieces as cp
board=cp.makeBoard();
print(board);
pg.init()
pg.display.set_caption("ChessProject1")
WIDTH=1000
HEIGHT=900
screen = pg.display.set_mode([WIDTH,HEIGHT])
font = pg.font.Font('freesansbold.ttf',50)
font1 = pg.font.Font('freesansbold.ttf',18)
timer = pg.time.Clock()
fps = 60
#0- white no select, 1- white with select, 2 black no select, 3 black with select
turn_selection=0
run=True
valid_moves = []
mode=None
button_pvp_rect = pg.Rect(825, 50, 150, 50)
button_pvp_text = font.render('PvP',True, 'black')
pvp_text_rect = button_pvp_text.get_rect(center=button_pvp_rect.center)

button_pvb_rect = pg.Rect(825, 150, 150, 50)
button_pvb_text = font.render('PvB',True, 'black')
pvb_text_rect = button_pvb_text.get_rect(center=button_pvb_rect.center)

button_bvb_rect = pg.Rect(825, 250, 150, 50)
button_bvb_text = font.render('BvB',True, 'black')
bvb_text_rect = button_bvb_text.get_rect(center=button_bvb_rect.center)

button_new_rect = pg.Rect(825, 350, 150, 50)
button_new_text = font.render('New',True, 'black')
new_text_rect = button_new_text.get_rect(center=button_new_rect.center)


def drawboard(pg, screen):
    for row in range(8):
        for column in range(8):
            color = 'light gray' if (row + column) % 2 == 0 else 'dark gray'
            pg.draw.rect(screen, color, [column * 100, row * 100, 100, 100])
    pg.draw.rect(screen, 'gray',[0,800,1000,100])
    pg.draw.rect(screen, 'gold',[0,800,1000,100],5)
    pg.draw.rect(screen, 'gold',[800,0,200,1000],5)
    status_text=['white select','white move','black select','black move']
    screen.blit(font.render(status_text[turn_selection],True,'black'),(20,820))
def loadimage(t):
    # Fix the path string and use double backslashes or a raw string
    image_path = r"C:\Users\Lenovo\Desktop\project1\chessAll\image\\" + t.name + ".png"
    a = pg.image.load(image_path)
    
    if t.name == "Wpawn" or t.name == "Bpawn":
        a = pg.transform.scale(a, (65, 65))
        screen.blit(a, ( (8-t.location[1] ) * 100 + 30,(8-t.location[0] ) * 100 + 22))
    else:
        a = pg.transform.scale(a, (80, 80))
        screen.blit(a, ((8-t.location[1] ) * 100 + 10,(8-t.location[0] ) * 100 + 10))
def load_chess():
    for chess in board:
        loadimage(chess)
valid_moves=[]
def draw_game_over():
    text=font.render(f'{winner} won the game', True,'blue')
    text2=font.render(f'press Enter to restart', True,'blue')
    screen.blit(text,(210,210))
    screen.blit(text2,(210,310))
def checking():
    a=0
    b=0
    for p in board:
        if p.name=="WKing":
            a=1
        if p.name=="BKing":
            b=1
    return [a,b]
def drawbutton():
    pg.draw.rect(screen, 'gray', button_pvp_rect)
    screen.blit(button_pvp_text, pvp_text_rect)
    pg.draw.rect(screen, 'gray', button_pvb_rect)
    screen.blit(button_pvb_text, pvb_text_rect)
    pg.draw.rect(screen, 'gray', button_bvb_rect)
    screen.blit(button_bvb_text, bvb_text_rect)
    pg.draw.rect(screen, 'gray', button_new_rect)
    screen.blit(button_new_text, new_text_rect)

    textmode=font1.render(f'Game Mode :{mode}',True, 'black')
    screen.blit(textmode,(825,650))
pvp=False
pvb=False
bvb=False
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    drawboard(pg,screen)
    drawbutton()
    load_chess()
    if checking()[0]==0 or checking()[1]==0:
        if(checking()[0]==0):
            winner="Black"
        else:
            winner="White"
        draw_game_over()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button ==1:
            x_coord=(event.pos[0]+75)//100
            y_coord=(event.pos[1]+50)//100
            click_coord=[y_coord,x_coord]
            print(click_coord)
            if click_coord==[1,9]:
                mode="PVP"
                pvp=True
                pvb=False
                bvb=False
            if click_coord==[2,9]:
                mode="PVB"
                pvp=False
                pvb=True
                bvb=False
            if click_coord==[3,9]:
                mode="BVB"
                pvp=False
                pvb=False
                bvb=True
            if click_coord==[4,9]:
                mode=None
                pvp=False
                pvb=False
                bvb=False
                board=board=cp.makeBoard()
                turn_selection=0
            print(pvp,pvb,bvb)
            print(mode)
        if event.type==pg.KEYDOWN and (checking()[0]==0 or checking()[1]==0):
            if event.key==pg.K_RETURN:
                board=board=cp.makeBoard()
                turn_selection=0
#PVP
        if event.type == pg.MOUSEBUTTONDOWN and event.button ==1 and checking()[0]!=0 and checking()[1]!=0 and pvp:
            x_coord=event.pos[0]//100
            y_coord=event.pos[1]//100
            click_coord=[8-y_coord,8-x_coord]
            if turn_selection==0:
                print(turn_selection)
                for chess in board: 
                    if(chess.location==click_coord and chess.name[0]=="W"):
                        selection = chess
                        turn_selection=1
                        valid_moves=cp.validmoves(selection,board)
                        print(valid_moves)
                        break
                continue
            if turn_selection==1:
                print(selection.name, selection.location)
                print(turn_selection)
                print(valid_moves)
                print(click_coord)
                if click_coord in valid_moves :
                    for chess in board:
                        if(click_coord==chess.location):
                            board.remove(chess)
                        if(chess.location[0]==selection.location[0] and chess.location[1]==selection.location[1]):
                            chess.location=click_coord
                    turn_selection=2;
                    continue
                if turn_selection==1:
                    turn_selection=0  
                    continue    
            if turn_selection==2:
                print(turn_selection)
                for chess in board: 
                    if(chess.location==click_coord and chess.name[0]=="B"):
                        selection = chess
                        turn_selection=3
                        valid_moves=cp.validmoves(selection,board)
                        print(valid_moves)
                        break
                continue
            if turn_selection==3:
                print(selection.name, selection.location)
                print(turn_selection)
                print(valid_moves)
                print(click_coord)
                if click_coord in valid_moves :
                    for chess in board:
                        if(click_coord==chess.location):
                            board.remove(chess)
                        if(chess.location[0]==selection.location[0] and chess.location[1]==selection.location[1]):
                            chess.location=click_coord
                    turn_selection=0;
                    continue
                if turn_selection==3:
                    turn_selection=2  
                    continue 
#pvb
        if event.type == pg.MOUSEBUTTONDOWN and event.button ==1 and (checking()[0]!=0 or checking()[1]!=0) and pvb:
            x_coord=event.pos[0]//100
            y_coord=event.pos[1]//100
            click_coord=[8-y_coord,8-x_coord]
            if turn_selection==0:
                #print(turn_selection)
                for chess in board: 
                    if(chess.location==click_coord and chess.name[0]=="W"):
                        selection = chess
                        turn_selection=1
                        valid_moves=cp.validmoves(selection,board)
                        #print(valid_moves)
                        break
                continue
            if turn_selection==1:
                #print(selection.name, selection.location)
                #print(turn_selection)
                #print(valid_moves)
                #print(click_coord)
                print("next")
                if click_coord in valid_moves :
                    for chess in board:
                        if(click_coord==chess.location):
                            board.remove(chess)
                            break
                    for chess in board:
                        if(chess.location[0]==selection.location[0] and chess.location[1]==selection.location[1]):
                            chess.location=click_coord
                            break
                    turn_selection=2
                    screen.fill('dark gray')
                    drawboard(pg,screen)
                    load_chess()
                    continue
                if turn_selection==1:
                    turn_selection=0  
                    continue 
    if turn_selection==2 and (checking()[0]!=0 or checking()[1]!=0) and pvb:
        board=cp.makeMove(board)
        turn_selection=0
        continue     
#bvb
    if turn_selection==0 and (checking()[0]!=0 and checking()[1]!=0) and bvb:
        board=cp.makeMoveW(board)
        turn_selection=2
        continue 
    pg.display.flip()
    if turn_selection==2 and (checking()[0]!=0 and checking()[1]!=0) and bvb:
        board=cp.makeMove(board)
        turn_selection=0
        continue     
            
    pg.display.flip()
pg.quit()