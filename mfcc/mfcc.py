
import scipy
import scipy.io
import scipy.signal 
from scipy.io import wavfile
from matplotlib import pyplot as plt 
import numpy as np 
amp = 2 * np.sqrt(2)
#采样率 帧长度#
rate,x = scipy.io.wavfile.read('C:/Users/jing/Desktop/语音比赛/quiteroom_echo0_11.wav')
f,t,z=scipy.signal.stft(x, fs =rate,window ='hann')

plt.pcolormesh(t,f,np.abs(z), vmin = 0, vmax = amp)
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

