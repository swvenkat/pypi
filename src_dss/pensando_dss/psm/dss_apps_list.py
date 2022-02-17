import time
import os
import pensando_dss
import pensando_dss.psm
import argparse
import sys
import urllib3
from pensando_dss.psm.api import security_v1_api
from pensando_dss.psm.models.security import *
from pensando_dss.psm.model.security_app_list import SecurityAppList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dss_common import *
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_v1_api.SecurityV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_tenant = "O.tenant_example" # str | Tenant to which the object belongs to. This can be automatically filled in many cases based on the tenant the user, who created the object, belongs to. Must be alpha-numerics. Length of string should be between 1 and 48. (optional)
    o_namespace = "O.namespace_example" # str | Namespace of the object, for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_generation_id = "O.generation-id_example" # str | GenerationID is the generation Id for the object. This is incremented anytime there is an update to the user intent, including Spec update and any update to ObjectMeta. System generated and updated, not updatable by user. (optional)
    o_resource_version = "O.resource-version_example" # str | Resource version in the object store. This is updated anytime there is any change to the object. System generated and updated, not updatable by user. (optional)
    o_uuid = "O.uuid_example" # str | UUID is the unique identifier for the object. This is generated on creation of the object. System generated, not updatable by user. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    o_mod_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ModTime is the Last Modification time of the object. System generated and updated, not updatable by user. (optional)
    o_self_link = "O.self-link_example" # str | SelfLink is a link for accessing this object. When the object is served from the API-GW it is the URI path. Example: - \"/v1/tenants/tenants/tenant2\" System generated and updated, not updatable by user. (optional)
    label_selector = "label-selector_example" # str | LabelSelector to select on labels in list or watch results. (optional)
    field_selector = "field-selector_example" # str | FieldSelector to select on field values in list or watch results. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)
    _from = 1 # int | From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination. (optional)
    max_results = 1 # int | MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination. (optional)
    sort_order = "sort-order_example" # str | order to sort List results in. (optional)
    meta_only = True # bool | If MetaOnly is set to true, the watch event notification that matches the watch criteria will not contain the full object. It will only contain the information about the object that changed, i.e. which object and what changed. MetaOnly is not set by default. (optional)

    # example passing only required values which don't have defaults set
    try:
        description = "List all configured App objects"
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument("-v", "--verbose", help = "Verbose output for all configured Apps", action="store_true")
        parser.add_argument("-n", "---name", help = "Verbose output for a specified App")
        args = parser.parse_args()
        if not args.verbose and not args.name:
            api_response = api_instance.list_app1()
            print(f"\nThere are {len(api_response.to_dict()['items'])} configured Apps\n")
            dict = api_response.to_dict()
            name_width = get_max_width(dict, key1="meta", key2="name")
            port_width = get_max_width (dict, key1="spec", key2="proto_ports")
            alg_width = 15
            alg_type_width = 15
            protocol_width = 15
            modified_dict = {}
            current_list_index = 1
            for i in range(len(dict["items"])):
                n=0
                try:
                    for j in range(len(dict["items"][i]["spec"]["proto_ports"])):
                        if n == 0:
                            try:
                                if dict["items"][i]["spec"]["alg"]:
                                    app_name = dict['items'][i]['meta']['name']
                                    modified_dict[current_list_index]=[app_name]
                                    is_alg = "Yes"
                                    alg_type = dict["items"][i]["spec"]["alg"]["type"]
                                    protocol = dict["items"][i]["spec"]["proto_ports"][j]["protocol"]
                                    ports = dict["items"][i]["spec"]["proto_ports"][j]["ports"]
                                    modified_dict[current_list_index].extend([is_alg, alg_type, protocol, ports])
                                    current_list_index+=1
                                    n+=1
                            except KeyError:
                                app_name = dict['items'][i]['meta']['name']
                                modified_dict[current_list_index]=[app_name]
                                is_alg = "-"
                                alg_type = "-"
                                protocol = dict["items"][i]["spec"]["proto_ports"][j]["protocol"]
                                ports = dict["items"][i]["spec"]["proto_ports"][j]["ports"]
                                modified_dict[current_list_index].extend([is_alg, alg_type, protocol, ports])
                                current_list_index+=1
                                n+=1
                        else:
                            app_name = ""
                            modified_dict[current_list_index]=[app_name]
                            is_alg = "-"
                            alg_type = "-"
                            protocol = dict["items"][i]["spec"]["proto_ports"][j]["protocol"]
                            ports = dict["items"][i]["spec"]["proto_ports"][j]["ports"]
                            modified_dict[current_list_index].extend([is_alg, alg_type, protocol, ports])
                            current_list_index+=1
                except KeyError:
                    app_name = dict['items'][i]['meta']['name']
                    modified_dict[current_list_index]=[app_name]
                    is_alg = "Yes"
                    alg_type = dict["items"][i]["spec"]["alg"]["type"]
                    protocol = ""
                    ports = ""
                    modified_dict[current_list_index].extend([is_alg, alg_type, protocol, ports])
                    current_list_index+=1
            print("App Name".ljust(name_width) + "ALG".ljust(alg_width) + "ALG Type".ljust(alg_type_width) + "Protocol".ljust(protocol_width) + "Ports")
            print(".........".ljust(name_width) + "....".ljust(alg_width) + ".........".ljust(alg_type_width) + ".........".ljust(protocol_width) + "......")
            for key, value in modified_dict.items():
                app_name, alg, alg_type, protocol, ports = value
                print(f"{app_name.ljust(name_width)}{alg.ljust(alg_width)}{alg_type.ljust(alg_type_width)}{protocol.ljust(protocol_width)}{ports}")
        if args.verbose:
             api_response = api_instance.list_app1()
             pprint(api_response.to_dict())
        if args.name:
            api_response = api_instance.list_app1(o_name=args.name)
            pprint(api_response.to_dict())

    except pensando_dss.psm.ApiException as e:
        print("Exception when calling SecurityV1Api->list_app1: %s\n" % e)
