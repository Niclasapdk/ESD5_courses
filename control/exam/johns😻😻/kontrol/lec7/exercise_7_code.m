clear all %jeg ved ikke hvad det her bliver brugt til.
close
syms K s
s = tf('s');
G = (s^2+s+2)/(s*(s+5)*(s+6)*(s^2+2*s+1));
rlocus(G);
T = 1+G*K;
collect(T,s)
s5 = [1 54 K+30];
s4 = [13 K+71 2*K];

% -1*((1*2*K)-(13*(K+30))) kræver et minus foran her ikke ??
%%
clear all
close
syms K
s = tf('s');
G = 1/s^2;
H = (s+2)/(s+4);
K = G*H;
% rlocus(G*H);
hold on
sen = 1/(0.1*s + 1);
rlocus(sen*G*H);
sgrid