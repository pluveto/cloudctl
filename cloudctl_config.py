
import os
import yaml

cloudctl_config = None


def init_config():
    global cloudctl_config
    # load config.yaml
    config_file_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    cloudctl_config = yaml.load(open(config_file_path, encoding="utf-8",
                                     mode="r"), Loader=yaml.SafeLoader)


def get_server_config(server_id):
    servers = cloudctl_config['servers']
    return next(server for server in servers if server['id'] == server_id)
