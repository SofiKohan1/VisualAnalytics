from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tempfile import mktemp
import numpy as np
import warnings
import IPython
import pandas as pd
warnings.filterwarnings("ignore")
import plotly.express as px
import pandas as pd



def read_mp3(filename, ch):
    mp3_audio = AudioSegment.from_file(filename, format="mp3") 
    wname = mktemp('.wav')  
    mp3_audio.export(wname, format="wav")  
    FS, data = wavfile.read(wname)  
    if data.ndim>1:
        data = data[:,ch] 
    #print('the sampeling frequncy is:',FS, 'Hz')
    return FS, data

from IPython.display import Audio

def spectograms(bird_species, test_audios, NFFT, noverlap ):
    FS, data = read_mp3(bird_species, ch=0)
    FS_, data_ = read_mp3(test_audios, ch=0)
    fig = plt.figure()
    fig, (ax1, ax2) = plt.subplots(ncols=2)
    fig.set_size_inches(50, 10)
    ax1.specgram(data, Fs=FS, NFFT=NFFT, noverlap=noverlap,vmin=-70, vmax=50, cmap='plasma')   
    ax1.set_ylabel('Frequency [Hz]')
    ax1.set_xlabel('Time [sec]')
    audio = Audio(filename=bird_species)
    display(audio)
    ax1.set_title('Bird Specie Spectrogram')
    
    print('The sampeling frequncy for the bird specie file is:',FS, 'Hz')
    ax2.specgram(data_, Fs=FS_, NFFT=NFFT, noverlap=noverlap, vmin=-70, vmax=50, cmap='plasma')   
    plt.ylabel('Frequency [Hz]')
    ax2.set_xlabel('Time [sec]')
    ax2.set_title('Test Audio Spectrogram')
    audio1 = Audio(filename=test_audios)
    display(audio1)
    print('The sampeling frequncy for the test file is:',FS_, 'Hz')
    plt.show()
    
    fig_plt = plt.figure()
    fig_plt, (ax3, ax4) = plt.subplots(ncols=2, figsize=(50,10))
    ax3.plot(data)
    ax4.plot(data_)
    ax3.set_title("Wave Form for Bird Specie audio file")
    ax3.set_xlabel("Time")
    ax4.set_title("Wave Form for test audio file")
    ax4.set_xlabel("Time")
    plt.show()
    


  