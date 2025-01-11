% 2 design a lead controller
close all
clear
s = tf('s');
% syms s

% PM > 45deg wc (cross over frequency) unity feed back

G = 1/(s*(s+1));
% sisotool(G) %brug til at finde lead controller parameter for at opnå PM
% og Wc

D = k*((s+a)/(s+b));
D2 = 2.03*((1+s)/(1+0.1*s)); %from sisotool
T = G*D2; %open loop

Tc = T/(1+T); %close loop

Tdt = c2d(Tc,(1/10),'tustin'); %sample rate 10Hz konverting til digital controller.
Tdz = c2d(Tc,(1/10),'ZOH');
step(Tc,'r-',Tdz,'-');