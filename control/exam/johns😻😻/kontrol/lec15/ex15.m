% K = place((A+B*F+L*C)',F',[pole1,pole2])';
%husk de transponerede matricer er for observer istedet.
%Mtilde = -place((A+B*F +L*C)',(-F)',[-3,-4])'
%% Ex 1
%1)
close all
clear
A = [7 -9; 6 -8];
B = [4;3];
C = [1 1];
F = [-2 2];
L = [-5; -3];

A1 = [2 -3; 4 -5];
B1 = [2;3];
C1 = [-3 2];
F1 = [22 -16];
L1 = [-122;-192];

% sys1 = ss([A1 B1*F1; -L1*C1 A1+(B1*F1)+(L1*C1)],[B1;B1],[C1 0 0; 0 0 0 0; 0 0 0 0; 0 0 0 0],0);
% sys2 = ss(A1,B1,C1,0);
% bodeplot(sys1(1));

sys = ss([A B*F; -L*C A+(B*F)+(L*C)],[B;B], [C 0 0; 0 0 0 0; 0 0 0 0; 0 0 0 0], 0);
% bodeplot(sys(1)/4);
hold on
%2)

Mtilde = place((A+(B*F)+(L*C))',F',[-1.4 -4])';


%3)
Acl = [A B*F; -L*C A+(B*F)+(L*C)];
Bcl = [B;Mtilde];
Ccl = [C 0 0];

N = -inv((Ccl*inv(Acl)*Bcl));

%4)
M = Mtilde*N;

%5)
B1 = [B*N; M];
sys1 = ss([A B*F; -L*C A+(B*F)+(L*C)],B1, [C 0 0], 0)
% bodeplot(sys1(1))
step(sys(1)/4);
hold on
step(sys1(1))
legend
%% Ex 2
%1)
close all
clear
A = [7 -9; 6 -8];
B = [4;3];
C = [1 1];
F = [-2 2];
L = [-5; -3];


Fopt = -lqr(A,B,1000*C'*C,1);

eig(A + B*Fopt); %Større rho giver poler der rykke mod venstre deraf giver større styresignal for et hurtigere system og modsat.
%2) Optimal kontrol vil placere poler i det venstre halvplan for
%nulpunkterne i højre halvplans placering. Giver en allpass karakteristik.

sys1 = ss(A,B,C,0);
zero(sys1);
%3)

s = tf('s');

sys2 = C*inv(s*eye(2) - (A + (B*Fopt)))*B;
% step(sys2)

%Qualative relationship ved at gøre rho større så får man en hurtigere rise time for sit system. 