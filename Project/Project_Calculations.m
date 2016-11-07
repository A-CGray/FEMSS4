%% Alasdair Gray, FEMSS 4 Project Calculations
%
clear all, hold off, close all, clc
%% Define beam parameters
L = 5; % Beam Length in m
b = 0.2; % Beam width in m
d = [0.2, 1]; % Beam depths in m
A = b*d;
w = [10, 100]*1000; % Beam UDL's in N/m
E = 200*10^9; % Steel elastic Modulus in Pa
nu = 0.3; % Steel Poisson's ratio
I = b*d.^3/12; % Section inertia in m^4
fs = 6/5; % Timoshenko form factor for recangular section
G = E/(2*(1+nu));
beam_size = {'thin', 'thick'};
%% Calculate and plot shear force and bending moment distributions
x = linspace(0,L,100);
for beam = 1:length(w)
    SF(beam,:) = w(beam).*(L/2-x);
    M(beam,:) = w(beam)*x/2.*(L-x);
    vmax(beam, :) = 5*w(beam)*L^4/(384*E*I(beam))*[1, (1+((48*fs*E*I(beam))/(5*G*A(beam)*L^2)))];
    figure(beam), yyaxis left, plot(x, SF(beam,:)/10^3), ylabel('Shear Force (kN)', 'FontSize', 14)
    yyaxis right, plot(x,M(beam,:)/10^3), ylabel('Bending Moment (kNm)', 'FontSize', 14)
    xlabel('X (m)', 'FontSize', 14), grid on
    title([beam_size{beam}, ' Beam, Shear Force and Bending Moment Diagram'], 'FontSize', 16)
    savefig(['images\', beam_size{beam}, ' Beam, Shear Force and Bending Moment Diagram.fig'])
    print(['images\', beam_size{beam}, ' Beam, Shear Force and Bending Moment Diagram.png'], '-dpng')
end
%% Compare with beam element results
element_type = {'B21', 'B22', 'B23'};
elements = [2, 10];
leg = {'theoretical';'theoretical'};
sym = {'o', '*', '+'};
for beam = 1:length(w)
    for type = 1:length(element_type)
        figure, plot(x,M(beam,:)*d(beam)/(2*10^6*I(beam)), 'LineWidth', 2), hold on
        xlabel('X (m)', 'FontSize', 14), grid on
        ylabel('Bending Stress (MPa)', 'FontSize', 14)
        title([beam_size{beam}, ' Beam', element_type{type}, ' Element Comparison '], 'FontSize', 14);
        for n = 1:length(elements)
            filename = ['beam_models\', element_type{type}, '_', beam_size{beam}, '_', num2str(elements(n)), 'EL\S11.csv'];
            S11 = csvread(filename);
            leg{beam, (type-1)*length(elements)+n+1} = [ element_type{type}, ' x ', num2str(elements(n))];
            plot(S11(:,1), S11(:,2)/10^6, '--o', 'MarkerSize', 10, 'LineWidth', 2)
        end
        legend('theoretical', '2 Elements', '10 Elements')
        savefig(['images\', beam_size{beam}, ' Beam', element_type{type}, ' Element Comparison '])
        print(['images\', beam_size{beam}, ' Beam', element_type{type}, ' Element Comparison '], '-dpng')
    end
end