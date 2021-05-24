import scipy
from spafe.utils import vis
from spafe.features.mfcc import mfcc, imfcc
import librosa
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
    plt.close()
# init input vars
num_ceps = 13
low_freq = 0
high_freq = 8000
nfilts = 24
nfft = 512
dct_type = 2,
use_energy = False,
lifter = 5
normalize = False
    
# read wav 
#fs, sig = scipy.io.wavfile.read("test.wav")
sig, fs = librosa.load("C:/Users/jing/source/repos/KWS/KWS/input/speech_commands/train/marvin/0ac15fe9_nohash_0.wav",sr=16000)
# compute features
mfccs = mfcc(sig=sig,
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
#vis.spectogram(sig, fs)
# visualize features
visualize_features(mfccs, 'MFCC Index', 'Frame Index')




# compute features
imfccs = imfcc(sig=sig,
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

# visualize features
vis.visualize_features(imfccs, 'IMFCC Index', 'Frame Index')
