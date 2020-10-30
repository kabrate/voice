
import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
 
# 1. Get the file path to the included audio example
filepath = 'C:/Users/jing/Desktop/语音比赛/'
filename =filepath+'waveform.wav'
# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename,sr=None)
 #调整大小
plt.figure(figsize=(12, 6))
#振幅转化为分贝
D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)
#plt.subplot(1, 1, 1)
#标签
librosa.display.specshow(D, y_axis='linear')
#分贝颜色
plt.colorbar(format='%+2.0f dB')
plt.title('Linear-frequency power spectrogram')#线性频率功率谱图
plt.show()
