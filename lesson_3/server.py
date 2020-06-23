from socket import *
import json
import argparse


def create_parcer():
    """
    Create named arguments for run server.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', default='')
    parser.add_argument('-p', '--port', default=7777)
    return parser


def create_answer(code):
    """
    Receive anwer code, then forms dict for answer
    retract json object for this code
    """
    if round((code/100), 0) == 2:
        if code == 200:
            answer_message = 'OK'
        elif code == 201:
            answer_message = 'Created'
        elif code == 202:
            answer_message = 'Accepted'
        else:
            answer_message = 'Answer'
    elif round((code/100), 0) == 4:
        if code == 400:
            answer_message = 'Wrong JSON-object/ wrong request'
        elif code == 401:
            answer_message = 'Not authorization'
        elif code == 402:
            answer_message = 'Not authorization'
        elif code == 403:
            answer_message = 'forbidden'
        elif code == 404:
            answer_message = 'Not found'
        elif code == 409:
            answer_message = 'conflict'
        elif code == 410:
            answer_message = 'User offline'
        else:
            answer_message = 'idc'
    elif round((code/100), 0) == 1:
        if code == 100:
            answer_message = 'Base notification'
        elif code == 101:
            answer_message = 'Important notification'
        else:
            answer_message = 'Notification'
    elif round((code/100), 0) == 5:
        if code == 500:
            answer_message = 'Server ERROR'
        else:
            answer_message = 'Server ERROR'
    else:
        print('Wrong code')

    _answer = {
        "response": code,
        "alert": answer_message,
    }
    _json_answer = json.dumps(_answer)
    return _json_answer


def defenition_answer(message):
    """
    Taked dict from read_message,
    then read action feild and retract code
    """
    if message['action'] == 'presence':
        return create_answer(200)


def read_message(message):
    """
    Read gotten mesage, converted from json
    then call defenition_answer function
    or taked code 400.
    """
    try:
        received_message = json.loads(message)
        return defenition_answer(received_message)
    except:
        create_answer(400)


if __name__ == '__main__':
    parser = create_parcer()
    namespace = parser.parse_args()
    sock = socket(type=SOCK_STREAM)
    sock.bind((namespace.addr, int(namespace.port)))
    sock.listen(5)
    try:
        while True:
            conn, addr = sock.accept()
            data = conn.recv(1024)
            if not data:
                answer = create_answer(400)
            else:
                answer = read_message(data)
                print(answer)
            conn.send(answer.encode('utf-8'))
    finally:
        conn.close()
