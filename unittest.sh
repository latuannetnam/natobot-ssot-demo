# invoke unittest -f -k -s -v
# invoke unittest -k -s -v
# invoke unittest --no-buffer -f -k -s -v -l nautobot_device_onboarding.tests.test_command_getter_junos
# invoke unittest --no-buffer -f -k -s -v -l nautobot_device_onboarding.tests.test_command_mapper_juniper_junos
# invoke unittest --no-buffer -f -k -s -v -l nautobot_device_onboarding.tests.test_command_getter_junos.TestJuniperJunosCommandGetterExtraction.test_extract_interface_description
# invoke unittest --no-buffer -f -k -s -v -l nautobot_device_onboarding.tests.test_command_getter_junos
# invoke unittest --no-buffer -f -k -s -v -l nautobot_device_onboarding.tests.test_command_getter_junos_interfaces
# invoke unittest --no-buffer -f -k -s -v -l nautobot_device_onboarding.tests.test_command_getter_junos_interfaces.TestJuniperJunosInterfaceExtractors
#poetry run invoke unittest --no-buffer -f -k -s -v -l nautobot_device_onboarding.tests.test_command_getter_junos_vlan.TestJuniperJunosInterfaceVLANExtractors.test_extract_interface_untagged_vlan_new
# invoke unittest --no-buffer -f -k -s -v -l nautobot_device_onboarding.tests.test_command_getter_junos_vlan
poetry run invoke unittest --no-buffer -f -k -s -v -l nautobot_ssot_demo.tests.test_views