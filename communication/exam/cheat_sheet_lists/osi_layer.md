Headers in different layers of the **OSI model** or **TCP/IP model** contain information necessary for data communication. Here's a breakdown of the headers at each layer:

---

### **1. Physical Layer (Layer 1)**
- **Header Content**: 
  - Does not use headers in the traditional sense.
  - Contains raw bitstreams and physical signaling.

---

### **2. Data Link Layer (Layer 2)**
- **Header Content**: 
  - **Source MAC Address**: Hardware address of the sending device.
  - **Destination MAC Address**: Hardware address of the receiving device.
  - **Frame Type**: Indicates the protocol (e.g., IPv4, IPv6) encapsulated in the payload.
  - **Error Detection (FCS - Frame Check Sequence)**: Used for error detection in frames.

---

### **3. Network Layer (Layer 3)**
- **Header Content**:
  - **Source IP Address**: Identifies the sending device’s network layer address.
  - **Destination IP Address**: Identifies the receiving device’s network layer address.
  - **Protocol Type**: Indicates the transport layer protocol (e.g., TCP, UDP) encapsulated.
  - **TTL (Time to Live)**: Prevents infinite loops in routing by limiting the lifetime of a packet.
  - **Fragmentation Info**: Assists in reassembly of fragmented packets.

---

### **4. Transport Layer (Layer 4)**
- **Header Content**:
  - **Source Port**: Identifies the application on the sending device.
  - **Destination Port**: Identifies the application on the receiving device.
  - **Sequence Number**: Used to reassemble data in the correct order.
  - **Acknowledgment Number**: Confirms receipt of data from the sender.
  - **Flags**: Control flags for connection management (e.g., SYN, ACK, FIN).
  - **Window Size**: Specifies the amount of data the sender can send without acknowledgment.
  - **Checksum**: Ensures data integrity.

---

### **5. Session Layer (Layer 5)** 
- **Header Content**:
  - **Session ID**: Unique identifier for maintaining session state.
  - **Synchronization Information**: Helps manage dialog control and session checkpoints.

---

### **6. Presentation Layer (Layer 6)**
- **Header Content**:
  - **Encryption Information**: Details of encryption schemes applied to the payload.
  - **Data Format Description**: Specifies the format or encoding (e.g., ASCII, JPEG).

---

### **7. Application Layer (Layer 7)**
- **Header Content**:
  - **Application-Specific Data**: Includes HTTP headers (e.g., Host, User-Agent) or SMTP commands for email.
  - **Protocol Information**: Indicates the specific application protocol (e.g., HTTP, FTP).

---

Each header layer provides information necessary for the layer's specific responsibilities, ensuring seamless communication and data transfer between devices in a network.