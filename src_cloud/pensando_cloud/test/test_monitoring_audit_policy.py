"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm.model.monitoring_audit_policy_spec import MonitoringAuditPolicySpec
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['MonitoringAuditPolicySpec'] = MonitoringAuditPolicySpec
from pensando_cloud.psm.psm.model.monitoring_audit_policy import MonitoringAuditPolicy


class TestMonitoringAuditPolicy(unittest.TestCase):
    """MonitoringAuditPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringAuditPolicy(self):
        """Test MonitoringAuditPolicy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringAuditPolicy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
