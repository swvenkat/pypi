"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.model.monitoring_alert_destination_spec import MonitoringAlertDestinationSpec
from pensando_ent.psm.model.monitoring_alert_destination_status import MonitoringAlertDestinationStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['MonitoringAlertDestinationSpec'] = MonitoringAlertDestinationSpec
globals()['MonitoringAlertDestinationStatus'] = MonitoringAlertDestinationStatus
from pensando_ent.psm.psm.model.monitoring_alert_destination import MonitoringAlertDestination


class TestMonitoringAlertDestination(unittest.TestCase):
    """MonitoringAlertDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringAlertDestination(self):
        """Test MonitoringAlertDestination"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringAlertDestination()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
