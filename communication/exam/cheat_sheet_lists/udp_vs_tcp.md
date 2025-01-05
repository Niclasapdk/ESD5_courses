### UDP vs TCP Cheat Sheet

#### **Overview**
| Feature             | **TCP (Transmission Control Protocol)**   | **UDP (User Datagram Protocol)**  |
|---------------------|-------------------------------------------|-----------------------------------|
| **Type**            | Connection-oriented                      | Connectionless                   |
| **Reliability**     | Reliable: ensures delivery and order      | Unreliable: no delivery guarantee |
| **Speed**           | Slower due to overhead                   | Faster due to minimal overhead   |
| **Use Cases**       | Data integrity critical                  | Speed or low-latency critical    |

---

#### **Key Functionalities**

##### **TCP (Transmission Control Protocol)**
1. **Connection Establishment**: 
   - Uses a three-way handshake process: SYN → SYN-ACK → ACK.
2. **Data Transfer**: 
   - Provides reliable delivery by retransmitting lost packets.
   - Ensures data arrives in order using sequence numbers.
3. **Flow Control**: 
   - Adjusts the rate of data flow using sliding windows to prevent overwhelming the receiver.
4. **Error Checking**: 
   - Uses checksums for error detection and retransmission for error correction.
5. **Congestion Control**: 
   - Implements algorithms like AIMD (Additive Increase/Multiplicative Decrease) to handle network congestion.
6. **Applications**: 
   - HTTP/HTTPS, FTP, Email (SMTP, IMAP, POP3), SSH.

---

##### **UDP (User Datagram Protocol)**
1. **Connectionless Transmission**: 
   - No need to establish a connection; data is sent directly to the destination.
2. **Unreliable Delivery**: 
   - Packets may be lost, arrive out of order, or be duplicated without retransmission.
3. **Low Overhead**: 
   - Minimal protocol mechanisms make it fast and lightweight.
4. **Broadcasting & Multicasting**: 
   - Supports one-to-many communication efficiently.
5. **Error Checking**: 
   - Uses checksums for error detection but does not correct errors.
6. **Applications**: 
   - Video streaming, VoIP, DNS, online gaming, TFTP.

---

#### **Comparison of Headers**
| Feature             | **TCP Header**       | **UDP Header**    |
|---------------------|----------------------|-------------------|
| **Header Size**     | 20–60 bytes          | 8 bytes           |
| **Fields**          | Sequence number, acknowledgment, flags, window size, etc. | Source port, destination port, length, checksum. |

---

#### **Quick Tips**
- Use **TCP** when reliability, order, and data integrity are essential (e.g., file transfers, web browsing).
- Use **UDP** when speed, low latency, and simplicity are critical (e.g., live video, voice chat). 

Would you like to expand on any specific area or see examples?-chat