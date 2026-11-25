import asyncio
import os
import wave
import numpy as np
import edge_tts
from PIL import Image, ImageDraw

assets_dir = r"c:\Users\Viranga\Downloads\upwrok new\hotel-housekeeping-remotion\public\assets"
os.makedirs(assets_dir, exist_ok=True)

VOICE = "en-US-ChristopherNeural"

# Target scene frame lengths:
# Scene 1: 225 frames = 7.50s (Max VO ~6.2s)
# Scene 2: 180 frames = 6.00s (Max VO ~4.8s)
# Scene 3: 315 frames = 10.50s (Max VO ~8.5s)
# Scene 4: 285 frames = 9.50s (Max VO ~7.8s)
# Scene 5: 240 frames = 8.00s (Max VO ~6.5s)
# Scene 6: 180 frames = 6.00s (Max VO ~4.8s)
# Scene 7: 180 frames = 6.00s (Max VO ~4.8s)
# Scene 8: 195 frames = 6.50s (Max VO ~4.4s, leaving 2.1s hold)
# Total = 1800 frames = exactly 60.0s

scenes = [
    {
        "id": "scene1",
        "text": "Which rooms are ready? Paper checklists and radios leave front desk guessing, while guests wait.",
        "rate": "+4%",
        "limit": 6.8
    },
    {
        "id": "scene2",
        "text": "Meet RoomReady: every room, live, ready faster.",
        "rate": "+4%",
        "limit": 5.0
    },
    {
        "id": "scene3",
        "text": "See every room in real time. Tiles update live as staff assign, clean, and turnover.",
        "rate": "+2%",
        "limit": 9.0
    },
    {
        "id": "scene4",
        "text": "Housekeepers follow clear checklists on mobile, with instant timers in their own language.",
        "rate": "+3%",
        "limit": 8.0
    },
    {
        "id": "scene5",
        "text": "Supervisors inspect in seconds. Tap Pass, and the room turns green on front desk screens.",
        "rate": "+4%",
        "limit": 6.8
    },
    {
        "id": "scene6",
        "text": "Maintenance issues include photo proof, auto-locking the room until resolved.",
        "rate": "+5%",
        "limit": 5.0
    },
    {
        "id": "scene7",
        "text": "Owners track turnaround times, pass rates, and team progress on one live dashboard.",
        "rate": "+5%",
        "limit": 5.0
    },
    {
        "id": "scene8",
        "text": "Turn housekeeping into your competitive edge. Book your free live demo today.",
        "rate": "+3%",
        "limit": 4.5
    }
]

