"""
Function checks the log file.
Return a spammer's IP and requests count of spammer.
"""

import urllib.request

log_url = 'https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt'


def find_spammer(url):
    tmp = set()
    result = {}

    with urllib.request.urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')
            idx = line.find(' - ')
            ip = line[:idx]
            if ip not in tmp:
                ip_dict = {ip: 1}
                result.update(ip_dict)
            else:
                count = result.get(ip) + 1
                result[ip] = count
            tmp.add(ip)

    spammer = ''
    for k, v in result.items():
        if v == max(result.values()):
            spammer = f'{k} - {v}'
    return f'spammer, {spammer}'


# check
print(find_spammer(log_url))
