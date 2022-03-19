import argparse
import logging
import os
from dotenv import load_dotenv
from cloudctl_config import init_config

from cloudctl_server import handle_server_cmd


def router(args):
    cmd = args.subcommand
    if cmd == 'server':
        handle_server_cmd(args)
    else:
        print('unknown subcommand: %s' % cmd)


def parse_args():
    parser = argparse.ArgumentParser(description='Cloud Controller')

    subparsers = parser.add_subparsers(
        title="subcommands", dest='subcommand', description="valid subcommands", help="additional help")
    subparsers.required = True
    cmd_server = subparsers.add_parser('server', help='server control')

    cmd_server.add_argument('--action', help='action')
    cmd_server.add_argument(
        '--server-ids', help='server ids', type=str, nargs='+', default=[])

    args = parser.parse_args()
    return args


def main():
    load_dotenv()
    init_config()
    log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()
    logging.basicConfig(level=log_level, format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d (%(funcName)s)] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S')
    args = parse_args()
    logging.debug('args: %s', args)

    router(args)


if __name__ == '__main__':
    main()
