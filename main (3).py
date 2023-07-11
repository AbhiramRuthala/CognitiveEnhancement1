import time
from pylsl import StreamInlet, resolve_stream
from playsound import playsound
#Not sure what to import to use playsound. Playsound is imported, but is unused. If anyone knows how to fix this, please let me know.

streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])

#Define your threshold numerals
threshold_high = 0.5
threshold_low = 0.3

#This is the main loop
while True:
  #EEG data (Muse headband is the EEG)
  sample, timestamp = inlet.pull_sample();
  eeg_value = sample [0]
#Check attention level
if eeg_value > threshold_high:
  print("High attention")
  #Play a sound if you want to. You can remove the hastag and the command would run with the code.
  playsound('sound1.wav')

elif eeg_value < threshold_low:
  print("Low attention!")
  #Play a sound if you want to. You can remove the hastag and the command would run with the code.
  playsound('sound2.wav')

#Wait for a short interval before the next reading.
time.sleep(0.1)
