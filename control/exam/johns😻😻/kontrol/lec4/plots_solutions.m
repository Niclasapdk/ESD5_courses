close all
clear
s = tf('s');
G = 10/(s*((s+1)*(s+2)));

% margin(G)%vælg 2 rad/s som ny wn her er phase = -198;
newphase = 45+20; %20 istedet for 13 for at give ekstra.
% gm 4.44 dB
newgain = 10 + 4.4;
D = (s+0.2)/(s+20);
% margin(D*G);
% step((D*G)/(1+(D*G)));
% bode(D)

% find kv ved at sætte s til 0;
% og brug lim funktion giver 0.05;
Kv = (0+0.2)/(0+20) * 10/(((0+1)*(0+2))) %s bliver sat til 0 og formlen lim s*(D*G) bruges det første forsvinder med et s i G.
%Brug en lag for at give lowfrequency gain!

%Sæt kvtotal ind altså 10 og løs for forholdet mellem zero og pole zero er
%større og vælges til 0.04 herfra får man pole i 0.0002 og samtidig væk fra
%de andre pol og nulpunkt fra lead.

lag = (s+0.04)/(s+0.0002);
%margin(lag*D*G);
open_loop = lag*D*G;
% step(open_loop/(1+open_loop))
%% 
close all
clear
s =tf('s')

G = 1/(s*(0.1*s+1)*(0.2*s+1));
margin(G)