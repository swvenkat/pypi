"""
    Network API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.model.network_ipam_policy_spec import NetworkIPAMPolicySpec
from pensando_ent.psm.model.network_ipam_policy_status import NetworkIPAMPolicyStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['NetworkIPAMPolicySpec'] = NetworkIPAMPolicySpec
globals()['NetworkIPAMPolicyStatus'] = NetworkIPAMPolicyStatus
from pensando_ent.psm.psm.model.network_ipam_policy import NetworkIPAMPolicy


class TestNetworkIPAMPolicy(unittest.TestCase):
    """NetworkIPAMPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNetworkIPAMPolicy(self):
        """Test NetworkIPAMPolicy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NetworkIPAMPolicy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
