https://gist.github.com/mabdrabo/8678538

import pyaudio
import wave
import audioop

# Set the desired audio settings
sample_rate = 44100
chunk_size = 1024
silence_threshold = 1000  # Adjust this threshold to detect silence

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the audio stream
stream = audio.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk_size)

print("Recording started...")

frames = []  # Array to store audio frames
recording = False  # Flag to indicate recording state

# Recording loop
while True:
    data = stream.read(chunk_size)
    
    # Check if the recorded audio is silent
    if not recording and audioop.rms(data, 2) >= silence_threshold:
        print("Recording started.")
        recording = True
    
    if recording:
        frames.append(data)
        
        # Check if the recorded audio falls below the silence threshold
        if audioop.rms(data, 2) < silence_threshold:
            print("Recording stopped.")
            break

print("Recording completed.")

# Stop and close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a file (e.g., WAV format)
output_file = wave.open("recorded_audio.wav", "wb")
output_file.setnchannels(1)
output_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
output_file.setframerate(sample_rate)
output_file.writeframes(b"".join(frames))
output_file.close()




import pyaudio
import wave
 
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,input_device_index=1
                frames_per_buffer=CHUNK)
print "recording..."
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print "finished recording"
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()