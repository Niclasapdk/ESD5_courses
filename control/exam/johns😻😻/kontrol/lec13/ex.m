x = [-1 0; 0 -2];
y = [1 1];

det([y; y*x])


%%
close all
clear

xdot = [7 -9; 6 -8];

y = [1 1];

O = [y; y*xdot];
t2 = inv(O)*[0;1];
t1 = xdot*t2;
T = [t1(1) t2(1); t1(2) t2(2)];
Ao = inv(T)*xdot*T;
Co = y*T;
Lo = [-8; -22];
L = T*Lo;
eig(xdot + L*y);


closedloop = [xdot [4;3]*[-2 2]; -L*y (xdot + L*y + [4;3]*[-2 2])];
eig(closedloop)