"""
    Rollout API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm.model.rollout_rollout_spec import RolloutRolloutSpec
from pensando_dss.psm.model.rollout_rollout_status import RolloutRolloutStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['RolloutRolloutSpec'] = RolloutRolloutSpec
globals()['RolloutRolloutStatus'] = RolloutRolloutStatus
from pensando_dss.psm.psm.model.rollout_rollout import RolloutRollout


class TestRolloutRollout(unittest.TestCase):
    """RolloutRollout unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRolloutRollout(self):
        """Test RolloutRollout"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RolloutRollout()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
