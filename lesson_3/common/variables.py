# Dictionary for code and ansvers from server
DICT_ANSWER_CODE = {
    100: 'Base notification',
    101: 'Important notification',
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    400: 'Wrong JSON-object/ wrong request',
    401: 'Not authorization',
    402: 'Not authorization',
    403: 'forbidden',
    404: 'Not found',
    409: 'conflict',
    410: 'User offline',
    500: 'Server ERROR',
}
# Default port for connection
DEFAULT_PORT = 7777
# Default IP address for connection
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Maximal queue connections
MAX_CONNECTIONS = 5
# Max length message in bytes
MAX_PACKAGE_LENGTH = 1024
# Project encoding
ENCODING = 'utf-8'