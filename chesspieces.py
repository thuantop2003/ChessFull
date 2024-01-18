import copy
class Chess:
    def __init__(self,name,location):
        self.name=name
        self.location=location
def makeBoard():
    board=[]
    for i in range(1,9):
        a= Chess("Wpawn",[2,i])
        b= Chess("Bpawn",[7,i])
        board.append(a)
        board.append(b)
    board.append(Chess("Wbishop",[1,3]))
    board.append(Chess("Wbishop",[1,6]))
    board.append(Chess("Wknight",[1,2]))
    board.append(Chess("Wknight",[1,7]))
    board.append(Chess("Wrook",[1,1]))
    board.append(Chess("Wrook",[1,8]))
    board.append(Chess("WKing",[1,5]))
    board.append(Chess("WQueen",[1,4]))
    board.append(Chess("Bbishop",[8,3]))
    board.append(Chess("Bbishop",[8,6]))
    board.append(Chess("Bknight",[8,2]))
    board.append(Chess("Bknight",[8,7]))
    board.append(Chess("Brook",[8,1]))
    board.append(Chess("Brook",[8,8]))
    board.append(Chess("BKing",[8,5]))
    board.append(Chess("BQueen",[8,4]))
    return board
def loadimage(chess,pg,screen):
    chessimage=pg.image.load(r"image/"+chess.name+".png")
    if(chess.name=="Bpawn"or chess.name=="Wpawn"):
        chessimage=pg.transform.scale(chessimage,(65,65))
        screen.blit(chessimage,((chess.location[0]-1)*100+20,(chess.location[1]-1)*100+20))
    else:
        chessimage=pg.transform.scale(chessimage,(80,80))
        screen.blit(chessimage,((chess.location[0]-1)*100+10,(chess.location[1]-1)*100+10))
def WpawnValid(chess,board):
    validmove=[]
    k1=0
    check1=[chess.location[0]+1,chess.location[1]]
    for chessb in board:
        if(check1==chessb.location):
            k1=1
            break
    if check1[0]<1 or check1[1]>8 or check1[0]>8 or check1[1]<1:
            k1=1
    if(k1==0):
        validmove.append(check1)
    check2=[chess.location[0]+2,chess.location[1]]
    k2=1
    if(chess.location[0]==2):
        k2=0
        for chessb in board:
            if(check2==chessb.location):
                k2=1
                break
    if check2[0]<1 or check2[1]>8 or check2[0]>8 or check2[1]<1:
            k2=1
    if(k2==0):
        validmove.append(check2)

    check3=[chess.location[0]+1,chess.location[1]+1]
    check4=[chess.location[0]+1,chess.location[1]-1]
    for chessb in board:
        if check3==chessb.location and chessb.name[0]=="B":
            validmove.append(check3)
            break
        if check4==chessb.location and chessb.name[0]=="B":
            validmove.append(check4)
            break  
    return validmove      
def BpawnValid(chess,board):
    validmove=[]
    k1=0
    check1=[chess.location[0]-1,chess.location[1]]
    for chessb in board:
        if(check1==chessb.location):
            k1=1
            break
    if check1[0]<1 or check1[1]>8 or check1[0]>8 or check1[1]<1:
            k1=1
    if(k1==0):
        validmove.append(check1)
    check2=[chess.location[0]-2,chess.location[1]]
    k2=1
    if(chess.location[0]==7):
        k2=0
        for chessb in board:
            if(check2==chessb.location):
                k2=1
                break
    if check2[0]<1 or check2[1]>8 or check2[0]>8 or check2[1]<1:
            k2=1
    if(k2==0):
        validmove.append(check2)
    check3=[chess.location[0]-1,chess.location[1]+1]
    check4=[chess.location[0]-1,chess.location[1]-1]
    for chessb in board:
        if check3==chessb.location and chessb.name[0]=="W":
            validmove.append(check3)
            break
        if check4==chessb.location and chessb.name[0]=="W":
            validmove.append(check4)
            break  
    return validmove  
