import asyncio
import os
import edge_tts
from PIL import Image, ImageDraw, ImageFont

assets_dir = r"c:\Users\Viranga\Downloads\upwrok new\hotel-housekeeping-remotion\public\assets"
os.makedirs(assets_dir, exist_ok=True)

VOICE = "en-US-ChristopherNeural"

# Precisely timed for each scene window with comfortable breathing margins:
# Scene 1: 0-8s (8.0s) -> VO ~6.2s
# Scene 2: 8-13s (5.0s) -> VO ~3.8s
# Scene 3: 13-24s (11.0s) -> VO ~7.5s
# Scene 4: 24-34s (10.0s) -> VO ~7.2s
# Scene 5: 34-42s (8.0s) -> VO ~6.2s
# Scene 6: 42-48s (6.0s) -> VO ~4.8s
# Scene 7: 48-54s (6.0s) -> VO ~4.7s
# Scene 8: 54-60s (6.0s) -> VO ~4.2s (leaving 1.8s silence hold for final contact card)

scenes = [
    {
        "id": "scene1",
        "text": "Which rooms are ready? Paper checklists and radios leave front desk guessing—while guests wait.",
        "rate": "+5%",
        "limit": 8.0
    },
    {
        "id": "scene2",
        "text": "Meet RoomReady. Every room. Live. Ready faster.",
        "rate": "+5%",
        "limit": 5.0
    },
    {
        "id": "scene3",
        "text": "See every room in real time. Tiles update live as staff assign, clean, and turnover.",
        "rate": "+2%",
        "limit": 11.0
    },
    {
        "id": "scene4",
        "text": "Housekeepers follow clear checklists on mobile. One tap to start, in their own language.",
        "rate": "+3%",
        "limit": 10.0
    },
    {
        "id": "scene5",
        "text": "Supervisors inspect in seconds. Once passed, the room turns green on front desk screens instantly.",
        "rate": "+4%",
        "limit": 8.0
    },
    {
        "id": "scene6",
        "text": "Maintenance requests include photo proof, locking the room until resolved with instant alerts.",
        "rate": "+5%",
        "limit": 6.0
    },
    {
        "id": "scene7",
        "text": "Owners track turnaround times, pass rates, and team progress on one live dashboard.",
        "rate": "+5%",
        "limit": 6.0
    },
    {
        "id": "scene8",
        "text": "Turn housekeeping into your competitive edge. Book your free live demo today.",
        "rate": "+3%",
        "limit": 6.0
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
    print("Generating calibrated executive voiceover clips...")
    for s in scenes:
        output_file = os.path.join(assets_dir, f"{s['id']}_vo.mp3")
        communicate = edge_tts.Communicate(s["text"], VOICE, rate=s["rate"], pitch="-1Hz")
        await communicate.save(output_file)
        dur = get_mp3_duration(output_file)
        margin = s["limit"] - dur
        print(f"[{s['id']}] Duration: {dur:.2f}s | Limit: {s['limit']}s | Margin: +{margin:.2f}s")
        if margin < 0.3:
            print(f"WARNING: {s['id']} duration is tight!")

def create_logo():
    logo_path = os.path.join(assets_dir, "logo.png")
    # 512x512 transparent logo - Executive Hotel SaaS Badge
    img = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    teal = (13, 148, 136, 255)       # Rich Emerald Teal
    deep_navy = (15, 23, 42, 255)    # Midnight Navy
    emerald = (16, 185, 129, 255)    # Bright Emerald Accent
    gold = (245, 158, 11, 255)       # Subtle Warm Amber/Gold
    white = (255, 255, 255, 255)

    # Outer elegant rounded square with subtle shadow border
    draw.rounded_rectangle([24, 24, 488, 488], radius=110, fill=deep_navy, outline=teal, width=6)
    
    # Inner luminous container
    draw.rounded_rectangle([52, 52, 460, 460], radius=88, fill=(19, 78, 74, 180), outline=(45, 212, 191, 120), width=3)

    # Stylized Hotel Penthouse / Room Keystone Symbol
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

    # Live Status Pulse Ring at top right
    draw.ellipse([345, 135, 375, 165], fill=emerald, outline=white, width=4)

    img.save(logo_path)
    print(f"Generated logo at {logo_path}")

if __name__ == "__main__":
    asyncio.run(generate_voiceovers())
    create_logo()
