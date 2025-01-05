### IPv4 vs IPv6 Cheat Sheet

#### **Overview**
| Feature              | **IPv4 (Internet Protocol Version 4)** | **IPv6 (Internet Protocol Version 6)**  |
|----------------------|-----------------------------------------|-----------------------------------------|
| **Address Format**   | 32-bit (e.g., 192.168.1.1)             | 128-bit (e.g., 2001:0db8:85a3::8a2e:0370:7334) |
| **Total Addresses**  | ~4.3 billion (2³²)                     | Virtually unlimited (~3.4 × 10³⁸)       |
| **Header Size**      | 20 bytes                               | 40 bytes                                |
| **Adoption**         | Widely used, but limited addresses      | Growing adoption for scalability        |

---

#### **Key Functionalities**

##### **IPv4**
1. **Addressing**: 
   - Written in dot-decimal format (e.g., `192.168.0.1`).
   - Network classes (A, B, C, D, E) and subnet masks.
2. **Routing**: 
   - Uses NAT (Network Address Translation) to conserve addresses.
3. **Configuration**:
   - Can be manual (static) or automatic via DHCP.
4. **Broadcast Support**:
   - Allows sending packets to all hosts in a subnet.
5. **Security**: 
   - Relies on additional protocols like IPsec (not built-in).
6. **Use Cases**:
   - Legacy systems, networks not needing extensive address space.

---

##### **IPv6**
1. **Addressing**: 
   - Written in hexadecimal and colon-separated (e.g., `fe80::1`).
   - Provides unique global addresses for every device.
2. **Routing**: 
   - Eliminates the need for NAT, making direct communication simpler.
3. **Configuration**:
   - Supports auto-configuration (SLAAC) and DHCPv6.
4. **Multicast and Anycast**: 
   - Replaces IPv4's broadcast with multicast; supports anycast addressing.
5. **Security**: 
   - IPsec is built into IPv6 protocol by default.
6. **Other Features**:
   - Simplified header structure for better performance.
   - Supports mobility and IoT devices effectively.
7. **Use Cases**:
   - Modern networks, future-proof applications, IoT.

---

#### **Comparison of Features**
| Feature                  | **IPv4**                          | **IPv6**                            |
|--------------------------|------------------------------------|-------------------------------------|
| **Address Length**       | 32 bits                           | 128 bits                            |
| **Address Format**       | Dot-decimal (e.g., `192.168.1.1`) | Hexadecimal (e.g., `2001:db8::1`)   |
| **Address Space**        | ~4.3 billion                     | ~340 undecillion                   |
| **Header Complexity**    | Complex, variable fields          | Simpler, fixed fields               |
| **Fragmentation**        | Routers and sending host          | Sending host only                   |
| **Checksum**             | Present                          | Not required                        |
| **NAT**                  | Required due to address shortage  | Not required                        |
| **Security**             | Add-on (IPsec optional)          | Built-in (IPsec mandatory)          |

---

#### **Quick Tips**
- **IPv4**: Best for legacy systems and small networks.
- **IPv6**: Essential for scalability, IoT, and modern networks.