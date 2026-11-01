"""IPv6 Network Address & EUI-64 Host Interface Toolkit."""

import ipaddress
from typing import Dict, Optional


class Ipv6Toolkit:
    """IPv6 address calculations and RFC 4291 EUI-64 generation."""

    @staticmethod
    def generate_eui64(prefix: str, mac_address: str) -> str:
        """
        Derives an IPv6 modified EUI-64 address from a /64 prefix and 48-bit MAC.

        Algorithm (RFC 4291):
        1. Clean MAC address into 12 hex digits.
        2. Insert 0xFFFE into the middle (after 6th hex digit).
        3. Flip the Universal/Local (U/L) bit (bit 7 of the 1st byte, XOR with 0x02).
        4. Combine 64-bit interface ID with the top 64 bits of the network prefix.
        """
        clean_mac = mac_address.replace(":", "").replace("-", "").replace(".", "").lower()
        if len(clean_mac) != 12:
            raise ValueError(f"Invalid MAC address format: '{mac_address}'")

        net = ipaddress.IPv6Network(prefix if "/" in prefix else prefix + "/64", strict=False)
        top_64_int = int(net.network_address) & (0xFFFFFFFFFFFFFFFF << 64)
        iid_int = int(clean_mac[:6] + "fffe" + clean_mac[6:], 16) ^ (0x02 << 56)
        full_int = top_64_int | iid_int
        return str(ipaddress.IPv6Address(full_int))

    @staticmethod
    def classify_address(ip_str: str) -> Dict[str, bool]:
        """Classifies address scope per RFC 4291 / RFC 3587."""
        addr = ipaddress.IPv6Address(ip_str)
        return {
            "is_link_local": addr.is_link_local,
            "is_global_unicast": addr.is_global,
            "is_multicast": addr.is_multicast,
            "is_loopback": addr.is_loopback
        }
