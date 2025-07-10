% Asumiendo que el archivo de audio es 'audio.wav'
[x, Fs] = audioread('Grabación.wav');

% Transformada de Fourier
fftx = fft(x);

% Define el orden del filtro
orden = 5;

cutoff =  300/ (Fs/2); %frecuencias de corte  
[b,a] = butter(orden, cutoff, 'high');% Filtro pasa altas
highPassx = filter(b, a, x);

cutoff = 800 / (Fs/2);%frecuencias de corte
[b,a] = butter(orden, cutoff, 'low');% Filtro pasa bajas
lowPassx = filter(b, a, x);


band = [300 800] / (Fs/2);%frecuencias de corte 
[b,a] = butter(orden, band, 'bandpass');% Filtro pasa banda
bandPassx = filter(b, a, x);

t = (0:length(x)-1)/Fs;

% Transformada inversa de Fourier
ifftx = ifft(bandPassx);

figure(1)
plot(t,ifftx);
title('Señal Original');

figure(2)
plot(t,fftx);
title('Transformada inversa de Fourier');

figure(3)
plot(t,highPassx);
title('Filtro pasa altas');

figure(4)
plot(t,lowPassx);
title('Filtro pasa bajas');

figure(5)
plot(t,bandPassx);
title('Filtro pasa banda');
%sonidos
%sound(ifftx,Fs)%Transformada Inversa para sacar el audio original original

%sound(highPassx,Fs)%Filtro Pasa Altas

%sound(lowPassx,Fs)%Filtro Pasa Bajas

%sound(bandPassx,Fs)%Filtro Pasa Banda


