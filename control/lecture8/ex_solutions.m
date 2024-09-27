%% ex 1
clear all
close

K = 1;
s = tf('s');
pade = (1-0.15*s)/(1+0.15*s);
G = K*(pade/(s+1));
rlocus(G);
%% ex2
clear all
close

K = 1;
s = tf('s')
G = (s^2+2*s+4)/(s*(s+4)*(s+6)*(s^2+1.4*s+1));
rlocus(G)
%% ex3
clear all
close
figure;
K = 1;
s = tf('s')
G = 10/(s*(s+1));
D = (s+3)/(s+(3.1*3)); %s+(factor*z) for at finde en pol som passer med dampning
% rlocus(G*D);
% hold on;
% sgrid(0.5,3);
% hold on;
% sgrid;
step((D*G)/(1+(D*G))); %step response :)))))😻🥵🥵