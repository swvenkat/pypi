"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.monitoring_auth_config import MonitoringAuthConfig
from pensando_cloud.psm.model.monitoring_privacy_config import MonitoringPrivacyConfig
globals()['MonitoringAuthConfig'] = MonitoringAuthConfig
globals()['MonitoringPrivacyConfig'] = MonitoringPrivacyConfig
from pensando_cloud.psm.psm.model.monitoring_snmp_trap_server import MonitoringSNMPTrapServer


class TestMonitoringSNMPTrapServer(unittest.TestCase):
    """MonitoringSNMPTrapServer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringSNMPTrapServer(self):
        """Test MonitoringSNMPTrapServer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringSNMPTrapServer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()