# SecuritySGRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | SGRule action, either PERMIT, DENY or REJECT. | [optional]  if omitted the server will use the default value of "permit"
**apps** | **[str]** | list of apps objects to which the rule applies to. | [optional] 
**description** | **str** | describes rule. Length of string should be between 0 and 256. | [optional] 
**from_ip_addresses** | **[str]** | inbound rule from a given ip-address/ip-mask/ip-range. Use any to refer to all ipaddresses cli-tags: id&#x3D;from-ip. | [optional] 
**from_security_groups** | **[str]** | inbound rule from a given security group. | [optional] 
**name** | **str** | rule name. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 0 and 64. | [optional] 
**proto_ports** | [**[SecurityProtoPort]**](SecurityProtoPort.md) | list of (protocol, ports) pairs to which the rule applies to, in addition to apps. | [optional] 
**to_ip_addresses** | **[str]** | outbound rule from a given ip-address/ip-mask/ip-range. Use any to refer to all ipaddresses cli-tags: id&#x3D;to-ip. | [optional] 
**to_security_groups** | **[str]** | outbound rule from a given security group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


