# IP address validator:  v1
def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


# IP address validator:  v2
import socket
try:
    socket.inet_aton(addr)
    # legal
except socket.error:
    # Not legal


# IP address validator:  v3
from IPy import IP
try:
    ip = IP('230.10.10.16')
except ValueError:
    # invalid IP