def WrookValid(chess,board):
    validmove=[]
    k1=k2=k3=k4=0
    for i in range(1,8):
        check1=[chess.location[0]+i,chess.location[1]]
        check2=[chess.location[0]-i,chess.location[1]]
        check3=[chess.location[0],chess.location[1]+i]
        check4=[chess.location[0],chess.location[1]-i]
        for chessb in board:
            if k1==0 and chessb.location==check1 and chessb.name[0]=="B":
                validmove.append(check1)
                k1=1
            if chessb.location==check1 and chessb.name[0]=="W":
                k1=1
            if k2==0 and chessb.location==check2 and chessb.name[0]=="B":
                validmove.append(check2)
                k2=1
            if chessb.location==check2 and chess.name[0]=="W":
                k2=1
            if k3==0 and chessb.location==check3 and chessb.name[0]=="B":
                validmove.append(check3)
                k3=1
            if chessb.location==check3 and chessb.name[0]=="W":
                k3=1
            if k4==0 and chessb.location==check4 and chessb.name[0]=="B":
                validmove.append(check4)
                k4=1
            if chessb.location==check4 and chessb.name[0]=="W":
                k4=1
        if check1[0]<1 or check1[1]>8 or check1[0]>8 or check1[1]<1:
            k1=1
        if check2[0]<1 or check2[1]>8 or check2[0]>8 or check2[1]<1:
            k2=1
        if check3[0]<1 or check3[1]>8 or check3[0]>8 or check3[1]<1:
            k3=1
        if check4[0]<1 or check4[1]>8 or check4[0]>8 or check4[1]<1:
            k4=1
        if k1==0:
            validmove.append(check1)
        if k2==0:
            validmove.append(check2)
        if k3==0:
            validmove.append(check3)
        if k4==0:
            validmove.append(check4)
    return validmove
def BrookValid(chess,board):
    validmove=[]
    k1=k2=k3=k4=0
    for i in range(1,8):
        check1=[chess.location[0]+i,chess.location[1]]
        check2=[chess.location[0]-i,chess.location[1]]
        check3=[chess.location[0],chess.location[1]+i]
        check4=[chess.location[0],chess.location[1]-i]
        for chessb in board:
            if k1==0 and chessb.location==check1 and chessb.name[0]=="W":
                validmove.append(check1)
                k1=1
            if chessb.location==check1 and chessb.name[0]=="B":
                k1=1
            if k2==0 and chessb.location==check2 and chessb.name[0]=="W":
                validmove.append(check2)
                k2=1
            if chessb.location==check2 and chess.name[0]=="B":
                k2=1
            if k3==0 and chessb.location==check3 and chessb.name[0]=="W":
                validmove.append(check3)
                k3=1
            if chessb.location==check3 and chessb.name[0]=="B":
                k3=1
            if k4==0 and chessb.location==check4 and chessb.name[0]=="W":
                validmove.append(check4)
                k4=1
            if chessb.location==check4 and chessb.name[0]=="B":
                k4=1
        if check1[0]<1 or check1[1]>8 or check1[0]>8 or check1[1]<1:
            k1=1
        if check2[0]<1 or check2[1]>8 or check2[0]>8 or check2[1]<1:
            k2=1
        if check3[0]<1 or check3[1]>8 or check3[0]>8 or check3[1]<1:
            k3=1
        if check4[0]<1 or check4[1]>8 or check4[0]>8 or check4[1]<1:
            k4=1
        if k1==0:
            validmove.append(check1)
        if k2==0:
            validmove.append(check2)
        if k3==0:
            validmove.append(check3)
        if k4==0:
            validmove.append(check4)
    return validmove
def WbishopValid(chess,board):
    validmove=[]
    k1=k2=k3=k4=0
    for i in range(1,8):
        check1=[chess.location[0]+i,chess.location[1]+i]
        check2=[chess.location[0]+i,chess.location[1]-i]
        check3=[chess.location[0]-i,chess.location[1]+i]
        check4=[chess.location[0]-i,chess.location[1]-i]
        for chessb in board:
            if k1==0 and chessb.location==check1 and chessb.name[0]=="B":
                validmove.append(check1)
                k1=1
            if chessb.location==check1 and chessb.name[0]=="W":
                k1=1
            if k2==0 and chessb.location==check2 and chessb.name[0]=="B":
                validmove.append(check2)
                k2=1
            if chessb.location==check2 and chess.name[0]=="W":
                k2=1
            if k3==0 and chessb.location==check3 and chessb.name[0]=="B":
                validmove.append(check3)
                k3=1
            if chessb.location==check3 and chessb.name[0]=="W":
                k3=1
            if k4==0 and chessb.location==check4 and chessb.name[0]=="B":
                validmove.append(check4)
                k4=1
            if chessb.location==check4 and chessb.name[0]=="W":
                k4=1
        if check1[0]<1 or check1[1]>8 or check1[0]>8 or check1[1]<1:
            k1=1
        if check2[0]<1 or check2[1]>8 or check2[0]>8 or check2[1]<1:
            k2=1
        if check3[0]<1 or check3[1]>8 or check3[0]>8 or check3[1]<1:
            k3=1
        if check4[0]<1 or check4[1]>8 or check4[0]>8 or check4[1]<1:
            k4=1
        if k1==0:
            validmove.append(check1)
        if k2==0:
            validmove.append(check2)
        if k3==0:
            validmove.append(check3)
        if k4==0:
            validmove.append(check4)
    return validmove
