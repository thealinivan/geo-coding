import re

def is_valid_ip(ip_address):
    pattern = re.compile(
        r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    )
    return re.match(pattern, ip_address) is not None