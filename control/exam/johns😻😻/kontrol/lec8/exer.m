%% Exercise 1
close all
clear
syms K
s = tf('s');
G = (((1-0.15*s)/(1+0.15*s))/(s+1));
rlocus(G); % Ved at se på rootlocus der kan man få et stabilt system for K =< 7.

%% Exercise 2
close all
clear
s = tf('s');
G = (s^2+2*s+4)/(s*(s+4)*(s+6)*(s^2+1.4*s+1));
rlocus(G); % Så K mindre end 15.6, K større end 70, K mindre end 165 disse områder giver stabilitet.
%% Exercise 3
close all
clear
s1 = -0.5*3+j*3*sqrt(1-0.5^2); % Pole location 1 and location 2 if it is - before 2.598
s = tf('s');
x1 = rad2deg(angle(s1));
x2 = rad2deg(angle(1+s1));
x3 = -1*(x1+x2); % needed phase for 180 is 40.893;
needP = 40.893;

pc = (-1*imag(s1)/tan(needP)) + real(s1);
zc = (-1*imag(s1)/tan(2*needP)) + real(s1);
G = 10/(s*(s+1));
D = (s+zc)/(s+(pc)); %s+(factor*z) for at finde en pol som passer med dampning
rlocus(G*D)

% damp((D*G)/(1+(D*G)));
% damp(1/(s^2 + 3*s + 9));

%step((D*G)/(1+(D*G))); %step response :)))))😻🥵🥵
% (D*G)/(1+(D*G));


%% 
close all
clear;

s = tf('s');
D = (s+2)/(s+10);
G = 1/(s*(s+1));
% rlocus(D*G)
L = ((s+5.4)/(s+20))*(1/(s*(s+1)));
rlocus(L);