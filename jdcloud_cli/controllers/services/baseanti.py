# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from argparse import RawTextHelpFormatter
from jdcloud_cli.cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class BaseantiController(BaseController):
    class Meta:
        label = 'baseanti'
        help = '京东云DDoS基础防护相关接口'
        description = '''
        baseanti cli 子命令，京东云DDoS基础防护相关接口。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/anti-ddos-basic/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) IP模糊匹配 """, dest='ip',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询区域下的公网Ip资源列表 ''',
        description='''
            查询区域下的公网Ip资源列表。

            示例: jdc baseanti describe-ip-resources 
        ''',
    )
    def describe_ip_resources(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeIpResourcesRequest import DescribeIpResourcesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpResourcesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) 公网ip """, dest='ip',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询公网Ip基本信息 ''',
        description='''
            查询公网Ip基本信息。

            示例: jdc baseanti describe-ip-resource-info  --ip xxx
        ''',
    )
    def describe_ip_resource_info(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeIpResourceInfoRequest import DescribeIpResourceInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpResourceInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) 公网ip """, dest='ip',  required=True)),
            (['--clean-threshold-spec'], dict(help="""(cleanThresholdSpec) cc参数 """, dest='cleanThresholdSpec',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 设置公网Ip的清洗阈值 ''',
        description='''
            设置公网Ip的清洗阈值。

            示例: jdc baseanti set-clean-threshold  --ip xxx --clean-threshold-spec '{"":""}'
        ''',
    )
    def set_clean_threshold(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.SetCleanThresholdRequest import SetCleanThresholdRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = SetCleanThresholdRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) 公网ip """, dest='ip',  required=True)),
            (['--start'], dict(help="""(int) 限制查询的开始范围 """, dest='start', type=int, required=False)),
            (['--limit'], dict(help="""(int) 限制查询的记录数 """, dest='limit', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询公网Ip的防护明细 ''',
        description='''
            查询公网Ip的防护明细。

            示例: jdc baseanti describe-ip-resource-protect-info  --ip xxx
        ''',
    )
    def describe_ip_resource_protect_info(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeIpResourceProtectInfoRequest import DescribeIpResourceProtectInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpResourceProtectInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) 公网ip """, dest='ip',  required=True)),
            (['--end-time'], dict(help="""(string) 查询的结束时间，UTC时间，格式：yyyy-MM-dd'T'HH:mm:ssZ """, dest='endTime',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询公网Ip的监控流量 ''',
        description='''
            查询公网Ip的监控流量。

            示例: jdc baseanti describe-ip-resource-flow  --ip xxx
        ''',
    )
    def describe_ip_resource_flow(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeIpResourceFlowRequest import DescribeIpResourceFlowRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpResourceFlowRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-ip-resources','describe-ip-resource-info','set-clean-threshold','describe-ip-resource-protect-info','describe-ip-resource-flow',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('baseanti', self.app.pargs.api)
        skeleton.show()
