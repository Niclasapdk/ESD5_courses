%system
s = tf('s');
G = 10/((s+1)*(s+2)*s) 


%lead_controller
K = 25
center = 3
alpha = 10

a = center/alpha
b = center * alpha
D_lead = K*(s+a)/(s+b) 


d = 0.0001
c = 20*d
D_lag = (s+c)/(s+d)

step(D_lead)
% step(4/(s^2+2*s+10))