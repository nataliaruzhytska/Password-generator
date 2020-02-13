import random
import string

from flask import jsonify


def random_chars(n=12, uppercase=False, symbol=False, digit=False):
    if not digit and not symbol and not uppercase:
        password = ''.join(random.choice(string.ascii_lowercase) for x in range(int(n)))
        return jsonify({'password': password, 'message': 'Your password is too simple'})
    elif not digit and not symbol:
        password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for x in range(int(n)))
        return jsonify({'password': password, 'message': 'Your password is simple'})
    elif uppercase and digit and not symbol:
        password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                           for x in range(int(n)))
        return jsonify({'password': password, 'message': 'Your password is normal'})
    elif uppercase and symbol and not digit:
        password = ''.join(random.choice('!@#$%^&*' + string.ascii_uppercase + string.ascii_lowercase)
                           for x in range(int(n)))
        return jsonify({'password': password, 'message': 'Your password is normal'})
    elif digit and not uppercase and not symbol:
        password = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(int(n)))
        return jsonify({'password': password, 'message': 'Your password is simple'})
    elif symbol and not digit and not uppercase:
        password = ''.join(random.choice('!@#$%^&*' + string.ascii_lowercase) for x in range(int(n)))
        return jsonify({'password': password, 'message': 'Your password is simple'})
    elif digit and symbol and not uppercase:
        password = ''.join(random.choice('!@#$%^&*' + string.ascii_lowercase + string.digits) for x in range(int(n)))
        return jsonify({'password': password, 'message': 'Your password is normal'})
    else:
        password = ''.join(random.choice('!@#$%^&*' + string.ascii_uppercase + string.ascii_lowercase + string.digits)
                           for x in range(int(n)))
        return jsonify({'password': password, 'message': 'Your password is OK!'})
