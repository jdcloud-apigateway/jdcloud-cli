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


class AgController(BaseController):
    class Meta:
        label = 'ag'
        help = '高可用组'
        description = '''
        ag cli 子命令，高可用组相关接口。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/cloud-ag-service/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--filters'], dict(help="""(array: filter) resourceTypes - 资源类型，暂时只支持[ag];  """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询(ag)配额 ''',
        description='''
            查询(ag)配额。

            示例: jdc ag describe-quotas 
        ''',
    )
    def describe_quotas(self):
        client_factory = ClientFactory('ag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ag.apis.DescribeQuotasRequest import DescribeQuotasRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeQuotasRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 """, dest='regionId',  required=False)),
            (['--page-number'], dict(help="""(int) 页码；默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小；默认为20；取值范围[10, 100] """, dest='pageSize', type=int, required=False)),
            (['--filters'], dict(help="""(array: filter) agName - ag名字，支持模糊匹配; agId - ag id，精确匹配; instanceTemplateId - 实例模板id，精确匹配; vpcId - vpc id，精确匹配; placementType - placement type，放置策略;  """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 使用过滤条件查询一个或多个高可用组 ''',
        description='''
            使用过滤条件查询一个或多个高可用组。

            示例: jdc ag describe-ags 
        ''',
    )
    def describe_ags(self):
        client_factory = ClientFactory('ag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ag.apis.DescribeAgsRequest import DescribeAgsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAgsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 """, dest='regionId',  required=False)),
            (['--azs'], dict(help="""(array: string) 支持的可用区，最少一个 """, dest='azs',  required=False)),
            (['--ag-name'], dict(help="""(string) 高可用组名称，只支持中文、数字、大小写字母、英文下划线 “_” 及中划线 “-”，且不能超过 32 字符 """, dest='agName',  required=True)),
            (['--ag-type'], dict(help="""(string) 高可用组资源类型，支持vm """, dest='agType',  required=False)),
            (['--instance-template-id'], dict(help="""(string) 实例模板的ID """, dest='instanceTemplateId',  required=False)),
            (['--description'], dict(help="""(string) 描述，长度不超过 256 字符 """, dest='description',  required=False)),
            (['--configuration-type'], dict(help="""(string) 高可用组配置类型，支持strict(关联模板型)、loose(自定义配置型) """, dest='configurationType',  required=False)),
            (['--placement-type'], dict(help="""(string) 高可用资源放置类型，支持fd、switch、host """, dest='placementType',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建一个高可用组 ''',
        description='''
            创建一个高可用组。

            示例: jdc ag create-ag  --ag-name xxx
        ''',
    )
    def create_ag(self):
        client_factory = ClientFactory('ag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ag.apis.CreateAgRequest import CreateAgRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateAgRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 """, dest='regionId',  required=False)),
            (['--ag-id'], dict(help="""(string) 高可用组 ID """, dest='agId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 根据 ID 查询高可用组详情 ''',
        description='''
            根据 ID 查询高可用组详情。

            示例: jdc ag describe-ag  --ag-id xxx
        ''',
    )
    def describe_ag(self):
        client_factory = ClientFactory('ag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ag.apis.DescribeAgRequest import DescribeAgRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAgRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 """, dest='regionId',  required=False)),
            (['--ag-id'], dict(help="""(string) 高可用组 ID """, dest='agId',  required=True)),
            (['--description'], dict(help="""(string) 描述，长度不超过 256 字符 """, dest='description',  required=False)),
            (['--name'], dict(help="""(string) 高可用组名称，只支持中文、数字、大小写字母、英文下划线 “_” 及中划线 “-”，且不能超过 32 字符 """, dest='name',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改一个高可用组的信息 ''',
        description='''
            修改一个高可用组的信息。

            示例: jdc ag update-ag  --ag-id xxx
        ''',
    )
    def update_ag(self):
        client_factory = ClientFactory('ag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ag.apis.UpdateAgRequest import UpdateAgRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UpdateAgRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 """, dest='regionId',  required=False)),
            (['--ag-id'], dict(help="""(string) 高可用组 ID """, dest='agId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 根据 ID 删除高可用组，需确保 AG 中云主机实例已全部删除 ''',
        description='''
            根据 ID 删除高可用组，需确保 AG 中云主机实例已全部删除。

            示例: jdc ag delete-ag  --ag-id xxx
        ''',
    )
    def delete_ag(self):
        client_factory = ClientFactory('ag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ag.apis.DeleteAgRequest import DeleteAgRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteAgRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 """, dest='regionId',  required=False)),
            (['--ag-id'], dict(help="""(string) 高可用组 ID """, dest='agId',  required=True)),
            (['--instance-ids'], dict(help="""(array: string) 准备剔除出高可用组的实例 ID """, dest='instanceIds',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 从高可用组中剔除实例 ''',
        description='''
            从高可用组中剔除实例。

            示例: jdc ag abandon-instances  --ag-id xxx
        ''',
    )
    def abandon_instances(self):
        client_factory = ClientFactory('ag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ag.apis.AbandonInstancesRequest import AbandonInstancesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = AbandonInstancesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 """, dest='regionId',  required=False)),
            (['--ag-id'], dict(help="""(string) 高可用组 ID """, dest='agId',  required=True)),
            (['--instance-template-id'], dict(help="""(string) 实例模板 ID """, dest='instanceTemplateId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改高可用组的实例模板<br>- 对于更换实例模板来说，如果已经关联负载均衡，则VPC不可以更改。<br>- 自定义配置型不可更改实例模板。 ''',
        description='''
            修改高可用组的实例模板<br>- 对于更换实例模板来说，如果已经关联负载均衡，则VPC不可以更改。<br>- 自定义配置型不可更改实例模板。。

            示例: jdc ag set-instance-template  --ag-id xxx --instance-template-id xxx
        ''',
    )
    def set_instance_template(self):
        client_factory = ClientFactory('ag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ag.apis.SetInstanceTemplateRequest import SetInstanceTemplateRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = SetInstanceTemplateRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-quotas','describe-ags','create-ag','describe-ag','update-ag','delete-ag','abandon-instances','set-instance-template',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('ag', self.app.pargs.api)
        skeleton.show()