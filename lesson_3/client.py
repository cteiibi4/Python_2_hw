from socket import *
import json
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8080))
client = 'client'
status = 'OK'

def presence_message():
    message = {
        'action': 'presence',
        'time': time.ctime(),
        'type': 'status',
        'user': {
            'account_name': client,
            'status': status,
        }
    }
    return json.dumps(message)
# message = {
#     'action':'authenticate',
#     'time': time.ctime(),
#     'type': 'status',
#     'user':{
#         'account_name': 'client',
#         'status': 'OK',
#     }
# }
def read_message(message):
    try:
        received_message = json.loads(message)
        return defenition_answer(received_message)
    except:
        pass

def defenition_answer(message):
    if message['action'] == 'probe':
        message_for_server = presence_message()
        s.send(message_for_server.encode('utf-8'))

if __name__ == '__main__':
    message_for_server = presence_message()
    s.send(message_for_server.encode('utf-8'))
    response = s.recv(1024)
    read_message(response)
    print(f'Ответ: {response.decode("utf-8")}')