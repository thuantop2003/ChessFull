
import chesspieces as cp
board=cp.makeBoard();
def areBoardsEqual(board1, board2):
    return all(chess1.name == chess2.name and chess1.location == chess2.location
               for chess1, chess2 in zip(board1, board2))
print(len(cp.makeChildrenB(board)))
    