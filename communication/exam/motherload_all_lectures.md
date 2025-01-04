
# Alle Opgaver Løst igen ark :)
# Lecture 1

![](./motherload_all_lectures_media//)


(a) Solution:


![](./motherload_all_lectures_media//)

```matlab
close all
clear
r = 100;
Etheta = 5;
eta = 120*pi;
Wrad = abs(Etheta)^2/(2*eta) %answer in W/m^2
```

```matlabTextOutput
Wrad = 
        0.0331572798108115

```

![](./motherload_all_lectures_media//)


Solution:


 ![](./motherload_all_lectures_media//)

```matlab
syms t g
fun1 = int(Wrad*r^2*sin(t),t,0,pi);
Prad = int(fun1,g,0,2*pi);
vpa(Prad) %answer in W;
```
ans = 
 $\displaystyle 4166.6666666666676908934378419728$
 

![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)

```matlab
close all
clear
Umax = 200e-3;
inputpower = 125.66e-3;
Prad = 0.9*inputpower;
D0 = (4*pi*Umax)/(Prad);%dimensionsless
D0dB = 10*log10(D0);%dB
G0 = 0.9*D0;
G0dB=10*log10(G0);
```

![](./motherload_all_lectures_media//)


solution:


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Solution: 


![](./motherload_all_lectures_media//)

```matlab
syms t
Umax = 1;
Prad = 2*pi*(int(sin(t),t,deg2rad(0),deg2rad(20)) + int(0.342*csc(t)*sin(t),t,deg2rad(20),deg2rad(60)) + int(0*sin(t),t,deg2rad(60),deg2rad(180)));
D0 = (4*pi*Umax)/(Prad);
vpa(D0);
toDbD0 = 10*log10(D0);
vpa(toDbD0);
```

![](./motherload_all_lectures_media//)


Solution: Husk at hvis Umax ikke er givet så er den normaliseret til 1!!


![](./motherload_all_lectures_media//)

```matlab
close all
clear
syms t
Umax = 1;
Prad = int(sin(t)^2,t,0,2*pi) * int(cos(t)^4*sin(t)^2*sin(t),t,0,pi/2); % Andet svar men jeg kan ikke se hvordan svaret kan være rigtigt?
% Johns cook
vpa(Prad);
D0 = 4*pi*Umax/Prad;
vpa(10*log10(D0))
```
ans = 
 $\displaystyle 18.450980400142568307122162585926$
 

![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)

```matlab
close all
clear
syms x
HPBW = solve(cos(x/2)^4==1/2,x);
deg = rad2deg(HPBW);
vpa(deg) % vælg det tal uden imaginær og positiv altid! Måske :)
```
ans = 
 $\displaystyle \left(\begin{array}{c} -65.530199479297808348650789880557\newline 65.530199479297808348650789880557\newline -180.0+87.580662372692780339764902555967\,\mathrm{i}\newline 180.0-87.580662372692780339764902555967\,\mathrm{i} \end{array}\right)$
 
# Lecture 2

![](./motherload_all_lectures_media//)


Solution to a) b) c)


Slide 5 lecture 2 for formel men den er isotropic og derfor kun dele af formlen bliver brugt.


a) b) og c)


![](./motherload_all_lectures_media//)

```matlab
close all
clear
syms;
% chose the small frequency instead apparently for the first, and middle
% for last and so on for the gainzz.
etDo = db2pow([14.8 16.5 18]);
lam = 3e8./[8.2e9 10.3e9 12.4e9];
Aem = etDo.*(lam.^2/(4*pi)) %HUSK ISQ :D
```

```matlabTextOutput
Aem = 1x3    
       0.00321665838623415       0.00301549210670105       0.00293893022335922

```

```matlab
A = 5.5*7.4;% cm^2 selvfølglig at kigge på enheder er lidt som at snyde jo :))
```

![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)

```matlab
close all
clear
R = 36000e3;
f = 2e9;
Pt = 8;
Wo = Pt/(4*pi*R^2); %W/m^2 unit
```

![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)

```matlab
Do = db2pow(60);
Pr = 10^6*(3e8/2e9)^2/(4*pi)*Wo; %HAH ingen afrunding BITCH
```

![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)

```matlab
close all
clear
Gt = db2pow(20);
Gr = db2pow(15);
R = 1e3;
Pi = 150;
f = 1e9;
lam = 3e8/f;
Pr = Gr*Gt*(lam/(4*pi*R))^2*Pi;
num2sip(Pr)
```

```matlabTextOutput
ans = '270.34 µ'
```

![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


1)

```matlab
close all
clear
Gr = db2pow(15);
Gt = db2pow(20);
Pt = 150;
d = 1e3;
f = 1e9;
lam = 3e8/f;
ht = 3;
hr = 3;
Pr = Gr*Gt*((ht*hr)/((d)^2))^2*Pt;
num2sip(Pr); % for 3 meter anden formel for den anden grundet en relation
```

2)

```matlab
ht1 = [5 10]; 
hr1 = [5 10];
4*Pt*(lam/(4*pi*d))^2.*Gr.*Gt*sin((2*pi.*ht1.*hr1)/(d*lam)).^2;
```

![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)

# Lecture 3

![](./motherload_all_lectures_media//)


Solution:

# Lecture 5

![](./motherload_all_lectures_media//)


(a) What is the minimum number of frames required to be transmitted by Alice in order to convey the 5,000 bytes of data to Bob?


Solution:

```matlab
number_frames = ceil(5000/64)% frames :)
```

```matlabTextOutput
number_frames = 
    79

```

(b) Consider that the communication channel that connects Alice and Bob supports a data rate of 1 kbit/s. What would be the minimum time required for Alice’s data to reach Bob if the ARQ procedure was not present and communication was error\-free?


Solution:

```matlab
totalbits = (24+(64*8))*number_frames; % Hele framen bruges.
min_time = totalbits/1e3; % 1e3 = 1kbits
```

(c) What is the efficiency of the protocol adopted? Then, what is the goodput in bit/s following the considerations made in (b)?


Solution:

```matlab
effeciency = (64*8)/((64*8)+24) %mængde data tæller, totalmængde bits i nævner
```

```matlabTextOutput
effeciency = 
         0.955223880597015

```

```matlab
goodput = 1e3*effeciency %bits/s
```

```matlabTextOutput
goodput = 
          955.223880597015

```

(d) Considering a very specific scenario where only Alice transmits and Bob receives with a fixed data packet length of 64 bytes. How would you change the frame to make the protocol more efficient? What is the efficiency gain and the new goodput when comparing the new protocol to the old one?


Solution:


Fjern pkt length nu hvor size er fixed.

```matlab
new_effeciency = 512/530; % 530 = uden packet length
new_goodput = new_effeciency*1e3;
```

```matlabTextOutput
new_goodput = 
          966.037735849057

```

![](./motherload_all_lectures_media//)


(a) What is the minimum time required by Alice to know that a frame has been lost? And the maximum?


Solution: 5ms+5ms (min) 20ms + 20ms(max) 


(b) Assuming that all frames are received successfully, what is the average throughput in bit/s of Alice’s transmission by considering now the ACKs from Bob?


Solution: $\frac{536\textrm{bits}\cdot 79\;\textrm{frames}}{20\textrm{ms}\cdot 79\;\textrm{frames}}=26800\frac{\textrm{bits}}{s}$ 

```matlab
average_throughput = (536*79)/(20e-3*79);
```

**Consider now that Alice transmits 10,000 frames to Bob and assume that every 100\-th frame is lost in transmission. Consider only that frames from Alice can be in error, while ACKs/NACKs are perfectly sent from Bob.**


(c) How many retransmissions would occur?

```matlab
retransmission = (10e3/100) + 1 % Husk at retransmission som man regner fra 10e3/100 også fejler derfor + 1 :)
```

```matlabTextOutput
retransmission = 
   101

```

(d) How long would it take to transmit all frames on average? Assume that all retrans\-mission is successful


Solution:

 $$ \frac{10100\;\textrm{frames}\cdot 536\;\textrm{bits}}{26\ldotp 8\textrm{E3}\;\textrm{averagethroughput}}=202\textrm{sekunder} $$ 
```matlab
average_transmit = (10100*536)/26.8e3;
```

Alternative answer:

```matlab
(10e3+100)*20e-3; %Total frame gange average delaye for receive
```

```matlabTextOutput
ans = 
   202

```

![](./motherload_all_lectures_media//)


Solution: FUCKING TEGN :)


(b) Consider a baud rate of 9,600 bit/s. How long would it take for to Alice send the sentence “hello world” to Bob assuming error\-free communication? Assume that each RS\-232 frame is comprised of a start bit and a stop bit and that there are no parity bits.

```matlab
x = (11*10)/(9600); % i sekunder for totalt mængde af karaktere(11) som fylder 10 bit
num2sip(x);
```

```matlabTextOutput
ans = '11.458 m'
```

![](./motherload_all_lectures_media//)


Solution: ACII = 'a' og paritiy bit = 1 grundet even parity hvilket medfører at man tæller antal '1' og da dette er ulige = 1 og modsat for hvis det var lige. For ulige parity så ville ulige antal 1 give 0 og omvendt.


&nbsp;&nbsp;&nbsp;&nbsp; (i) q and yes.


&nbsp;&nbsp;&nbsp;&nbsp; (ii) u and no, fordi det er lige parity og der er lige antal 1 så skulle det sidste bit være 0?


![](./motherload_all_lectures_media//)


Solution:


 $1-{\left(p_{\textrm{PER}} \right)}^{\textrm{Total}\;\textrm{transmissions}\left(K+M\right)}$ = $\textrm{proability}\;\textrm{of}\;\textrm{succesful}\;\textrm{transmission}$ 


![](./motherload_all_lectures_media//)


(b) Calculate the throughput for K = 1, and then for K = 2

 $$ \textrm{Number}\;\textrm{of}\;\textrm{packet}\left(M\right)\cdot \frac{\textrm{proability}\;\textrm{of}\;\textrm{succes}\;\textrm{transmissions}}{\textrm{number}\;\textrm{of}\;\textrm{transmissiomns}\left(M+K\right)}=1\cdot \frac{0\ldotp 99}{2}=0\ldotp 495\;\textrm{packet}\;\textrm{per}\;\textrm{slot} $$ 

 $$ 1\cdot \frac{0\ldotp 999}{3}=0\ldotp 333\;\textrm{Packet}\;\textrm{per}\;\textrm{slot} $$ 

(c) Characterize the relationship between the throughput, the probability of successful packet transmission, and the value of K.


Solution: Increasing the number of retransmissions leads to a higher probability of successful packet transmission for a single packet, while it deteriorates the throughput. **TLDR**: Betal ved kasse 1 


![](./motherload_all_lectures_media//)


Solution:


If the set number of retransmissions makes the total number of transmissions for the 2 packets higher than 5 slots, then the reliability is zero.


Fx: M=2 og K=1 så hvis hver message fejler og en retransmission sker så det totalt 4 hvilket er under 5 slots hvilket er godt. Mere end det så er reliability zero.


Notice that the reliability also depends on Bob successfully receiving the data packets. Hence, if the total number of transmissions for the 2 packets is below 5 slots, the communication reliability is defined by the packet error rate.

# Lecture 6

![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Solution: $\textrm{log2}\left(4\right)\;$ Hvor 4 er de forskellige different frame types.


![](./motherload_all_lectures_media//)


Solution: 

-  Det kan gå galt hvis de alle gerne vil snak med Basil på samme tid og der sker ingen ting. 
-  ACK can be lost in transmission for both parties and nothing happens then try again to fix it :) 

![](./motherload_all_lectures_media//)


Solution:


Based on the initial access frame, a link termination frame would be comprised of a reference signal sent by Basil to establish that this frame has begun. Then, Basil sends the address of the user that she wants to be terminated. The user listens to it and withdraws its connection. The user no longer has access to the network. 


![](./motherload_all_lectures_media//)


Solution: 1kbit /s bliver delt i mellem 3 som skal høre det hele

```matlab
1e3/3;
```

```matlabTextOutput
ans = 
          333.333333333333

```

![](./motherload_all_lectures_media//)


Solution: Jeg har lagt det på github og sæt billede ind.


![](./motherload_all_lectures_media//)


Solution:


User 1, Slot 3 and User 5 Slot 5


![](./motherload_all_lectures_media//)


Solution:  U have to pick either slot 3 or slot 5 since there are only one package which means the sequence will either start with user 1 or user 5.


![](./motherload_all_lectures_media//)


Solution:


 $\frac{{\left(1-\frac{1}{4}\right)}^{4-1} +{\left(1-\frac{1}{16}\right)}^{\left(16-1\right)} }{2}=0\ldotp 4$ Brug formlen som er i givet i opgave beskrivelsen.


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Solution:

 $$ 60+30+60+20+0+160+80=410 $$ 

![](./motherload_all_lectures_media//)


Solution: Det betyder at en node kan bruge lang tid på at sende så rimelig unfair :)


Ingen garanti på latens for at kommunikere.


![](./motherload_all_lectures_media//)


Solution: 50+30+50+20+50+50+50+10+10+50+30=400 (Så man skal to gange rund eftersom at 50 er maksimal det der kan sendes så der er en rest for nogen)


![](./motherload_all_lectures_media//)


Solution:

-  Increased: Node; 2,0,5 
-  Decreased: Node; 1,3,6,7 
-  Unchanged: Node; 4 

![](./motherload_all_lectures_media//)


Solution:


If we think of time when doing a full circle of the ring, Node 0 may communicate again after 300 ms. If we consider the maximum time we may use the medium (50 ms), Node 0 knows at least 6 nodes are in the system since 300. If we consider the maximum time we may use the medium (50ms), Node 0 knows atleast 6 nodes are in the system since $\frac{300}{50}=6$ 


![](./motherload_all_lectures_media//)


It wouldnt know, but with round robin it would since max delay time is implemented?

# Lecture 7

Wireshark opgave sæt billeder ind????


Payload er 40 bytes istedet for 48 bytes som der står i github til løsning 2.e

# Lecture 8
![](./motherload_all_lectures_media//)

Solution: Number of vertices \- 1 so it is 4


![](./motherload_all_lectures_media//)


Solution:


 ![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Solution:


Which is 40 instructions in 40 nanoseconds.


64 bits i pakken = 8 bytes:


 $\frac{8}{40e-9}=5\textrm{nano}\;\textrm{sekund}$ for enkelt byte men vi har gigabitpersekund så derfor: $\frac{8\textrm{bit}}{5e-9\textrm{sekund}}=1600\frac{\textrm{gigabit}}{\textrm{sekund}}$ hvilket vil sige at den kan håndtere det eftersom det er større end 1 gigabit.


Egen solution fra github:


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Solution: At der var for få addreser i IPV4 og derfor blev IPV6 lavet :)


Eftersom at TCP kan snakke sammen på forskellige versioner af sig selv men det kan IP (fordi det er fysisk) og derfor er det reluctance.


![](./motherload_all_lectures_media//)


Solution:


Det tilføjer at man kan se om man bruger det 32bit acknowledge field.


Det spild hvis man nu ikke skal bruge feltet.


![](./motherload_all_lectures_media//)

# Lecture 9

![](./motherload_all_lectures_media//)


Solution: 

-  ECB; Much data must not have patterns cause it can be decrypted then. 
-  CBC; Packet cannot be lost since decryption is then impossible for subsequent packages. 

![](./motherload_all_lectures_media//)


Solution: The receiver can only verify the message contents and the sender but not the transmitter can not verify anything.


But if they both send a message the receivers can decrypt the same thing iguees?.


![](./motherload_all_lectures_media//)


Solution: YES :)


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Solution: Held og lykke brormand :)


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Man stoler på de certificates der kommer fra en authority ![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)

# Lecture 11
### problem 1

![](./motherload_all_lectures_media//)


Solution: 


use formula $R\left(\textrm{code}\;\textrm{rate}\right)=\frac{\log_2 \left(\textrm{bits}\right)}{\textrm{channel}\;\textrm{use}\left(n\right)}=\frac{3}{6}=0\ldotp 5$ 


![](./motherload_all_lectures_media//)


Solution:


forskellen i frekvens + 2\*R


![](./motherload_all_lectures_media//)

 $$ \textrm{BW}={f_{\textrm{mark}} -f}_{\textrm{space}} +2\cdot R_{\textrm{sym}} \Rightarrow 700\textrm{kHz}-500\textrm{kHz}+2\cdot 10\textrm{kbps}=220\textrm{kHz} $$ 

![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)


16\-PSK


![](./motherload_all_lectures_media//)


16 symbols


![](./motherload_all_lectures_media//)


log2(16)=4bits


![](./motherload_all_lectures_media//)


10000\*4=40000


![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)


log2(16)=4bits


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Yes, the order in which the symbols are labeled matters. We can use for example Gray labeling. The idea is to reduce the quantity of errors and make them easier to be detected.    


![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)


kigger på største eksponent hvilket er 3 ergo 3 bits requried


![](./motherload_all_lectures_media//)


 

```matlab
padmessage = [0 0 0 1 1 0 1 1];%husk lsb først
crcpoly = [1 1 0 1];%det er fra polynomiet som giver 1 0 1 1 som kommer fra exponenterne(husk igen lsb først)
[q,r] = gfdeconv(padmessage,crcpoly)%
```

```matlabTextOutput
q = 1x5    
     1     1     1     1     1

r = 1
```

derfor er crc 001 og hele message er 11011001


![](./motherload_all_lectures_media//)

```matlab
padmessage = [1 0 0 0 1 0 1 1];
crcpoly = [1 1 0 1];
[q,r] = gfdeconv(padmessage,crcpoly)% r er forskellige fra 0 ergo har den fundet fejlen
```

```matlabTextOutput
q = 1x5    
     0     1     1     1     1

r = 1x2    
     1     1

```

hele message 11010011 fordi crc er forskellig fra 0 kan den detektere fejlen


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)


det er en fejl at $n_{i,2}$ står dobbelt der skulle stå $n_{i,1}$ da noisen ikke er den samme for begge.


per retranmission skaleres SNR linært 



![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)



![](./motherload_all_lectures_media//)


Solution:


![](./motherload_all_lectures_media//)


a) x(t) => 8000 \* 2 = 16kHz , (den højeste frekvens i signalet)


b) y(t) => 16000\*2=32kHz


c) x(t)+y(t)=> tager du den højeste derfor 32 kHz


d) x(t)y(t) => der addere du de to, 16+32= 48kHz


![](./motherload_all_lectures_media//)


e) $\begin{array}{l} T=\frac{1}{F}=\frac{1}{16\textrm{kHz}}=62\ldotp 5\textrm{us}\newline \frac{1\textrm{ms}}{62\ldotp 5\textrm{us}}=16\;\textrm{samples} \end{array}$ 


f) Solution code for plotting graph.

```matlab
close all
clear
% Parameters
Ax = 1;          % Amplitude, you can adjust this value
a_x = 8000;      % Frequency in Hz, you can adjust this value as well

% Continuous Time Vector for Smooth Plot
fs_continuous = 100000;           % High sampling frequency for smooth plot
t_continuous = 0:1/fs_continuous:0.001; % Time vector for continuous plot

% Discrete Time Vector for 16 samples over 1 ms
num_samples = 16;                 % Number of samples within 1 ms
t_samples = linspace(0, 0.001, num_samples); % 16 equally spaced points from 0 to 1 ms

% Continuous Signal Definition
x_t_continuous = Ax * (sin(2 * pi * 4000 * t_continuous) + cos(2 * pi * a_x * t_continuous));

% Sampled Signal Definition
x_t_samples = Ax * (sin(2 * pi * 4000 * t_samples) + cos(2 * pi * a_x * t_samples));

% Plotting
figure;
plot(t_continuous * 1000, x_t_continuous, 'b-', 'LineWidth', 1.5); % Continuous signal plot
hold on;
stem(t_samples * 1000, x_t_samples, 'r', 'LineWidth', 1.5); % Sampled signal plot
xlabel('Time (ms)');
ylabel('x(t)');
title('Plot of x(t) over 1 ms with 16 samples');
legend('Continuous Signal', 'Sampled Signal (16 samples)');
grid on;
hold off;
```


![](./motherload_all_lectures_media//)


Solution: Impossible since the gap between bits are to large to reconstruct the signal or simply look at graph :).


 ![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)


Solution: Indsæt løsning for expansion af spectrum ligning og billede fra tavle.


Tavle løsning: 


![](./motherload_all_lectures_media//)


![](./motherload_all_lectures_media//)     


Solution: 00 01 10 11 since 4\-PAM has 4 in it :) $\textrm{log2}\left(4\right)=2$ therefor 2 bits represents it.


![](./motherload_all_lectures_media//)


Solution: ![](./motherload_all_lectures_media//)


b)  Solution:

```matlab
% Parameters
close all
clear
fs = 1000; % Sampling frequency
t = 0:1/fs:1;% Time vector (one period of the pulse shape)
g_t = cos(2*pi*t); % Pulse shape g(t)

% Amplitudes for 4-PAM
A = [-2, -1, 1, 2]; % Corresponding to binary symbols 00, 01, 10, 11
symbols = ["00", "01", "10", "11"]; % Binary symbols

% Plot the signal waveforms
figure;
for i = 1:length(A)
    plot(t+(i-1), A(i) * g_t, 'LineWidth', 1.5); % Scaled pulse shape
    hold on
    grid on;
end
title(['4-PAM Symbol: ', symbols(i), ' (Amplitude: ', num2str(A(i)), ')']);
    xlabel('Time (s)');
    ylabel('Amplitude');
    legend(symbols)
```

(c) Solution: Her er vi interesseret i C istedet for den nye besked. Hernæst er der tilføjet $\cos \left(2\pi \cdot 1\textrm{Hz}\cdot t\right)$ i for loopet for at tilføje carrieren. Ellers så er værdierne bare trykket ind i C arrayet.

```matlab
    % Parameters
close all
clear
fs = 1000; % Sampling frequency
t = 0:1/fs:1;% Time vector (one period of the pulse shape)
g_t = cos(2*pi*t); % Pulse shape g(t)

% Amplitudes for 4-PAM
A = [-2, -1, 1, 2]; % Corresponding to binary symbols 00, 01, 10, 11
symbols = ["00", "01", "10", "11"]; % Binary symbols
C = [-2, 1, 2, -1, 2, -2, 1];
symbolsC = string(C);
% Plot the signal waveforms
figure;
for i = 1:length(C)
    plot(t+(i-1), C(i) * g_t.*cos(2*pi*t), 'LineWidth', 1.5); % Scaled pulse shape
    hold on
    grid on;
end
% title(['4-PAM Symbol: ', symbols(i), ' (Amplitude: ', num2str(A(i)), ')']);
    xlabel('Time (s)');
    ylabel('Amplitude');
    % legend(symbols)
    legend(symbolsC)
```

![](./motherload_all_lectures_media//)

![](./motherload_all_lectures_media//)


Solution: Find svar arket bror mand.

```matlab
T = 1;
Eg = (4*pi*T+sin(4*pi*T))/(8*pi);
```

```matlabTextOutput
ans = 
                       0.5

```

 ![](./motherload_all_lectures_media//)


Solution:


Based on the maximum\-a\-posterior principle, the received demodulated signals would be: \[−1.20, −2.40, 1.49, 2.10\]→ \[01, 00, 10, 11\] (just find the closest symbol using the TRUE mapping \[−2, −1, 1, 2\]→ \[00, 01, 10, 11\]). Assuming that the sequence of true transmitted symbols was: \[00, 00, 11, 11\], the percentage of error was 50%.

