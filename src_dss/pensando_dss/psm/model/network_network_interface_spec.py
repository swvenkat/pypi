"""
    Network API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from pensando_dss.psm.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from pensando_dss.psm.model.cluster_ip_config import ClusterIPConfig
    from pensando_dss.psm.model.network_pause_spec import NetworkPauseSpec
    globals()['ClusterIPConfig'] = ClusterIPConfig
    globals()['NetworkPauseSpec'] = NetworkPauseSpec


class NetworkNetworkInterfaceSpec(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('admin_status',): {
            'UP': "up",
            'DOWN': "down",
        },
        ('ip_alloc_type',): {
            'NONE': "none",
            'STATIC': "static",
            'DHCP': "dhcp",
        },
        ('type',): {
            'NONE': "none",
            'HOST-PF': "host-pf",
            'UPLINK-ETH': "uplink-eth",
            'UPLINK-MGMT': "uplink-mgmt",
            'LOOPBACK-TEP': "loopback-tep",
            'HOST-VF': "host-vf",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'admin_status': (str,),  # noqa: E501
            'attach_network': (str,),  # noqa: E501
            'attach_tenant': (str,),  # noqa: E501
            'connection_tracking': (bool,),  # noqa: E501
            'enable_fw_logging': (bool,),  # noqa: E501
            'ip_alloc_type': (str,),  # noqa: E501
            'ip_config': (ClusterIPConfig,),  # noqa: E501
            'mac_address': (str,),  # noqa: E501
            'mtu': (int,),  # noqa: E501
            'pause': (NetworkPauseSpec,),  # noqa: E501
            'speed': (str,),  # noqa: E501
            'tx_policer': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'vnf_attached': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'admin_status': 'admin-status',  # noqa: E501
        'attach_network': 'attach-network',  # noqa: E501
        'attach_tenant': 'attach-tenant',  # noqa: E501
        'connection_tracking': 'connection-tracking',  # noqa: E501
        'enable_fw_logging': 'enable-fw-logging',  # noqa: E501
        'ip_alloc_type': 'ip-alloc-type',  # noqa: E501
        'ip_config': 'ip-config',  # noqa: E501
        'mac_address': 'mac-address',  # noqa: E501
        'mtu': 'mtu',  # noqa: E501
        'pause': 'pause',  # noqa: E501
        'speed': 'speed',  # noqa: E501
        'tx_policer': 'tx-policer',  # noqa: E501
        'type': 'type',  # noqa: E501
        'vnf_attached': 'vnf-attached',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """NetworkNetworkInterfaceSpec - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            admin_status (str): desired Admin state of the port.. [optional] if omitted the server will use the default value of "up"  # noqa: E501
            attach_network (str): AttachNetwork associates the interface with a Network. This is only valid for HOST_PF type.. [optional]  # noqa: E501
            attach_tenant (str): [optional]  # noqa: E501
            connection_tracking (bool): ConnectionTracking enables connection tracking on the interface. This is valid only for HOST_PF type.. [optional] if omitted the server will use the default value of False  # noqa: E501
            enable_fw_logging (bool): EnableFwLogging enables flow logging on the interface. This is valid only for HOST_PF type.. [optional]  # noqa: E501
            ip_alloc_type (str): [optional] if omitted the server will use the default value of "none"  # noqa: E501
            ip_config (ClusterIPConfig): [optional]  # noqa: E501
            mac_address (str): Override system allocated MAC address. Should be a valid MAC address.. [optional]  # noqa: E501
            mtu (int): Mtu of the interface.. [optional]  # noqa: E501
            pause (NetworkPauseSpec): [optional]  # noqa: E501
            speed (str): Intefaae speed.. [optional]  # noqa: E501
            tx_policer (str): [optional]  # noqa: E501
            type (str): Type specifies the type of interface.. [optional] if omitted the server will use the default value of "none"  # noqa: E501
            vnf_attached (bool): VNFAttached knob on the interface. This is valid only for HOST_PF type.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
