"""
    Search API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.search_entry import SearchEntry
from pensando_dss.psm.model.search_error import SearchError
from pensando_dss.psm.model.search_tenant_aggregation import SearchTenantAggregation
from pensando_dss.psm.model.search_tenant_preview import SearchTenantPreview
globals()['SearchEntry'] = SearchEntry
globals()['SearchError'] = SearchError
globals()['SearchTenantAggregation'] = SearchTenantAggregation
globals()['SearchTenantPreview'] = SearchTenantPreview
from pensando_dss.psm.psm.model.search_search_response import SearchSearchResponse


class TestSearchSearchResponse(unittest.TestCase):
    """SearchSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchSearchResponse(self):
        """Test SearchSearchResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchSearchResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
