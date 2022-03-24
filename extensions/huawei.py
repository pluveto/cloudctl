import logging
import os
from unicodedata import name
from huaweicloudsdkecs.v2 import EcsClient, ListServersDetailsRequest, ListServersDetailsResponse, BatchStartServersRequest, BatchStartServersResponse, BatchStopServersRequest, BatchStopServersResponse
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.exceptions import exceptions

from cloudctl_exception import BadRequestException


def get_ecs_client() -> EcsClient:
    ecs_client: EcsClient = None

    def _impl():
        nonlocal ecs_client
        if ecs_client is not None:
            return ecs_client
        endpoint = os.environ.get('HUAWEICLOUD_SDK_IAM_ENDPOINT')
        ecs_client = EcsClient.new_builder().with_endpoint(endpoint).build()
        return ecs_client

    return _impl()


def _filter_server_detail(server):
    logging.debug('server: %s', server)
    vpc_id = server.metadata.get('vpc_id')
    d = dict()
    d['id'] = server.id
    d['status'] = server.status
    d['name'] = server.name
    d['private_ip'] = server.addresses.get(vpc_id)[0].addr
    d['public_ip'] = server.addresses.get(vpc_id)[-1].addr
    return d


def get_server_status(server_ids):
    if len(server_ids) == 0:
        raise ValueError('server_ids is empty')

    ecs_client = get_ecs_client()
    servers_detail: ListServersDetailsResponse = ecs_client.list_servers_details(
        ListServersDetailsRequest(name=server_ids[0]))
    if len(servers_detail.servers) == 0:
        raise BadRequestException('server not found')
    return _filter_server_detail(servers_detail.servers[0])


def list_servers():
    ecs_client = get_ecs_client()
    servers_detail: ListServersDetailsResponse = ecs_client.list_servers_details(
        ListServersDetailsRequest())

    return list(map(_filter_server_detail, servers_detail.servers))


def start_servers(server_ids):
    ecs_client = get_ecs_client()
    body = {'os-start':{'servers': [{'id': server_id} for server_id in server_ids]}}
    logging.debug("body: {}".format(body))
    resp: BatchStartServersResponse = ecs_client.batch_start_servers(BatchStartServersRequest(
        body=body))
    logging.debug("resp: {}".format(resp))
    return None

def stop_servers(server_ids):
    ecs_client = get_ecs_client()
    body = {'os-stop':{'servers': [{'id': server_id} for server_id in server_ids]}}
    logging.debug("body: {}".format(body))
    resp: BatchStopServersResponse = ecs_client.batch_stop_servers(BatchStopServersRequest(
        body=body))
    logging.debug("resp: {}".format(resp))
    return None