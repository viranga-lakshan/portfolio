import numpy as np
import wave
import struct
import os

sample_rate = 44100
duration = 60.0  # seconds
num_samples = int(sample_rate * duration)

t = np.linspace(0, duration, num_samples, False)

# Create an ambient, modern SaaS corporate tech track
# Chord progression: Am7 -> Fmaj7 -> Cmaj7 -> G (subtle, warm synth chords)
# Frequencies
chords = [
    [220.0, 261.63, 329.63, 392.0],  # Am7
    [174.61, 220.0, 261.63, 329.63], # Fmaj7
    [130.81, 164.81, 196.0, 246.94], # Cmaj7
    [196.0, 246.94, 293.66, 392.0]   # G
]

chord_duration = 3.75  # 4 chords per 15s loop -> 4 loops = 60s
audio_left = np.zeros(num_samples)
audio_right = np.zeros(num_samples)

for i in range(16):
    chord = chords[i % 4]
    c_start = int(i * chord_duration * sample_rate)
    c_end = int((i + 1) * chord_duration * sample_rate)
    c_len = c_end - c_start
    c_t = np.linspace(0, chord_duration, c_len, False)

    # Soft envelope (fade in and out)
    env = np.sin(np.pi * c_t / chord_duration) ** 1.5

    # Pad sound (sum of sines with soft harmonics)
    for idx, f in enumerate(chord):
        pan = 0.3 if idx % 2 == 0 else 0.7
        sine1 = np.sin(2 * np.pi * f * c_t)
        sine2 = 0.3 * np.sin(2 * np.pi * f * 2.0 * c_t)
        sine3 = 0.15 * np.sin(2 * np.pi * (f + 0.5) * c_t)  # chorus detune
        tone = (sine1 + sine2 + sine3) * env * 0.12
        audio_left[c_start:c_end] += tone * (1.0 - pan)
        audio_right[c_start:c_end] += tone * pan

# Add light arpeggio plucks
arp_notes = [523.25, 659.25, 783.99, 1046.50, 880.0, 659.25, 587.33, 783.99]
step_time = 0.25 # 4 notes per sec
num_steps = int(duration / step_time)
for s in range(num_steps):
    note = arp_notes[s % len(arp_notes)]
    s_start = int(s * step_time * sample_rate)
    s_end = min(s_start + int(0.3 * sample_rate), num_samples)
    s_len = s_end - s_start
    if s_len <= 0:
        continue
    st = np.linspace(0, s_len / sample_rate, s_len, False)
    decay = np.exp(-14.0 * st) # quick plucky decay
    pluck = (np.sin(2 * np.pi * note * st) + 0.4 * np.sin(2 * np.pi * note * 2 * st)) * decay * 0.05
    pan = 0.5 + 0.3 * np.sin(s * 0.8)
    audio_left[s_start:s_end] += pluck * (1.0 - pan)
    audio_right[s_start:s_end] += pluck * pan

# Overall fade in (1s) and fade out (2s)
fade_in = np.minimum(1.0, t / 1.0)
fade_out = np.minimum(1.0, (duration - t) / 2.0)
master_gain = fade_in * fade_out * 0.75

audio_left = np.clip(audio_left * master_gain, -0.95, 0.95)
audio_right = np.clip(audio_right * master_gain, -0.95, 0.95)

# Convert to 16-bit PCM
left_pcm = (audio_left * 32767).astype(np.int16)
right_pcm = (audio_right * 32767).astype(np.int16)

# Interleave stereo
stereo = np.empty((num_samples * 2,), dtype=np.int16)
stereo[0::2] = left_pcm
stereo[1::2] = right_pcm

wav_path = r"c:\Users\Viranga\Downloads\upwrok new\hotel-housekeeping-remotion\public\assets\music.wav"
with wave.open(wav_path, "wb") as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(stereo.tobytes())

print(f"Generated WAV audio: {wav_path}")

