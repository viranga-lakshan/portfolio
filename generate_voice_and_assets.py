import asyncio
import os
import edge_tts
from PIL import Image, ImageDraw, ImageFont

assets_dir = r"c:\Users\Viranga\Downloads\upwrok new\hotel-housekeeping-remotion\public\assets"
os.makedirs(assets_dir, exist_ok=True)

VOICE = "en-US-AndrewNeural"

scenes = [
    {
        "id": "scene1",
        "start": 0.8,
        "text": "Which rooms are ready? Nobody knows. Paper checklists, walkie-talkies, and messy chat groups mean delays, missed cleanings, and frustrated guests."
    },
    {
        "id": "scene2",
        "start": 8.3,
        "text": "Meet RoomFlow by Team Axio Global. Every room. Live. Ready faster."
    },
    {
        "id": "scene3",
        "start": 13.5,
        "text": "See every room's status live on one screen. Watch tiles update in real time as rooms get assigned, cleaned, and turned around."
    },
    {
        "id": "scene4",
        "start": 24.3,
        "text": "Housekeepers get a clear priority list. One tap starts the timer, checklists guide every task, and staff work effortlessly in their own language."
    },
    {
        "id": "scene5",
        "start": 34.3,
        "text": "Supervisors inspect with a single tap. Once passed, the room turns green on the front desk board—ready to sell instantly."
    },
    {
        "id": "scene6",
        "start": 42.3,
        "text": "Maintenance requests include photo proof and live status tracking, with instant alerts keeping everyone aligned."
    },
    {
        "id": "scene7",
        "start": 48.3,
        "text": "Hotel owners track cleaning times, inspection scores, and team progress on one comprehensive executive dashboard."
    },
    {
        "id": "scene8",
        "start": 54.3,
        "text": "Transform your housekeeping into a live, organized flow. Book your free demo today with Team Axio Global."
    }
]

async def generate_voiceovers():
    print("Generating voiceover clips...")
    for s in scenes:
        output_file = os.path.join(assets_dir, f"{s['id']}_vo.mp3")
        communicate = edge_tts.Communicate(s['text'], VOICE, rate="+3%", pitch="+0Hz")
        await communicate.save(output_file)
        print(f"Generated {output_file}")

def create_logo():
    logo_path = os.path.join(assets_dir, "logo.png")
    # 512x512 transparent logo
    img = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Rounded rectangle background with teal gradient / solid teal
    # Hex: #14B8A6 (Teal), #0F172A (Navy)
    teal = (20, 184, 166, 255)
    dark_teal = (13, 148, 136, 255)
    white = (255, 255, 255, 255)

    # Draw rounded badge
    draw.rounded_rectangle([32, 32, 480, 480], radius=96, fill=teal)
    draw.rounded_rectangle([48, 48, 464, 464], radius=80, fill=dark_teal)

    # Draw modern stylized 'R' + hotel building/door grid icon
    # Draw hotel grid / door keys
    # Door / Room shape
    draw.rounded_rectangle([140, 120, 372, 392], radius=48, fill=(15, 23, 42, 255))
    draw.rounded_rectangle([164, 144, 348, 368], radius=32, fill=(255, 255, 255, 255))

    # Center checkmark / pulse in teal
    # Draw checkmark points
    points = [
        (200, 250),
        (240, 290),
        (315, 205),
        (335, 225),
        (240, 330),
        (180, 270)
    ]
    draw.polygon(points, fill=teal)

    img.save(logo_path)
    print(f"Generated logo at {logo_path}")

asyncio.run(generate_voiceovers())
create_logo()

