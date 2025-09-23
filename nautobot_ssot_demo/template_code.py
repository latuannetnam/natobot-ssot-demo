INTERFACE_IPADDRESSES = """
{% for ip in record.interface.ip_addresses.all %}
    <a href="{{ ip.get_absolute_url }}">{{ ip }}</a> (<a href="{{ ip.parent.namespace.get_absolute_url }}">{{ ip.parent.namespace }}</a>)<br />
{% endfor %}
"""