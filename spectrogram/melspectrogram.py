import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display

waveform, sr=librosa.core.load("C:/Users/jing/Desktop/语音比赛/waveform.wav",sr=None)
win_length = int(0.025 * sr)  # Window length 15ms, 25ms, 50ms, 100ms, 200ms 音频帧长度
hop_length = int(0.010 * sr)  # Window shift  10ms 音频帧间隔
n_fft = win_length
S = librosa.feature.melspectrogram(waveform, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=128)
S_DB = librosa.power_to_db(S, ref=np.max)
plt.figure(figsize=(12, 6));
librosa.display.specshow(S_DB, sr=sr, y_axis='linear');
plt.colorbar(format='%+2.0f dB');
plt.show();
#语谱图也叫时频谱图 横轴是时间 纵轴是频率  颜色表示幅度 声强 