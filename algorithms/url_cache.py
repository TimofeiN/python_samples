"""
Function takes url-address, checks address is in cache.
If not - write it in file.
Else returns hash value.
"""


def url_cache(url):
    import hashlib
    import json
    salt = 'my_salt'

    try:
        open('url_cache.json', 'r+')
    except FileNotFoundError:
        with open('url_cache.json', 'w+') as f:
            data = {}
            url_hash = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
            data[url] = url_hash
            json.dump(data, f)
    else:
        f = open('url_cache.json', 'r+')
        file_data = f.read()
        if file_data == '':
            data = {}
            url_hash = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
            data[url] = url_hash
            json.dump(data, f, indent=4)
            f.close()
        else:
            data = json.loads(file_data)
            if url in data:
                result = f'For {url} \nhash - {data[url]}'
                f.close()
                return result
            else:
                f.close()
                with open('url_cache.json', 'w+') as f:
                    url_hash = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
                    data[url] = url_hash
                    f.write(json.dumps(data, indent=4))


# check
urls = [
    'https://www.yahoo.com/',
    'https://www.mail.cat/',
    'https://www.google.com/',
    'https://www.amazon.com/'
]

for address in urls:
    print(url_cache(address))
