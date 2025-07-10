n = 0:10;
n2 = 0:12;
x = 1*square(2*pi*.125*n, 50);
grap2 = 1*square(2*pi*.125*n2, 50);
n1 = length(x);
n2 = length(grap2);

% Obtener el reflejo de h(n)
reflectedgrap2 = fliplr(grap2);
N = n2 - n1;
signalD = padarray(reflectedgrap2, [0, N], 0, 'pre');
x = [x zeros(1, n2 - n1)];
nmax = length(signalD);
signalmov = x;

correlation = zeros(1, length(grap2)-1);

for i = 1:nmax
    diferencia = length(signalD) - length(signalmov);
    signalmovf = padarray(signalmov, [0, diferencia], 0, 'post');
    result = signalmovf .* signalD;
    if(length(correlation)<length(result))
       diferencia = length(result) - length(correlation);
       correlationl = padarray(correlation, [0, diferencia], 0, 'post'); 
    end
    correlationl = correlationl+result;
    signalD = padarray(signalmov, [0, i], 0, 'pre');
end

% Mostrar el resultado de la suma acumulativa
disp('Arreglo de suma acumulativa:');
disp(correlationl);

% Calcular los desplazamientos para la gráfica
%xs=xcorr(x,grap2,'normalized');
%hold('on');
%stem( xs, 'cya');
%stem( grap2, 'magenta');
%stem( reflectedgrap2, 'red');
%stem(shifts, correlation, 'filled');
%xlabel('Desplazamiento');
%ylabel('Correlación');
%title('Correlación Cruzada');
%hold('off');







