close all;
clear;
%A)
s = tf('s');
% phaselead = (s+1)/(s+3.62);
% GH = 5/(s*(s+1)) * phaselead;
% [r,k] = rlocus(GH);
% angles = 180/pi*atan2(imag(r),-real(r));

syms T
K = 1.0232929922807541309662751748199
Td = exp(-5*s);
G = (20/((s+2)*(s+10))) * Td;
sym = G/(1+G)*K; 
margin(G);
x = solve(0.2==20*log10(T),T);
vpa(x);
%% B)
close all;
clear;
s = tf('s');
syms T
Td = exp(-5*s);
G1 = (20/((s+2)*(s+10)));
% margin(G1);
K1 = solve(21.3==20*log10(T),T);
K2 = 11.614486138403427485697000798309;
sysfunc = K2*((G1*Td))/(1+(K2*G1));
step(sysfunc);