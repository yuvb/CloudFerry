# Copyright (c) 2014 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and#
# limitations under the License.

from cloudferrylib.base.action import transporter
from cloudferrylib.os.actions import utils
from cloudferrylib.utils import utils as utl


class TransportCephToCephViaSsh(transporter.Transporter):

    def __init__(self, init,
                 resource_info='storage_info',
                 resource_name=utl.VOLUMES_TYPE,
                 resource_root_name=utl.VOLUME_BODY):
        super(TransportCephToCephViaSsh, self).__init__(init)
        self.resource_info = resource_info
        self.resource_name = resource_name
        self.resource_root_name = resource_root_name

    def run(self, **kwargs):
        info = kwargs[self.resource_info]
        data_for_trans = info[self.resource_name]
        for item in data_for_trans.itervalues():
            i = item[self.resource_root_name]
            src_host = i['src_host']
            dst_host = i['dst_host']
            src_path = i['src_path']
            dst_path = i['dst_path']
            utils.transfer_from_ceph_to_ceph(self.src_cloud,
                                             self.dst_cloud,
                                             src_host,
                                             dst_host,
                                             src_path,
                                             dst_path)
        return {}