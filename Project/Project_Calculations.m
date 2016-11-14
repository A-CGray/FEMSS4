% Alasdair Gray, FEMSS 4 Project Calculations

clear all, hold off, close all, clc
% Define beam parameters
L = 5; % Beam Length in m
b = 0.2; % Beam width in m
d = [0.2, 1]; % Beam depths in m
A = b*d;
w = [10, 100]*1000; % Beam UDL's in N/m
E = 200*10^9; % Steel elastic Modulus in Pa
nu = 0.3; % Steel Poisson's ratio
I = b*d.^3/12; % Section inertia in m^4
fs = (12+11*nu)/(10*(1+nu)); % Timoshenko form factor for recangular section
G = E/(2*(1+nu));
beam_size = {'thin', 'thick'};
% Calculate and plot shear force, bending moment , bending stress and deflection
x = linspace(0,L,100);
for beam = 1:length(w)
    SF(beam,:) = w(beam).*(L/2-x);
    M(beam,:) = w(beam)*x/2.*(L-x);
    v_euler(beam,:) = w(beam)*x/(24*E*I(beam)).*((2*L*x.^2) -x.^3 - L^3);
    v_timo(beam,:) = v_euler(beam,:) - w(beam)*x*fs/(2*A(beam)*G).*(L-x);
    %%
    vmax(beam, :) = 5*w(beam)*L^4/(384*E*I(beam))*[1, (1+((48*fs*E*I(beam))/(5*G*A(beam)*L^2)))];
    figure(2*beam-1), yyaxis left, plot(x, SF(beam,:)/10^3), ylabel('Shear Force (kN)', 'FontSize', 14)
    text(L/2, 0.5*min(SF(beam,:)/10^3),['Maximum Shear ', num2str(max(SF(beam,:)/10^3)), ' kN'], 'FontSize', 14,'HorizontalAlignment', 'center')
    yyaxis right, plot(x,M(beam,:)/10^3), ylabel('Bending Moment (kNm)', 'FontSize', 14), hold on
    plot([L/2, L], max(M(beam,:)/10^3)*[1,1], '-k')
    text(L/2, 1.05*max(M(beam,:)/10^3),['Maximum Bending Moment ', num2str(round(max(M(beam,:)))/10^3), ' kNm'], 'FontSize', 14,'HorizontalAlignment', 'center')
    xlabel('X (m)', 'FontSize', 14), grid on
    title([beam_size{beam}, ' Beam, Shear Force and Bending Moment'], 'FontSize', 16)
    savefig(['images\', beam_size{beam}, ' Beam, Shear Force and Bending Moment Diagram.fig'])
    print(['images\', beam_size{beam}, ' Beam, Shear Force and Bending Moment Diagram.png'], '-dpng')
    %
    figure(2*beam), yyaxis left, plot(x,v_euler(beam,:)*10^3, x, v_timo(beam,:)*10^3), hold on
    plot( [0, L/2], [-vmax(beam,1), -vmax(beam,1)]*10^3, 'k-')
    plot([0, L/2], [-vmax(beam,2), -vmax(beam,2)]*10^3, 'k-')
    ylabel('Displacement (mm)', 'FontSize', 14)
    legend('Euler', 'Timoshenko')
    text(L/2, -3/7*vmax(beam,1)*10^3, ['Max $\delta_{Euler} =$ ', num2str(vmax(beam,1)*10^3), ' mm'], 'FontSize', 14, 'Interpreter', 'latex','HorizontalAlignment', 'center')
    text(L/2, -4/7*vmax(beam,1)*10^3, ['Max $\delta_{Timoshenko} =$ ', num2str(vmax(beam,2)*10^3), ' mm'], 'FontSize', 14, 'Interpreter', 'latex','HorizontalAlignment', 'center')
    yyaxis right, plot(x,M(beam,:)*d(beam)/(2*10^6*I(beam))), ylabel('Bending Stress (MPa)', 'FontSize', 14)
    plot([L/2, L], max(M(beam,:)*d(beam)/(2*10^6*I(beam)))*[1,1],'-k')
    text(L/2, 0.8*max(M(beam,:)*d(beam)/(2*10^6*I(beam))), ['Max $\sigma =$ ', num2str(max(M(beam,:)*d(beam)/(2*10^6*I(beam)))), ' MPa'], 'FontSize', 14, 'Interpreter', 'latex','HorizontalAlignment', 'center')
    xlabel('X (m)', 'FontSize', 14), grid on
    title([beam_size{beam}, ' Beam, Theoretical Stress and Deflection'], 'FontSize', 16)
    savefig(['images\', beam_size{beam}, ' Beam, Theoretical Stress and Deflection.fig'])
    print(['images\', beam_size{beam}, ' Beam, Theoretical Stress and Deflection.png'], '-dpng')
end
% %% Compare with beam element results
% element_type = {'B21', 'B22', 'B23'};
% elements = [2, 10];
% leg = {'theoretical';'theoretical'};
% sym = {'o', '*', '+'};
% for beam = 1:length(w)
%     for type = 1:length(element_type)
%         figure, plot(x,M(beam,:)*d(beam)/(2*10^6*I(beam)), 'LineWidth', 2), hold on
%         xlabel('X (m)', 'FontSize', 14), grid on
%         ylabel('Bending Stress (MPa)', 'FontSize', 14)
%         title([beam_size{beam}, ' Beam ', element_type{type}, ' Stress Comparison '], 'FontSize', 14);
%         for n = 1:length(elements)
%             filename = ['beam_models\', element_type{type}, '_', beam_size{beam}, '_', num2str(elements(n)), 'EL\S11.csv'];
%             S11 = csvread(filename);
%             max_stress(beam,(type-1)*length(elements)+n) = max(abs(S11(:,2)));
%             leg{beam, (type-1)*length(elements)+n+1} = [ element_type{type}, ' x ', num2str(elements(n))];
%             plot(S11(:,1), S11(:,2)/10^6, '--o', 'MarkerSize', 10, 'LineWidth', 2)
%             text(L/2, n*0.1*max(M(beam,:)*d(beam)/(2*10^6*I(beam))), ['Max $\sigma_{', num2str(elements(n)), 'EL} =$ ', num2str(max_stress(beam,(type-1)*length(elements)+n)/10^6), ' MPa'], 'FontSize', 14, 'Interpreter', 'latex','HorizontalAlignment', 'center')
%         end
%         legend('theoretical', '2 Elements', '10 Elements', 'Location', 'best')
%         savefig(['images\', beam_size{beam}, ' Beam ', element_type{type}, ' Stress Comparison '])
%         print(['images\', beam_size{beam}, ' Beam ', element_type{type}, ' Stress Comparison '], '-dpng')
%         %%
%         figure, plot(x,v_euler(beam,:)*10^3, '-k', x, v_timo(beam,:)*10^3, '--k', 'LineWidth', 2), hold on
%         xlabel('X (m)', 'FontSize', 14), grid on
%         ylabel('Vertical Displacement (mm)', 'FontSize', 14)
%         title([beam_size{beam}, ' Beam ', element_type{type}, ' Deflection Comparison '], 'FontSize', 14);
%         for n = 1:length(elements)
%             filename = ['beam_models\', element_type{type}, '_', beam_size{beam}, '_', num2str(elements(n)), 'EL\U2.csv'];
%             U2 = csvread(filename);
%             max_def(beam,(type-1)*length(elements)+n) = max(abs(U2(:,2)));
%             plot(U2(:,1), U2(:,2)*10^3, '--o', 'MarkerSize', 10, 'LineWidth', 2)
%             text(L/2, n*-0.1*vmax(beam,1)*10^3, ['Max $\delta_{', num2str(elements(n)), 'EL} =$ ', num2str(max_def(beam,(type-1)*length(elements)+n)*10^3), ' mm'], 'FontSize', 14, 'Interpreter', 'latex','HorizontalAlignment', 'center')
%         end
%         legend('Euler', 'Timoshenko', '2 Elements', '10 Elements', 'Location', 'SouthEast')
%         savefig(['images\', beam_size{beam}, ' Beam ', element_type{type}, ' Deflection Comparison '])
%         print(['images\', beam_size{beam}, ' Beam ', element_type{type}, ' Deflection Comparison '], '-dpng')
%     end
% end
close all
% Create plots for 2D models
elements = {'CPS4', 'CPS4I', 'CPS4R', 'CPS8'};
sym = {'o', '*', '+', 'X'};
y = linspace(-d(2)/2, d(2)/2, 100);
tau_L_5 = 1.5/A(2)*w(2).*(L/2-L/5)*(1-(y/(d(2)/2)).^2);

for n = 1:length(elements)
    filename = ['solid_models\', elements{n}];
    L_5_S11 = csvread([filename, '\L-5-S11.csv']);
    L_5_S12 = csvread([filename, '\L-5-S12.csv']);
    tau_ave(n) = abs(mean(L_5_S12(:,2)))/10^6;
    tau_max(n) = max(abs(L_5_S12(:,2)))/10^6;
    tau_ratio(n) = tau_max(n)/tau_ave(n);
    BOTTOM_S11 = csvread([filename, '\BOTTOM-S11.csv']);
    BOTTOM_U2 = csvread([filename, '\BOTTOM-U2.csv']);
    figure(1), plot(BOTTOM_U2(:,1), BOTTOM_U2(:,2)*10^3, ['-.', sym{n}], 'LineWidth', 2, 'MarkerSize', 10), hold on
    figure(2), plot(BOTTOM_S11(:,1), BOTTOM_S11(:,2)/10^6, ['-.', sym{n}], 'LineWidth', 2, 'MarkerSize', 10), hold on
    figure(3), plot(L_5_S11(:,2)/10^6, L_5_S11(:,1)-d(2)/2, ['-.', sym{n}], 'LineWidth', 2, 'MarkerSize', 10), hold on
    figure(4), plot(-L_5_S12(:,2)/10^6, L_5_S12(:,1)-d(2)/2, ['-.', sym{n}], 'LineWidth', 2, 'MarkerSize', 10), hold on
    figure(5), plot(L_5_S11(:,2)/10^6 - interp1([-d(2)/2, d(2)/2],(w(2)*L/10.*(L-L/5))*d(2)/2/I(2)/10^6*[1, -1], L_5_S11(:,1)-d(2)/2), L_5_S11(:,1)-d(2)/2, ['-.', sym{n}], 'LineWidth', 2, 'MarkerSize', 10), hold on
    figure(6), plot(BOTTOM_U2(:,1), BOTTOM_U2(:,2)*10^3 - interp1(x, v_timo(2,:)*10^3, BOTTOM_U2(:,1)), ['-.', sym{n}], 'LineWidth', 2, 'MarkerSize', 10), hold on
end
figure(1), plot(x,v_euler(2,:)*10^3, '-k', x, v_timo(2,:)*10^3, '--k', 'LineWidth', 2)
xlabel('X (m)', 'FontSize', 14), grid on
ylabel('Vertical Displacement (mm)', 'FontSize', 14)
title('Plane Stress Element, Displacement Comparison', 'FontSize', 14)
legend(elements{:}, 'Euler', 'Timoshenko', 'Location', 'best')
savefig('images\Plane Stress Element, Displacement Comparison.fig')
print('images\Plane Stress Element, Displacement Comparison.png', '-dpng')

figure(2), plot(x,M(2,:)*d(2)/(2*10^6*I(2)),'k', 'LineWidth', 2)
xlabel('X (m)', 'FontSize', 14), grid on
ylabel('Bending Stress (MPa)', 'FontSize', 14)
title('Plane Stress Element, Bending Stress Comparison', 'FontSize', 14)
legend(elements{:}, 'Theoretical', 'Location', 'best')
savefig('images\Plane Stress Element, Bending Stress Comparison.fig')
print('images\Plane Stress Element, Bending Stress Comparison.png', '-dpng')

figure(3), plot((w(2)*L/10.*(L-L/5))*d(2)/2/I(2)/10^6*[1, -1], [-d(2)/2, d(2)/2],'k', 'LineWidth', 2)
xlabel('$\sigma_{xx}$ (MPa)', 'FontSize', 16, 'Interpreter', 'latex'), grid on
ylabel('Y (m)', 'FontSize', 14)
title('Plane Stress Element, Section Stress @ x = $\frac{L}{5}$', 'FontSize', 14, 'Interpreter', 'latex')
legend(elements{:}, 'Theoretical', 'Location', 'best')
savefig('images\Plane Stress Element, Section Stress Comparison.fig')
print('images\Plane Stress Element, Section Stress Comparison.png', '-dpng')

figure(4), plot(tau_L_5/10^6, y,'k', 'LineWidth', 2)
xlabel('$\tau_{xy}$ (MPa)', 'FontSize', 16, 'Interpreter', 'latex'), grid on
ylabel('Y (m)', 'FontSize', 14)
title('Plane Stress Element, Section Shear @ x = $\frac{L}{5}$', 'FontSize', 14, 'Interpreter', 'latex')
legend(elements{:}, 'Theoretical', 'Location', 'best')
savefig('images\Plane Stress Element, Section Shear Comparison.fig')
print('images\Plane Stress Element, Section Shear Comparison.png', '-dpng')

figure(5)
xlabel('$\sigma_{xx}$ Error (MPa)', 'FontSize', 16, 'Interpreter', 'latex'), grid on
ylabel('Y (m)', 'FontSize', 14)
title('Plane Stress Element, Section Stress Error @ x = $\frac{L}{5}$', 'FontSize', 14, 'Interpreter', 'latex')
legend(elements{:}, 'Location', 'best')
savefig('images\Plane Stress Element, Section Stress Error.fig')
print('images\Plane Stress Element, Section Stress Error.png', '-dpng')

figure(6)
xlabel('X (m)', 'FontSize', 14), grid on
ylabel('Vertical Displacement Error (mm)', 'FontSize', 14)
title('Plane Stress Element, Displacement Error', 'FontSize', 14)
legend(elements{:}, 'Location', 'best')
savefig('images\Plane Stress Element, Displacement Error.fig')
print('images\Plane Stress Element, Displacement Error.png', '-dpng')