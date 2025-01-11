close all
clear

syms Kp
s = tf('s');
expr = 1/(10*s+1);
expr1 = 1/(0.1*s+1);
G = expr*expr*expr1;
margin(G)
%%
close all
clear
Kp = 10; % egne udregenelser stememr selvfølgelig ikke overens
% s = tf('s');
syms s
expr = 1/(10*s+1);
expr1 = 1/(0.1*s+1);
G = Kp*expr*expr*expr1;
D = Kp*expr*expr;
T = D/(1+G); %uden error signalet altså R -> Y
% limit(T,s,0); udregning af limit for overføringsfunktionen.

% step(T); %for Propertional controller istedet.
Kp1 = 3*((s+0.1)/s);
T1 = expr/(1+Kp1*expr*expr*expr1); %med error altså W -> Y
% step(T1);
