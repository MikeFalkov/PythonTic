class Node(object) :
    def __init__(self, move, parentNode):
        self.parentNode = parentNode
        if not move is None:
            self.move = move+1
            self.isX = not parentNode.isX
            self.board = parentNode.board.copy()
            self.board[move] = self.isX
            self.state = state(self.board, self.isX)
             
        else:
            self.isX = False
            self.board = [None for i in range(9)]
            self.state = state(self.board, self.isX)
        
        self.childNodes = addChildren(self)
        
        if not self.childNodes is None:
            self.maxWins = getMaxWins(self)
        else:
            self.maxWins = self.state

def getMaxWins(node):
    maxWins = sum([k.maxWins for k in node.childNodes])
    return maxWins

def addChildren(parentNode):
    if parentNode.state == 0:
        return [Node(k, parentNode) for k, v in enumerate(parentNode.board) if v is None]
    else:
        return None

def availableMoves(board):
    return [k for k, v in enumerate(board) if v is None]

def findNode(nodes, move):
    return next(n for n in nodes if n.move == move)

def playerMove(node):
    move = int(input("Your Move: "))
    if move in availableMoves(node.board):
        return findNode(node.childNodes, move)

def computerMove(parentNode):
    bestMove = None
    for n in parentNode.childNodes:
        if n.state != 0:
            return n
    maxWins = max([n.maxWins for n in parentNode.childNodes])
    return next(n for n in parentNode.childNodes if n.maxWins == maxWins)

def printBoard(board):
        b = [" "]*9
        for x in range(0, 9) :
            if (board[x] == True) :
                b[x] = "X"
            if (board[x] == False) :
                b[x] = "O"
        print('     |     |     ')
        print('  ' + b[0] + '  |  ' + b[1] + '  |  ' + b[2])
        print('_____|_____|_____')
        print('     |     |     ')
        print('  ' + b[3] + '  |  ' + b[4] + '  |  ' + b[5])
        print('_____|_____|_____')
        print('     |     |     ')
        print('  ' + b[6] + '  |  ' + b[7] + '  |  ' + b[8])
        print('     |     |     ')

def state(b, isX):
    if ((b[0] == b[1] == b[2] == isX) or
        (b[3] == b[4] == b[5] == isX) or
        (b[6] == b[7] == b[8] == isX) or
        (b[0] == b[3] == b[6] == isX) or
        (b[1] == b[4] == b[7] == isX) or
        (b[2] == b[5] == b[8] == isX) or
        (b[0] == b[4] == b[8] == isX) or
        (b[2] == b[4] == b[6] == isX)):
        if (isX == True):
            return 1
        if (isX == False):
            return -1
    else:
        return 0

def XorO():
    while True:
        response = input('X or O, choose: ').lower()
        if response == 'x':
            return True
        if response == 'o':
            return False
        else:
            print('Invalid response.')

def playForPlayer(node):
    printBoard(node.board)
    node = computerMove(playerMove(node))
    printBoard(node.board)
    if node.state != 0:
        print(node.state)
        return
    playForPlayer(node)

def playForComputer(node):
    node = computerMove(node)
    if node.state != 0:
        print(node.state)
        return
    printBoard(node.board)
    node = playerMove(node)
    playForComputer(node)

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')



tree = Node(None, None)

#play(tree)

while True:
    if XorO():
        playForPlayer(tree)
    else:
        playForComputer(tree)
    if not playAgain():
        break

pass