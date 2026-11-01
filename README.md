# IPv6 Address Toolkit

Classifies IPv6 address scopes and derives modified EUI-64 interface identifiers from a /64 prefix and a 48-bit MAC address.

## Main entry points

- `src.ipv6.Ipv6Toolkit` (`generate_eui64, classify_address`)

## Run the tests

```bash
python -m unittest discover -s tests -v
```

The project uses the Python standard library; no third-party package is required.

## Scope

EUI-64 generation is provided for study and lab use. Many networks use privacy addresses or manually assigned interface identifiers instead.
