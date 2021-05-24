import librosa
from spafe.utils import vis
from spafe.features.lfcc import lfcc
import matplotlib
import matplotlib.pyplot as plt
def visualize_features(feats, ylabel, xlabel, cmap='viridis'):
    """
    visualize a matrix including the features coefficients. Each row corresponds
    to a frame.

    Args:
        feats  (array) : 2d array including the the features coefficients.
        ylabel   (str) : y-axis label.
        xlabel   (str) : x-axis label.
        cmap     (str) : matplotlib colormap to use.
    """
    plt.imshow(feats.T,
               origin='lower',
               aspect='auto',
               cmap=cmap,
               interpolation='nearest')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()
    #plt.close()
    plt.savefig('lfcc.png')
    plt.close()
def spectogram(sig, fs):
    """
    visualize a the spectogram of the given mono signal.

    Args:
        sig (array) : a mono audio signal (Nx1) from which to compute features.
        fs    (int) : the sampling frequency of the signal we are working with.
    """
    plt.specgram(sig, NFFT=1024, Fs=fs)
    plt.ylabel("Frequency (kHz)")
    plt.xlabel("Time (s)")
    plt.show()
    plt.close()
# init input vars
num_ceps = 60
low_freq = 0
high_freq = 8000
nfilts = 60
nfft = 2205
dct_type = 2,
use_energy = False,
lifter = 5
normalize = False
    
# read wav 
#fs, sig = scipy.io.wavfile.read("test.wav")
sig, fs = librosa.load("E:\\data\\poco4\\wolf\\false\\0203_2-2-1_wolf.WAV")
# compute features
lfccs = lfcc(sig=sig,
             fs=fs,
             num_ceps=num_ceps,
             nfilts=nfilts,
             nfft=nfft,
             low_freq=low_freq,
             high_freq=high_freq,
             dct_type=dct_type,
             use_energy=use_energy,
             lifter=lifter,
             normalize=normalize)

# visualize spectogram
#spectogram(sig, fs)
# visualize features
visualize_features(lfccs, 'LFCC Index', 'Frame Index')