def BbishopValid(chess,board):
    validmove=[]
    k1=k2=k3=k4=0
    for i in range(1,8):
        check1=[chess.location[0]+i,chess.location[1]+i]
        check2=[chess.location[0]+i,chess.location[1]-i]
        check3=[chess.location[0]-i,chess.location[1]+i]
        check4=[chess.location[0]-i,chess.location[1]-i]
        for chessb in board:
            if k1==0 and chessb.location==check1 and chessb.name[0]=="W":
                validmove.append(check1)
                k1=1
            if chessb.location==check1 and chessb.name[0]=="B":
                k1=1
            if k2==0 and chessb.location==check2 and chessb.name[0]=="W":
                validmove.append(check2)
                k2=1
            if chessb.location==check2 and chess.name[0]=="B":
                k2=1
            if k3==0 and chessb.location==check3 and chessb.name[0]=="W":
                validmove.append(check3)
                k3=1
            if chessb.location==check3 and chessb.name[0]=="B":
                k3=1
            if k4==0 and chessb.location==check4 and chessb.name[0]=="W":
                validmove.append(check4)
                k4=1
            if chessb.location==check4 and chessb.name[0]=="B":
                k4=1
        if check1[0]<1 or check1[1]>8 or check1[0]>8 or check1[1]<1:
            k1=1
        if check2[0]<1 or check2[1]>8 or check2[0]>8 or check2[1]<1:
            k2=1
        if check3[0]<1 or check3[1]>8 or check3[0]>8 or check3[1]<1:
            k3=1
        if check4[0]<1 or check4[1]>8 or check4[0]>8 or check4[1]<1:
            k4=1
        if k1==0:
            validmove.append(check1)
        if k2==0:
            validmove.append(check2)
        if k3==0:
            validmove.append(check3)
        if k4==0:
            validmove.append(check4)
    return validmove
def WKingValid(chess,board):
    validmove=[]
    validmovess=[]
    validmove.append([chess.location[0]+1,chess.location[1]])
    validmove.append([chess.location[0]+1,chess.location[1]+1])
    validmove.append([chess.location[0]+1,chess.location[1]-1])
    validmove.append([chess.location[0]-1,chess.location[1]])
    validmove.append([chess.location[0]-1,chess.location[1]+1])
    validmove.append([chess.location[0]-1,chess.location[1]-1])
    validmove.append([chess.location[0],chess.location[1]+1])
    validmove.append([chess.location[0],chess.location[1]-1])
    for move in validmove:
        if move[0]>0 and move[0]<9 and move[1]>0 and move[1]<9:
            validmovess.append(move)
        for chessb in board:
                if chessb.location == move and chessb.name[0]=="W":
                    validmovess.remove(move)
                    break
    return validmovess
def BKingValid(chess,board):
    validmove=[]
    validmovess=[]
    validmove.append([chess.location[0]+1,chess.location[1]])
    validmove.append([chess.location[0]+1,chess.location[1]+1])
    validmove.append([chess.location[0]+1,chess.location[1]-1])
    validmove.append([chess.location[0]-1,chess.location[1]])
    validmove.append([chess.location[0],chess.location[1]+1])
    validmove.append([chess.location[0],chess.location[1]-1])
    validmove.append([chess.location[0]-1,chess.location[1]+1])
    validmove.append([chess.location[0]-1,chess.location[1]-1])
    for move in validmove:
        if move[0]>0 and move[0]<9 and move[1]>0 and move[1]<9:
            validmovess.append(move)
        for chessb in board:
                if chessb.location == move and chessb.name[0]=="B":
                    validmovess.remove(move)
                    break
    return validmovess
def WknightValid(chess,board):
    validmove=[]
    validmovess=[]
    validmove.append([chess.location[0]+2,chess.location[1]+1])
    validmove.append([chess.location[0]+2,chess.location[1]-1])
    validmove.append([chess.location[0]-2,chess.location[1]+1])
    validmove.append([chess.location[0]-2,chess.location[1]-1])
    validmove.append([chess.location[0]+1,chess.location[1]+2])
    validmove.append([chess.location[0]-1,chess.location[1]+2])
    validmove.append([chess.location[0]+1,chess.location[1]-2])
    validmove.append([chess.location[0]-1,chess.location[1]-2])
    for move in validmove:
        if move[0]>0 and move[0]<9 and move[1]>0 and move[1]<9:
            validmovess.append(move)
        for chessb in board:
                if chessb.location == move and chessb.name[0]=="W":
                    validmovess.remove(move)
    return validmovess
