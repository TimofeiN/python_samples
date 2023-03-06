"""
Function parses web server log file using regular expression.
Returns information:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)
"""
import re
import urllib.request


def log_parsing(url):
    RE_DATA = re.compile(r'^([\d.]+)[\s-]+([\S\w\s]+[]])\W+(\w+)\s(\S+)\s\S+\s(\d+)\s(\d+)')

    with urllib.request.urlopen(url) as response:
        for line in response:
            line = str(line).strip("b'")[:-3]
            parsed_line = RE_DATA.findall(line)
            return parsed_line[0]


# check
test_url = 'https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt'
for i in range(10):
    print(log_parsing(test_url))
