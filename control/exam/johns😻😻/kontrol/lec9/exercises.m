close all
clear

syms s

h11 = (-10)/(1+100*s);
h12 = 3/((1+100*s)*(1+8*s));
h21 = (-11)/(1+200*s);
h22 = (10)/(1+100*s);

P(s) = [h11 h12; h21 h22];
R = P(0).*inv(P(0)).';
vpa(R,2);

x = inv(P(0)).';

Q(s) = inv(P(0))*P(s);

%% 
close all
clear

s = tf('s');
% syms s

h11 = (-10)/(1+100*s);
h12 = 3/((1+100*s)*(1+8*s));
h21 = (-11)/(1+200*s);
h22 = (10)/(1+100*s);

Q = (h21*h12)/(h11*h22);
k = -0.0062362*((1+27*s)/s);

sisotool((1-Q)*h11);
% margin(-0.6*(1-Q)*h11)
% hold on
% margin(k*(1-Q)*h11)
% pole((1-Q)*h11)
% zero((1-Q)*h11)
% margin(k*(1-Q)*h22)