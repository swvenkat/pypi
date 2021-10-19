"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.fields_selector import FieldsSelector
from pensando_dss.psm.model.monitoring_email_export import MonitoringEmailExport
from pensando_dss.psm.model.monitoring_snmp_export import MonitoringSNMPExport
from pensando_dss.psm.model.monitoring_syslog_export import MonitoringSyslogExport
globals()['FieldsSelector'] = FieldsSelector
globals()['MonitoringEmailExport'] = MonitoringEmailExport
globals()['MonitoringSNMPExport'] = MonitoringSNMPExport
globals()['MonitoringSyslogExport'] = MonitoringSyslogExport
from pensando_dss.psm.psm.model.monitoring_alert_destination_spec import MonitoringAlertDestinationSpec


class TestMonitoringAlertDestinationSpec(unittest.TestCase):
    """MonitoringAlertDestinationSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringAlertDestinationSpec(self):
        """Test MonitoringAlertDestinationSpec"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringAlertDestinationSpec()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
