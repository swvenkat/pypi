"""
    Workload API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm.model.workload_workload_spec import WorkloadWorkloadSpec
from pensando_cloud.psm.model.workload_workload_status import WorkloadWorkloadStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['WorkloadWorkloadSpec'] = WorkloadWorkloadSpec
globals()['WorkloadWorkloadStatus'] = WorkloadWorkloadStatus
from pensando_cloud.psm.psm.model.workload_workload import WorkloadWorkload


class TestWorkloadWorkload(unittest.TestCase):
    """WorkloadWorkload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWorkloadWorkload(self):
        """Test WorkloadWorkload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WorkloadWorkload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()