import unittest
from src.ipv6 import Ipv6Toolkit

class TestIpv6(unittest.TestCase):
    def test_eui64_derivation(self):


        eui = Ipv6Toolkit.generate_eui64("2001:db8::", "00:11:22:33:44:55")
        self.assertEqual(eui, "2001:db8::211:22ff:fe33:4455")

    def test_classification(self):
        info_ll = Ipv6Toolkit.classify_address("fe80::1")
        self.assertTrue(info_ll["is_link_local"])
        self.assertFalse(info_ll["is_global_unicast"])

        info_global = Ipv6Toolkit.classify_address("2600::1")
        self.assertTrue(info_global["is_global_unicast"])

if __name__ == "__main__":
    unittest.main()
