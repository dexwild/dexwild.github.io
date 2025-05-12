#!/usr/bin/env python3
import os, json, random

# adjust this to your folder
video_dir = os.path.join('resources', 'data_grid_videos')

# list and sort all .mp4 files
videos = sorted(
    os.path.join(video_dir, f)
    for f in os.listdir(video_dir)
    if f.lower().endswith('.mp4')
)

# shuffle the list
random.shuffle(videos)

# write JSON array
os.makedirs('_data', exist_ok=True)
with open(os.path.join('_data', 'data_collection_videos.json'), 'w') as out:
    json.dump(videos, out, indent=2)

print(f"Written {len(videos)} entries.")
