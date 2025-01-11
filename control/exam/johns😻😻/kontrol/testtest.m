clc
clear all
syms s x k
G(s) = 10/(s*(s+1)*(s+2));
limit(s*G,s,0);
Kv = 10;
GM = 10;%dB
collect(G,s);
D(s) = k*((1+10*s)/(1+26*s));
x = G(s)*D(s)
b = [10];
a = [1 3 2 0];
[z,p,K] = tf2zp(b,a);
G1 = tf([10],[1 3 2 0]);
% margin(G1)
grid on
K = solve(16.2==20*log10(x));