from email import message_from_file
import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []
nicknames = []

questions = [
    "What is the Italian word for PIE? \n a.Mozarella\n b.Pasty\n c.Patty\n d.Pizza",
    "How many bones does an adult human have? \n a.206\n b.208\n c.201\n d.196",
    "Which planet is closest to the sun? \n a.Mercury\n b.Pluto\n c.Earth\n d.Venus"]

answers = ['d','a','a']

print('Server has started...')
    
def get_random_answer(conn):
    random_index = random.randint(0,len(questions) - 1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)
def clientthread(conn,nickname):
    score= 0
    conn.send('Welcome to this quiz!'.encode('utf-8'))
    conn.send("You will receive a question. The answer to that question should be one of the options a, b, c or d\n".encode('utf-8'))    
    conn.send('Good Luck!\n\n'.encode('utf-8'))
    index, question, answer = get_random_answer(conn)
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message.split(": ")[-1].lower() == answer:
                    if message.lower() == answer:
                        score = score + 1
                        conn.send(f"Bravo! Your score is {score}\n\n".encode('utf-8'))
                    else:
                        conn.send('Incorrect answer! Better luck next time!\n\n'.encode('utf-8'))
                    remove_question(index)
                    index, question, answer = get_random_answer(conn)
                    remove_nickname(nickname)
            else:
                remove(conn)
        except:
            continue
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def remove_nickname(nickname): 
    if nickname in nicknames: 
        nicknames.remove(nickname)


while True:
    conn, addr = server.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    list_of_clients.append(conn)
    nicknames.append(nickname)
    print(nickname+ 'Connected')
    new_thread = Thread(target=clientthread,args=(conn,nickname))
    new_thread.start()
