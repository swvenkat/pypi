"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm.model.cluster_version_status import ClusterVersionStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['ClusterVersionStatus'] = ClusterVersionStatus
from pensando_cloud.psm.psm.model.cluster_version import ClusterVersion


class TestClusterVersion(unittest.TestCase):
    """ClusterVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterVersion(self):
        """Test ClusterVersion"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterVersion()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
