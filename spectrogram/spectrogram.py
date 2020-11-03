
import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
 
# 1. Get the file path to the included audio example
filepath = 'C:/Users/jing/Desktop/语音比赛/'
filename =filepath+'LA_T_4451472.wav'

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename,sr=None)
# trim silent edges  减去静音片段
y, _ = librosa.effects.trim(y)
win_length = int(0.025 * sr)  # Window length 15ms, 25ms, 50ms, 100ms, 200ms 音频帧长度
hop_length = int(0.010 * sr)  # Window shift  10ms 音频帧间隔
n_fft = 512 #快速傅里叶变换的维度 音频帧中信号不足 补零处理
 #调整大小
plt.figure(figsize=(12, 6))
#振幅转化为分贝
D = librosa.amplitude_to_db(librosa.stft(y,n_fft=n_fft,hop_length=hop_length,win_length=win_length), ref=np.max)
#标签
librosa.display.specshow(D,sr=sr, hop_length =hop_length,x_axis='time', y_axis='linear')
#分贝颜色
plt.colorbar(format='%+2.0f dB')
plt.show()


