# Lecture 5 - Communication systems

## Problem 1

a. Minimum number of frames required to convey 5000 bytes of data.

Max. data length is 64 bytes.

```py
from math import ceil
numframes = ceil(5000/64)
# 79
```

So 79 frames required.

b. Minimum time required with 1 kbit/s data rate, error-free communication and no ARQ.

Frame length (in bits) at max data length is

```py
maxlen = 8 + 6 + 1 + 1 + 8 + 64*8
# 536
datarate = 1000
numbits = numframes * maxlen
mintime = numbits / datarate
# 42.344
```

42.344 seconds

c. efficiency of protocol and goodput.

```py
goodput = datarate * 64*8 /maxlen
# 955.2 bits pr second
```

d. Change frame when only alice transmits and fixed packet length of 64 bytes

Drop pkt length and other seq number.

```py
maxlen_new = 8 + 1 + 8 + 64*8
# 529
goodput_new = datarate * 64*8 / maxlen_new
# 967.9 bits pr second
```

## Problem 2

```py
# time to transmit frame
t_f = {
    "min": 5e-3,
    "avg": 10e-3,
    "max": 20e-3}

# time to know if frame has been lost
t_f_lost = {k: 2*v for (k, v) in t_f.items()}
# {'min': 0.01, 'avg': 0.02, 'max': 0.04}

# average throughput in bits/s
# data transmission delay (when 0% packet error rate)
t_avg_ideal = t_f["avg"] + t_f_lost["avg"]
# 0.0300 s
frame_len = 536
throughput_avg = frame_len / t_avg_ideal
# 17866.7

# 
num = 10000
p_PER = 1/100
retransmissions = num * p_PER
# 100
t_avg_successful_retrans = (t_f["avg"] + t_f_lost["avg"])/(1-p_PER)
# 0.0303 s
```

## Problem 3

a. No...

b. Hello world time

```py
baud = 9600
sent = "hello world"
l = len(sent)*8
# 88
f_len = 1 + 8 + 1
t_hello = (l / f_len) / baud
# 0.92 ms
```

c.

It is 0x61 or 'a' and parity is 1.

i. 01110001 is 0x71 or 'q' and parity is 0.
ii. 01110101 is 0x75 or 'u' and parity is 1.

## Problem 4

a.

```py
def p_k(p_PER, k): return (1-p_PER) * (p_PER ** (k-1))

def p_success_after_k(p_PER, k):
    acc = 0
    for ki in range(1, k+1):
        acc += p_k(p_PER, ki)
    return acc

p_PER = 0.1
p_success_after_k(p_PER, 1)
# 0.9
p_success_after_k(p_PER, 2)
# 0.99
```
