"""
    Workload API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_list_meta import ApiListMeta
from pensando_cloud.psm.model.workload_workload import WorkloadWorkload
globals()['ApiListMeta'] = ApiListMeta
globals()['WorkloadWorkload'] = WorkloadWorkload
from pensando_cloud.psm.psm.model.workload_workload_list import WorkloadWorkloadList


class TestWorkloadWorkloadList(unittest.TestCase):
    """WorkloadWorkloadList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWorkloadWorkloadList(self):
        """Test WorkloadWorkloadList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WorkloadWorkloadList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
