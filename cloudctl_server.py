import importlib
import json
import logging
import traceback

from cloudctl_exception import BadRequestException


def handle_server_cmd(args):

    driver_name = "huawei"
    mod = importlib.import_module('extensions.' + driver_name)

    def handle_get_status(server_ids):
        logging.debug('handle_get_status: %s', server_ids)

        return mod.get_server_status(server_ids)

    def handle_list():
        return mod.list_servers()

    def handle_start(server_ids):
        logging.debug('handle_start: %s', server_ids)
        mod.start_servers(server_ids)

    def handle_stop(server_ids):
        logging.debug('handle_stop: %s', server_ids)
        mod.stop_servers(server_ids)
    
    try:
        action = args.action
        server_ids = args.server_ids
        ret = None
        if action == 'status':
            ret = handle_get_status(server_ids)
        elif action == 'list':
            ret = handle_list()
        elif action == 'start':
            ret = handle_start(server_ids)
        elif action == 'stop':
            ret = handle_stop(server_ids)
        else:
            print('unknown action: %s' % action)
            return

        print(json.dumps(ret, indent=2))

    except BadRequestException as e:
        wrap = {'error': str(e)}
        if logging.getLogger().isEnabledFor(logging.DEBUG):
            wrap['traceback'] = traceback.format_tb(e.__traceback__)

        print(json.dumps(wrap, indent=2))

    except Exception as e:
        print(json.dumps(
            {'error': str(e), 'stack': traceback.format_exc()}, indent=2))
