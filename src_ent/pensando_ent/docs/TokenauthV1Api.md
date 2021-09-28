# psm.TokenauthV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_generate_node_token**](TokenauthV1Api.md#get_generate_node_token) | **GET** /tokenauth/v1/node | 


# **get_generate_node_token**
> TokenauthNodeTokenResponse get_generate_node_token()



### Example

```python
import time
import psm
from api import tokenauth_v1_api
from pensando_ent.psm.model.tokenauth_node_token_response import TokenauthNodeTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_ent.psm.Configuration(
    psm_config_path=HOME+"/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with psm.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tokenauth_v1_api.TokenauthV1Api(api_client)
    audience = [
        "audience_example",
    ] # [str] | Audience represents a list of nodes the token is valid for. \"*\" indicates all nodes. (optional)
    validity_start = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ValidityStart indicates the time at which the token becomes valid. (optional)
    validity_end = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ValidityEnd indicates the time at which the token becomes invalid. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_generate_node_token(audience=audience, validity_start=validity_start, validity_end=validity_end)
        pprint(api_response)
    except psm.ApiException as e:
        print("Exception when calling TokenauthV1Api->get_generate_node_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience** | **[str]**| Audience represents a list of nodes the token is valid for. \&quot;*\&quot; indicates all nodes. | [optional]
 **validity_start** | **datetime**| ValidityStart indicates the time at which the token becomes valid. | [optional]
 **validity_end** | **datetime**| ValidityEnd indicates the time at which the token becomes invalid. | [optional]

### Return type

[**TokenauthNodeTokenResponse**](TokenauthNodeTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
