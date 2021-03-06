import subprocess
import requests
import os 
from pathlib import Path 

game_id = "your_game_id" # Game ID goes here
scrub_count = 6

project_folder = str(Path(__file__).parent.resolve())
ts_list = []
s = requests.Session()

for i in range(scrub_count):
    scrub_id = f'{i:06}'
    scrub_url = f"https://cfscrubbed.nfhsnetwork.com/{game_id}/{game_id}_{scrub_id}.ts"

    print(f"Getting {game_id}_{scrub_id}.ts...")

    res = s.get(scrub_url)
    print(f"{game_id}_{scrub_id}.ts downloaded.")

    open(f'{project_folder}/{game_id}_{scrub_id}.ts', 'wb').write(res.content)
    ts_list.append(f'{project_folder}/{game_id}_{scrub_id}.ts')


for file in ts_list:
    with open(f"{project_folder}/tslist.txt", "a") as txt:
        print(f"Writing {file} to file...")
        txt.write(f'file \'{file}\'\n')

infile = f'{project_folder}/tslist.txt'
outfile = f'{project_folder}/output.mp4'
subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', infile, outfile])

for file in ts_list:
    if os.path.exists(file):
        os.remove(file)
        print(f"Removed {file}")
    else:
        print(f"Cannot find {file}")

os.remove(f"{project_folder}/tslist.txt")

print("Program done, output complete.")
