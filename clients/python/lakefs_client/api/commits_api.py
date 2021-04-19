"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from lakefs_client.api_client import ApiClient, Endpoint as _Endpoint
from lakefs_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from lakefs_client.model.commit import Commit
from lakefs_client.model.commit_creation import CommitCreation
from lakefs_client.model.commit_list import CommitList
from lakefs_client.model.error import Error


class CommitsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __commit(
            self,
            repository,
            branch,
            commit_creation,
            **kwargs
        ):
            """create commit  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.commit(repository, branch, commit_creation, async_req=True)
            >>> result = thread.get()

            Args:
                repository (str):
                branch (str):
                commit_creation (CommitCreation):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Commit
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['repository'] = \
                repository
            kwargs['branch'] = \
                branch
            kwargs['commit_creation'] = \
                commit_creation
            return self.call_with_http_info(**kwargs)

        self.commit = _Endpoint(
            settings={
                'response_type': (Commit,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token'
                ],
                'endpoint_path': '/repositories/{repository}/branches/{branch}/commits',
                'operation_id': 'commit',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'branch',
                    'commit_creation',
                ],
                'required': [
                    'repository',
                    'branch',
                    'commit_creation',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'branch':
                        (str,),
                    'commit_creation':
                        (CommitCreation,),
                },
                'attribute_map': {
                    'repository': 'repository',
                    'branch': 'branch',
                },
                'location_map': {
                    'repository': 'path',
                    'branch': 'path',
                    'commit_creation': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__commit
        )

        def __get_commit(
            self,
            repository,
            commit_id,
            **kwargs
        ):
            """get commit  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_commit(repository, commit_id, async_req=True)
            >>> result = thread.get()

            Args:
                repository (str):
                commit_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Commit
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['repository'] = \
                repository
            kwargs['commit_id'] = \
                commit_id
            return self.call_with_http_info(**kwargs)

        self.get_commit = _Endpoint(
            settings={
                'response_type': (Commit,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token'
                ],
                'endpoint_path': '/repositories/{repository}/commits/{commitId}',
                'operation_id': 'get_commit',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'commit_id',
                ],
                'required': [
                    'repository',
                    'commit_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'commit_id':
                        (str,),
                },
                'attribute_map': {
                    'repository': 'repository',
                    'commit_id': 'commitId',
                },
                'location_map': {
                    'repository': 'path',
                    'commit_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_commit
        )

        def __log_branch_commits(
            self,
            repository,
            branch,
            **kwargs
        ):
            """get commit log from branch. Deprecated: replaced by logCommits by passing branch name as ref   # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.log_branch_commits(repository, branch, async_req=True)
            >>> result = thread.get()

            Args:
                repository (str):
                branch (str):

            Keyword Args:
                after (str): return items after this value. [optional]
                amount (int): how many items to return. [optional] if omitted the server will use the default value of 100
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CommitList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['repository'] = \
                repository
            kwargs['branch'] = \
                branch
            return self.call_with_http_info(**kwargs)

        self.log_branch_commits = _Endpoint(
            settings={
                'response_type': (CommitList,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token'
                ],
                'endpoint_path': '/repositories/{repository}/branches/{branch}/commits',
                'operation_id': 'log_branch_commits',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'branch',
                    'after',
                    'amount',
                ],
                'required': [
                    'repository',
                    'branch',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'amount',
                ]
            },
            root_map={
                'validations': {
                    ('amount',): {

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': -1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'branch':
                        (str,),
                    'after':
                        (str,),
                    'amount':
                        (int,),
                },
                'attribute_map': {
                    'repository': 'repository',
                    'branch': 'branch',
                    'after': 'after',
                    'amount': 'amount',
                },
                'location_map': {
                    'repository': 'path',
                    'branch': 'path',
                    'after': 'query',
                    'amount': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__log_branch_commits
        )
