import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display

waveform, sr=librosa.core.load("C:/Users/jing/Desktop/语音比赛/waveform.wav",sr=None)
win_length = int(0.025 * sr)  # Window length 15ms, 25ms, 50ms, 100ms, 200ms
hop_length = int(0.010 * sr)  # Window shift  10ms
n_fft = win_length
S = librosa.feature.melspectrogram(waveform, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=128)
S_DB = librosa.power_to_db(S, ref=np.max)
plt.figure(figsize=(15, 6));
librosa.display.specshow(S_DB, sr=sr, hop_length=512, x_axis='time', y_axis='mel');
plt.colorbar(format='%+2.0f dB');
plt.show();