from django.http import JsonResponse
import json
import jwt
import random
from threading import Thread
from time import sleep
import threading

SECRET = "jjfkecmwKJMd_effje2rfk394rf_KFMdsckW34x_ckr"
GAME_DB = {}

lock = threading.Lock()

def validate_and_get_email_from_jwt(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    encoded_jwt = body['jwt']
    decode_jwt = jwt.decode(encoded_jwt, SECRET, algorithms=['HS256'])
    return decode_jwt['email']

def start_new_game(request):
    if request.method != "POST":
            return JsonResponse({})
    email = validate_and_get_email_from_jwt(request)
    if not email:
        return JsonResponse({'err':'NO EMAIL FOUND'})
    # @TODO no email found
    cpuPlay = random.choice(['x','o'])
    playerPlay = 'x' 
    if cpuPlay == 'x':
        playerPlay = 'o'
    with lock:
        GAME_DB[email] = {
            'board': [
                ['','',''],
                ['','',''],
                ['','',''],
            ],
            'turn': random.choice(['x','o']),
            'cpu_play': cpuPlay,
            'player_play': playerPlay,
            'winner': '',
            'is_over': False
        }
    return JsonResponse({'gameStart':True}, safe=False)

def is_have_active_game(request):
    if request.method != "POST":
            return JsonResponse({})
    email = validate_and_get_email_from_jwt(request)
    if not email:
        return JsonResponse({'err':'NO EMAIL FOUND'})
    if email not in GAME_DB:
        return JsonResponse({'having_game':False}) 
    gameBoard = GAME_DB[email]        
    return JsonResponse({'having_game':not gameBoard['is_over']})

def get_game_state(request):
    if request.method != "POST":
        return JsonResponse({})
    email = validate_and_get_email_from_jwt(request)
    if not email:
        return JsonResponse({'err':'NO EMAIL FOUND'})
    # @TODO no email found
    return JsonResponse(GAME_DB[email], safe=False)

def checkWinnerCord(board, p0, p1, p2):
    if board[p0[0]][p0[1]] == "": return ""
    if board[p0[0]][p0[1]] != board[p1[0]][p1[1]]: return ""
    if board[p0[0]][p0[1]] != board[p2[0]][p2[1]]: return ""
    return board[p0[0]][p0[1]]

def checkWinner(board):
    winner = checkWinnerCord(board, (0,0),(0,1),(0,2))
    if winner: return winner
    winner = checkWinnerCord(board, (1,0),(1,1),(1,2))
    if winner: return winner
    winner = checkWinnerCord(board, (2,0),(2,1),(2,2))
    if winner: return winner
    winner = checkWinnerCord(board, (0,0),(1,0),(2,0))
    if winner: return winner
    winner = checkWinnerCord(board, (0,1),(1,1),(2,1))
    if winner: return winner
    winner = checkWinnerCord(board, (0,2),(1,2),(2,2))
    if winner: return winner
    winner = checkWinnerCord(board, (0,0),(1,1),(2,2))
    if winner: return winner
    winner = checkWinnerCord(board, (0,2),(1,1),(2,0))
    if winner: return winner
    return ""

def isAllBoardFull(board):
    i = 0
    while i<=2:
        j = 0
        while j<=2:
            if board[i][j] == "": return False
            j+=1
        i+=1
    return True
    
def player_move(request):
    if request.method != "POST":
        return JsonResponse({})
    email = validate_and_get_email_from_jwt(request)
    if not email:
        return JsonResponse({'err':'NO EMAIL FOUND'})
    # @TODO no email found
    # validate that it's player turn & player choose empty cell
    gameBoard = GAME_DB[email]
    if gameBoard['turn'] != gameBoard['player_play']:
        return JsonResponse({'msg':"NOT PLAYER TURN"})
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    row = body['row']
    col = body['col']
    if gameBoard['board'][row][col] != "":
        return JsonResponse({'msg':"NOT EMPTY CELL"})
    # place player move on board
    gameBoard['board'][row][col] = gameBoard['player_play']
    # check if someone alredy win
    gameBoard['winner'] = checkWinner(gameBoard['board'])
    
    if gameBoard['winner'] or isAllBoardFull(gameBoard['board']):
        gameBoard['is_over'] = True
    else: 
        # change turn to cpu
        gameBoard['turn'] = gameBoard['cpu_play']
    return JsonResponse({'msg':""})

def cpu_player_worker():
    while True:
        with lock:
            for key, gameBoard in GAME_DB.items():
                if gameBoard['turn'] != gameBoard['cpu_play']:
                    continue
                # random find an empty cell to p
                while True:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
                    if gameBoard['board'][row][col] == "":
                        gameBoard['board'][row][col] = gameBoard['cpu_play']
                        break
                # check if someone alredy win
                gameBoard['winner'] = checkWinner(gameBoard['board'])
                if gameBoard['winner'] or isAllBoardFull(gameBoard['board']):
                    gameBoard['is_over'] = True
                else: 
                    # change turn to player
                    gameBoard['turn'] = gameBoard['player_play']
        sleep(random.uniform(1,2))


thread = Thread(target = cpu_player_worker)
thread.start()
