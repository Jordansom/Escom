% Asumiendo que el archivo de audio es 'audio.wav'
[signal, Fs] = audioread('audio.wav');

% Transformada de Fourier
fftSignal = fft(signal);

% Transformada inversa de Fourier
ifftSignal = ifft(fftSignal);

% Filtro pasa altas
% Define el orden del filtro
order = 5;
% Define la frecuencia de corte como 85 Hz
cutoff =  300/ (Fs/2); 
[b,a] = butter(order, cutoff, 'high');
highPassSignal = filter(b, a, signal);

% Filtro pasa bajas
% Define la frecuencia de corte como 900 Hz
cutoff = 900 / (Fs/2);
[b,a] = butter(order, cutoff, 'low');
lowPassSignal = filter(b, a, signal);

% Filtro pasa banda
% Define las frecuencias de corte como 85 Hz y 180 Hz
band = [300 900] / (Fs/2);
[b,a] = butter(order, band, 'bandpass');
bandPassSignal = filter(b, a, signal);

% Graficando las señales
t = (0:length(signal)-1)/Fs;

subplot(5,1,1);
plot(t,signal);
title('Señal Original');

subplot(5,1,2);
plot(t,ifftSignal);
title('Transformada inversa de Fourier');

subplot(5,1,3);
plot(t,highPassSignal);
title('Filtro pasa altas');

subplot(5,1,4);
plot(t,lowPassSignal);
title('Filtro pasa bajas');

subplot(5,1,5);
plot(t,bandPassSignal);
title('Filtro pasa banda');

% Guardando los archivos de audio
audiowrite('TransformadaInversa.wav', ifftSignal, Fs);
audiowrite('FiltroPasaAltas.wav', highPassSignal, Fs);
audiowrite('FiltroPasaBajas.wav', lowPassSignal, Fs);
audiowrite('FiltroPasaBanda.wav', bandPassSignal, Fs);