def BknightValid(chess,board):
    validmove=[]
    validmovess=[]
    validmove.append([chess.location[0]+2,chess.location[1]+1])
    validmove.append([chess.location[0]+2,chess.location[1]-1])
    validmove.append([chess.location[0]-2,chess.location[1]+1])
    validmove.append([chess.location[0]-2,chess.location[1]-1])
    validmove.append([chess.location[0]+1,chess.location[1]+2])
    validmove.append([chess.location[0]-1,chess.location[1]+2])
    validmove.append([chess.location[0]+1,chess.location[1]-2])
    validmove.append([chess.location[0]-1,chess.location[1]-2])
    for move in validmove:
        if move[0]>0 and move[0]<9 and move[1]>0 and move[1]<9:
            validmovess.append(move)
        for chessb in board:
                if chessb.location == move and chessb.name[0]=="B":
                    validmovess.remove(move)
    return validmovess
def validmoves(chess,board):
    validmove=[]
    if(chess.name=="Wpawn"):
        validmove=WpawnValid(chess,board)
    if(chess.name=="Bpawn"):
        validmove=BpawnValid(chess,board)
    if(chess.name=="Wrook"):
        validmove=WrookValid(chess,board)
    if(chess.name=="Brook"):
        validmove=BrookValid(chess,board)
    if(chess.name=="Wbishop"):
        validmove=WbishopValid(chess,board)
    if(chess.name=="Bbishop"):
        validmove=BbishopValid(chess,board)
    if(chess.name=="WQueen"):
        validmove=WrookValid(chess,board)
        validmove.extend(WbishopValid(chess,board))
    if(chess.name=="BQueen"):
        validmove=BrookValid(chess,board)
        validmove.extend(BbishopValid(chess,board))
    if(chess.name=="BKing"):
        validmove=BKingValid(chess,board)
    if(chess.name=="WKing"):
        validmove=WKingValid(chess,board)
    if(chess.name=="Wknight"):
        validmove=WknightValid(chess,board)   
    if(chess.name=="Bknight"):
        validmove=BknightValid(chess,board)  
    return validmove
def heuBoard(board):
    h={}
    h["Wpawn"]=-1
    h["Wrook"]=-5
    h["Wbishop"]=-3
    h["Wknight"]=-3
    h["WQueen"]=-9
    h["WKing"]=-1000
    h["Bpawn"]=1
    h["Brook"]=5
    h["Bbishop"]=3
    h["Bknight"]=3
    h["BQueen"]=9
    h["BKing"]=1000
    sum=0
    for chess in board:
        sum=sum+h[chess.name]
    return sum
def makeChildrenB(board):
    children=[]
    for chess in board:
        if chess.name[0]=="B":
            for move in validmoves(chess,board):
                board1 = copy.deepcopy(board)
                for c in board1:
                    if move ==c.location:
                        board1.remove(c)
                        break
                for c in board1:
                    if chess.location==c.location:
                        c.location=move
                        break
                children.append(board1)
    return children
def makeChildrenW(board):
    children=[]
    for chess in board:
        if chess.name[0]=="W":
            for move in validmoves(chess,board):
                board1 = copy.deepcopy(board)
                for c in board1:
                    if move ==c.location:
                        board1.remove(c)
                        break
                for c in board1:
                    if chess.location==c.location:
                        c.location=move
                        break
                children.append(board1)
    return children
def pChildren(board,i,x,y):
    if i==4:
        return [board,heuBoard(board)]
    if i%2==1:
        maxx=-10000
        for b in makeChildrenB(board):
            if(heuBoard(b)>500):
                return [b,heuBoard(b)]
            if(heuBoard(b)<-500):
                return [b,heuBoard(b)]
            a=pChildren(b,i+1,x,y)[1]
            if a>maxx:
                maxx=a
                sb=b
            if maxx>=x:
                return [sb,maxx]
            if y<maxx:
                y=maxx
        return [sb,maxx]
    if i%2==0:
        minn=10000
        sb=board
        for b in makeChildrenW(board):
            if(heuBoard(b)<-500):
                sb=b
                return [sb,heuBoard(b)]
            if(heuBoard(b)>500):
                sb=b
                return [sb,heuBoard(b)]
            a=pChildren(b,i+1,x,y)[1]
            if a<minn:
                minn=a
                sb=b
            if minn<=y:
                return [sb,minn]
            if x>minn:
                x=minn
        return [sb,minn]
def makeMove(board):
    x=pChildren(board,1,1000,-1000)
    sboard=x[0]
    return sboard
def makeMoveW(board):
    x=pChildren(board,2,1000,-1000)
    sboard=x[0]
    return sboard

