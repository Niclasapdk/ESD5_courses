%% ex1
close all
clear
%a)
b = [317 951 951 317];
a = [10000 -14590 9104 -1978];
sys = tf(b,a);
[b,a] = eqtflength(b,a);
[z,p,k] = tf2zp(b,a);
zplane(b,a)
text(real(z)+0.1,imag(z),"Zero")
text(real(p)+0.1,imag(p),"Pole")
%% 
%b)
close all
clear
w = linspace(0,pi,100);%😻🥵🥵😻
z = exp(j*w);
for i=1:length(w)
    H(i) = 0.0317*((1+3*z(i).^-1+3*z(i).^-2+z(i).^-3)/(1-1.4590*z(i).^-1+0.9104*z(i).^-2-0.1978*z(i).^-3));
    Ha(i) = abs(H(i));
end
plot(w,Ha)

% 20*log10(0.231835908196271) %
%c)

%% 
close all
clear
%d)
w = linspace(0,pi,316);
z = exp(j*w);
for i=1:length(w)
    H(i) = 0.0317*((1+3*z(i).^-1+3*z(i).^-2+z(i).^-3)/(1-1.4590*z(i).^-1+0.9104*z(i).^-2-0.1978*z(i).^-3));
    Ha(i) = angle(H(i));
end

plot(w,Ha);
%%😻🙏😻

%%
close all
clear