% Problem antenna
lam = 3e8/5e9;
num2sip(lam);
syms d
c = 3e8;
f = 5e9;

%a)
fspl_distance = solve(35 == 20*log10(d)+20*log10(f) + 20*log10((4*pi)/c) - mag2db(1.63) - mag2db(1.63),d);
vpa(fspl_distance) % det er svaret!
sqrt(10^2+50^2) %pythagoras :) a^2+b^2=c^2

%b) Placer rf isolerended materiale imellem antennerne, forskellige
%polarizering mellem antennerne, placer dem oven på i hinanden så grundet
%ubdrebedelse af en dipol,

%c) Nej fordi med et reflekterende materiale så forsvinder der mindre af
%signalerne og deraf mindre isolation i mellem antennerne.

%% problem 4 :D
syms t
x = 2 * solve(1/2 == cos(2*t)^2,t);
rad2deg(x);

%% problem 11
% a) A to B 4 pakker
% b) B to A 3 pakker (B skal sende en ACK tilbage når den modtager en pakke
%.

%c) 2 pakker
%d) 1 pakke (luk comm)

%% problem 13
5*8;
40/5;

total_bytes = (20+8+5); %ellers se 2015 svar!