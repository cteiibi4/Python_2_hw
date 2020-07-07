from socket import *
import json
import argparse
import os
import logging
import logging.config
import logging.handlers
import yaml
from common.variables import ENCODING, MAX_PACKAGE_LENGTH, MAX_CONNECTIONS ,DEFAULT_PORT, DEFAULT_IP_ADDRESS, LOG_PATH_CONFIG_SERVER



with open(LOG_PATH_CONFIG_SERVER, 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logger = logging.getLogger('server')
logger.info('Start logging')


def create_parcer():
    """
    Create named arguments for run server.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', default=DEFAULT_IP_ADDRESS)
    parser.add_argument('-p', '--port', default=DEFAULT_PORT)
    logger.info(f'take args on start server: ip address {parser.parse_args().addr}, port {parser.parse_args().port}')
    return parser


def create_answer(code):
    """
    Receive anwer code, then forms dict for answer
    retract json object for this code
    """

    if round((code / 100), 0) == 2:
        if code == 200:
            answer_message = 'OK'
        elif code == 201:
            answer_message = 'Created'
        elif code == 202:
            answer_message = 'Accepted'
        else:
            answer_message = 'Answer'
    elif round((code / 100), 0) == 4:
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
    elif round((code / 100), 0) == 1:
        if code == 100:
            answer_message = 'Base notification'
        elif code == 101:
            answer_message = 'Important notification'
        else:
            answer_message = 'Notification'
    elif round((code / 100), 0) == 5:
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
    logger.info(f'return message for code {code}')
    return _json_answer


def defenition_answer(message):
    """
    Take dict from read_message,
    then read action feild and retract code
    """
    logger.info(f'take massage')
    if message['action'] == 'presence':
        return create_answer(200)


def read_message(message):
    """
    Read gotten mesage, converted from json
    then call defenition_answer function
    or taked code 400.
    """
    logger.info('read massage from client')
    try:
        received_message = json.loads(message)
        return defenition_answer(received_message)
    except:
        logger.error('Exception:', exc_info=True)
        create_answer(400)


if __name__ == '__main__':
    parser = create_parcer()
    namespace = parser.parse_args()
    sock = socket(type=SOCK_STREAM)
    sock.bind((namespace.addr, int(namespace.port)))
    sock.listen(MAX_CONNECTIONS)
    try:
        while True:
            conn, addr = sock.accept()
            data = conn.recv(MAX_PACKAGE_LENGTH )
            if not data:
                answer = create_answer(400)
            else:
                answer = read_message(data)
                print(answer)
            conn.send(answer.encode(ENCODING))
    finally:
        logger.info('server stop')
        conn.close()
