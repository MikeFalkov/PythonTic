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
            self.score = getScore(self)
        else:
            self.maxWins = self.state
            self.score = self.state

def getMaxWins(node):
    return sum([k.maxWins for k in node.childNodes])
    #return maxWins

def getScore(node):
    try:
        score = max([s.state for s in node.childNodes])
    except:
        score = node.state
    return score

def addChildren(parentNode):
    if parentNode.state == 0:
        return [Node(k, parentNode) for k, v in enumerate(parentNode.board) if v is None]
    else:
        return None

def availableMoves(board):
    return [k+1 for k, v in enumerate(board) if v is None]

def findNode(nodes, move):
    return next(n for n in nodes if n.move == move)

def playerMove(node):
    while True:
        move = None
        try:
            move = int(input("Your Move: "))
        except:
            print("Invalid response. Must be an integer")
            continue

        if move in availableMoves(node.board):
            return findNode(node.childNodes, move)

        if move > 0 and move < 10:
            print(str(move) + " is not available.")
        else:
            print(str(move) + " is an invalid move.")

def computerMove(parentNode):
    bestMove = None
    try:
        for childNode in parentNode.childNodes:
            if childNode.state != 0:
                bestMove = childNode
    except:
        bestMove = parentNode.childNodes
    if bestMove != None:
        return bestMove

    if parentNode.isX == 1:
        maxWins = min([n.maxWins for n in parentNode.childNodes])
        scores = [s.score for s in parentNode.childNodes]
        if max(scores) == 1:
            return next(n for n in parentNode.childNodes if n.score == min(scores))
            #return bestMove
        else:
            return next(n for n in parentNode.childNodes if n.maxWins == maxWins)
            #return bestMove
    
    maxWins = max([n.maxWins for n in parentNode.childNodes])
    return next(n for n in parentNode.childNodes if n.maxWins == maxWins)
    #return bestMove

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
    #node = computerMove(playerMove(node))
    player = playerMove(node)
    if player.childNodes == []:
        printBoard(player.board)
        print("It's a Draw.")
        return
    computer = computerMove(player)
    printBoard(computer.board)
    if computer.state != 0:
        print("Computer wins!!!")
        return
    playForPlayer(computer)

def playForComputer(node):
    computer = computerMove(node)
    printBoard(computer.board)
    if computer.state != 0:
        print("Computer wins!!!")
        return
    if computer.childNodes == []:
        print("It's a Draw.")
        return
    player = playerMove(computer)
    playForComputer(player)

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


tree = Node(None, None)
while True:
    if XorO():
        printBoard(tree.board)
        playForPlayer(tree)
    else:
        playForComputer(tree)
    if not playAgain():
        break