def get_mp3_duration(path):
    with open(path, "rb") as f:
        data = f.read()
    pos = 0
    if data[:3] == b"ID3":
        size = ((data[6] & 0x7F) << 21) | ((data[7] & 0x7F) << 14) | ((data[8] & 0x7F) << 7) | (data[9] & 0x7F)
        pos = 10 + size
    bitrates_v2 = [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0]
    sample_rates_v2 = [22050, 24000, 16000, 0]
    total_samples = 0
    sample_rate = 24000
    while pos < len(data) - 4:
        if data[pos] == 0xFF and (data[pos+1] & 0xE0) == 0xE0:
            header = (data[pos] << 24) | (data[pos+1] << 16) | (data[pos+2] << 8) | data[pos+3]
            sr_idx = (header >> 10) & 3
            br_idx = (header >> 12) & 0xF
            padding = (header >> 9) & 1
            if sr_idx < 3 and br_idx > 0 and br_idx < 15:
                sample_rate = sample_rates_v2[sr_idx]
                bitrate = bitrates_v2[br_idx] * 1000
                frame_len = (72 * bitrate // sample_rate) + padding
                total_samples += 576
                pos += frame_len
                continue
        pos += 1
    return total_samples / sample_rate

async def generate_voiceovers():
    print("--- GENERATING CALIBRATED VOICEOVERS ---")
    for s in scenes:
        output_file = os.path.join(assets_dir, f"{s['id']}_vo.mp3")
        communicate = edge_tts.Communicate(s["text"], VOICE, rate=s["rate"], pitch="-1Hz")
        await communicate.save(output_file)
        dur = get_mp3_duration(output_file)
        margin = s["limit"] - dur
        print(f"[{s['id']}] Duration: {dur:.2f}s | Limit: {s['limit']}s | Margin: +{margin:.2f}s")
        if margin < 0:
            print(f"ERROR: {s['id']} duration exceeds limit by {-margin:.2f}s!")

def generate_luxury_hotel_soundtrack():
    print("--- SYNTHESIZING LUXURY HOTEL AMBIENT SOUNDTRACK ---")
    sr = 44100
    total_duration = 60.0
    num_samples = int(sr * total_duration)
    t = np.linspace(0, total_duration, num_samples, False)

    left = np.zeros(num_samples)
    right = np.zeros(num_samples)

    # Progression: Fmaj9 -> Am7 -> Bbmaj9 -> C9sus
    # Luxury hospitality chords (frequencies in Hz):
    chord_progression = [
        # Fmaj9: F3 (174.61), C4 (261.63), E4 (329.63), G4 (392.00), A4 (440.00)
        [174.61, 261.63, 329.63, 392.00, 440.00],
        # Am7: A2 (110.00), E3 (164.81), G3 (196.00), C4 (261.63), E4 (329.63)
        [110.00, 164.81, 196.00, 261.63, 329.63],
        # Bbmaj9: Bb2 (116.54), F3 (174.61), A3 (220.00), D4 (293.66), F4 (349.23)
        [116.54, 174.61, 220.00, 293.66, 349.23],
        # C9sus: C3 (130.81), G3 (196.00), Bb3 (233.08), D4 (293.66), F4 (349.23)
        [130.81, 196.00, 233.08, 293.66, 349.23],
    ]
    bass_roots = [87.31, 110.00, 116.54, 130.81] # F2, A2, Bb2, C3

    chord_time = 3.75 # 4 chords * 3.75s = 15s loop -> 4 repeats = 60s

    for i in range(16):
        c_idx = i % 4
        c_notes = chord_progression[c_idx]
        b_root = bass_roots[c_idx]
        start_samp = int(i * chord_time * sr)
        end_samp = int(min((i + 1) * chord_time * sr, num_samples))
        chunk_len = end_samp - start_samp
        if chunk_len <= 0:
            continue
        ct = np.linspace(0, chunk_len / sr, chunk_len, False)

        # 1. Warm Silk Pad Envelope (smooth swell and sustain)
        pad_env = np.sin(np.pi * ct / (chunk_len / sr)) ** 1.3

        # Pad harmonics
        for n_idx, freq in enumerate(c_notes):
            pan = 0.25 + 0.5 * (n_idx / len(c_notes))
            # Multi-oscillator detuned warmth
            s1 = np.sin(2 * np.pi * freq * ct)
            s2 = 0.35 * np.sin(2 * np.pi * (freq * 1.002) * ct)
            s3 = 0.35 * np.sin(2 * np.pi * (freq * 0.998) * ct)
            pad_tone = (s1 + s2 + s3) * pad_env * 0.08
            left[start_samp:end_samp] += pad_tone * (1.0 - pan)
            right[start_samp:end_samp] += pad_tone * pan

        # 2. Electric Piano / Rhodes chord strike on downbeat
        # Envelope: immediate strike, natural decay
        ep_env = np.exp(-1.8 * ct) + 0.15 * np.exp(-0.4 * ct)
        for n_idx, freq in enumerate(c_notes):
            pan = 0.35 if n_idx % 2 == 0 else 0.65
            # Bell tine transient + rich warm body
            tine = 0.4 * np.sin(2 * np.pi * freq * 3.0 * ct) * np.exp(-25.0 * ct)
            body1 = np.sin(2 * np.pi * freq * ct)
            body2 = 0.3 * np.sin(2 * np.pi * freq * 2.0 * ct)
            body3 = 0.1 * np.sin(2 * np.pi * freq * 4.0 * ct)
            ep_tone = (body1 + body2 + body3 + tine) * ep_env * 0.09
            left[start_samp:end_samp] += ep_tone * (1.0 - pan)
            right[start_samp:end_samp] += ep_tone * pan

        # 3. Deep warm acoustic bass pluck
        bass_env = np.exp(-1.2 * ct)
        bass_tone = (np.sin(2 * np.pi * b_root * ct) + 0.4 * np.sin(2 * np.pi * b_root * 2.0 * ct)) * bass_env * 0.16
        left[start_samp:end_samp] += bass_tone * 0.5
        right[start_samp:end_samp] += bass_tone * 0.5

    # 4. Delicate Acoustic Chime / Sparkle arpeggios
    chimes = [523.25, 659.25, 783.99, 880.00, 1046.50, 1318.51] # C, E, G, A, C5, E5
    step_s = 0.25 # 4 notes per sec
    num_steps = int(total_duration / step_s)
    for s in range(num_steps):
        note = chimes[(s * 3 + 1) % len(chimes)]
        ns_start = int(s * step_s * sr)
        ns_end = min(ns_start + int(0.4 * sr), num_samples)
        n_len = ns_end - ns_start
        if n_len <= 0:
            continue
        nt = np.linspace(0, n_len / sr, n_len, False)
        chime_env = np.exp(-12.0 * nt)
        chime_tone = (np.sin(2 * np.pi * note * nt) + 0.3 * np.sin(2 * np.pi * note * 2.0 * nt)) * chime_env * 0.035
        pan = 0.5 + 0.35 * np.sin(s * 0.6)
        left[ns_start:ns_end] += chime_tone * (1.0 - pan)
        right[ns_start:ns_end] += chime_tone * pan

    # Fade in (1.2s) and fade out (2.2s)
    fade_in = np.minimum(1.0, t / 1.2)
    fade_out = np.minimum(1.0, (total_duration - t) / 2.2)
    master_gain = fade_in * fade_out * 0.72

    # Analog Tape Soft-Saturation (smooth tanh compression)
    left = np.tanh(left * master_gain * 1.1) * 0.85
    right = np.tanh(right * master_gain * 1.1) * 0.85

    # Save to WAV
    left_pcm = (left * 32767).astype(np.int16)
    right_pcm = (right * 32767).astype(np.int16)
    stereo = np.empty((num_samples * 2,), dtype=np.int16)
    stereo[0::2] = left_pcm
    stereo[1::2] = right_pcm

    wav_path = os.path.join(assets_dir, "music.wav")
    with wave.open(wav_path, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(stereo.tobytes())
    print(f"Generated music WAV: {wav_path}")

    # Also save MP3
    mp3_path = os.path.join(assets_dir, "music.mp3")
    # Convert WAV to MP3 using ffmpeg if available or wave
    os.system(f'npx remotion ffmpeg -y -i "{wav_path}" -b:a 192k "{mp3_path}"')
    print(f"Converted music MP3: {mp3_path}")

def generate_sfx():
    print("--- GENERATING HIGH-END UI SOUND EFFECTS ---")
    sr = 44100

    def write_wav(filename, audio_data):
        pcm = (np.clip(audio_data, -0.95, 0.95) * 32767).astype(np.int16)
        path = os.path.join(assets_dir, filename)
        with wave.open(path, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sr)
            wf.writeframes(pcm.tobytes())
        print(f"Generated SFX: {path}")

    # 1. SFX Click / Tap (soft haptic button tap ~0.08s)
    dur = 0.08
    n = int(sr * dur)
    t = np.linspace(0, dur, n, False)
    click = (np.sin(2 * np.pi * 320 * t) + 0.5 * np.sin(2 * np.pi * 840 * t)) * np.exp(-60.0 * t)
    write_wav("sfx_click.wav", click * 0.6)

    # 2. SFX Chime / Success (crystalline hotel bell chime ~1.2s)
    dur = 1.2
    n = int(sr * dur)
    t = np.linspace(0, dur, n, False)
    c_env = np.exp(-4.5 * t)
    chime = (
        np.sin(2 * np.pi * 523.25 * t) +
        0.7 * np.sin(2 * np.pi * 659.25 * t) +
        0.5 * np.sin(2 * np.pi * 783.99 * t) +
        0.4 * np.sin(2 * np.pi * 1046.50 * t) +
        0.2 * np.sin(2 * np.pi * 1567.98 * t)
    ) * c_env
    write_wav("sfx_chime.wav", chime * 0.45)

    # 3. SFX Pop / Notification (soft bubbly bubble pop ~0.15s)
    dur = 0.15
    n = int(sr * dur)
    t = np.linspace(0, dur, n, False)
    freq = 400 + 400 * (t / dur)
    pop = np.sin(2 * np.pi * freq * t) * np.exp(-30.0 * t)
    write_wav("sfx_pop.wav", pop * 0.5)

    # 4. SFX Whoosh (soft cinematic transition sweep ~0.6s)
    dur = 0.6
    n = int(sr * dur)
    t = np.linspace(0, dur, n, False)
    noise = np.random.uniform(-1, 1, n)
    sweep_env = np.sin(np.pi * t / dur) ** 2
    # Simple lowpass moving average
    filtered_noise = np.convolve(noise, np.ones(25)/25, mode='same')
    whoosh = filtered_noise * sweep_env * 0.35
    write_wav("sfx_whoosh.wav", whoosh)

def create_logo():
    logo_path = os.path.join(assets_dir, "logo.png")
    img = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    teal = (13, 148, 136, 255)       # Rich Emerald Teal
    deep_navy = (15, 23, 42, 255)    # Midnight Navy
    emerald = (16, 185, 129, 255)    # Bright Emerald Accent
    white = (255, 255, 255, 255)

    draw.rounded_rectangle([24, 24, 488, 488], radius=110, fill=deep_navy, outline=teal, width=6)
    draw.rounded_rectangle([52, 52, 460, 460], radius=88, fill=(19, 78, 74, 180), outline=(45, 212, 191, 120), width=3)

    # Roof / Top Arch
    draw.polygon([(256, 110), (370, 200), (330, 200), (256, 145), (182, 200), (142, 200)], fill=white)
    
    # Central Room Frame
    draw.rounded_rectangle([175, 205, 337, 385], radius=36, fill=(15, 23, 42, 255), outline=white, width=8)

    # Emerald Ready Checkmark inside the door
    points = [
        (215, 290),
        (245, 320),
        (298, 255),
        (314, 270),
        (245, 350),
        (198, 305)
    ]
    draw.polygon(points, fill=emerald)

    # Live Status Pulse Ring
    draw.ellipse([345, 135, 375, 165], fill=emerald, outline=white, width=4)

    img.save(logo_path)
    print(f"Generated logo at {logo_path}")

if __name__ == "__main__":
    asyncio.run(generate_voiceovers())
    generate_luxury_hotel_soundtrack()
    generate_sfx()
    create_logo()

