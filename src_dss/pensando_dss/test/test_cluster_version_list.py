"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.api_list_meta import ApiListMeta
from pensando_dss.psm.model.cluster_version import ClusterVersion
globals()['ApiListMeta'] = ApiListMeta
globals()['ClusterVersion'] = ClusterVersion
from pensando_dss.psm.psm.model.cluster_version_list import ClusterVersionList


class TestClusterVersionList(unittest.TestCase):
    """ClusterVersionList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterVersionList(self):
        """Test ClusterVersionList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterVersionList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
