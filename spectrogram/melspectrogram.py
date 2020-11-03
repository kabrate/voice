import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
#Mel Spectrogram, is, rather surprisingly, a Spectrogram with the Mel Scale as its y axis.
waveform, sr=librosa.core.load("C:/Users/jing/Desktop/语音比赛/LA_T_4451472.wav",sr=None)
waveform, _ = librosa.effects.trim(waveform)
win_length = int(0.025 * sr)  # Window length 15ms, 25ms, 50ms, 100ms, 200ms 音频帧长度
hop_length = int(0.010 * sr)  # Window shift  10ms 音频帧间隔
n_fft = 512
S = librosa.feature.melspectrogram(waveform, sr=sr, n_fft=n_fft, hop_length=hop_length,win_length=win_length, n_mels=128)
S_DB = librosa.power_to_db(S, ref=np.max)
plt.figure(figsize=(12, 6));
librosa.display.specshow(S_DB,sr=sr,hop_length=hop_length,x_axis='time', y_axis='mel');
plt.colorbar(format='%+2.0f dB');
plt.show();
#语谱图也叫时频谱图 横轴是时间 纵轴是频率  颜色表示幅度 声强 