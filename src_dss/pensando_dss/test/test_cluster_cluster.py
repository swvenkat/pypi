"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm.model.cluster_cluster_spec import ClusterClusterSpec
from pensando_dss.psm.model.cluster_cluster_status import ClusterClusterStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['ClusterClusterSpec'] = ClusterClusterSpec
globals()['ClusterClusterStatus'] = ClusterClusterStatus
from pensando_dss.psm.psm.model.cluster_cluster import ClusterCluster


class TestClusterCluster(unittest.TestCase):
    """ClusterCluster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterCluster(self):
        """Test ClusterCluster"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterCluster()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
