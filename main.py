import subprocess
import requests
import os 
from pathlib import Path 

game_id = "gam67ba2a837e" # Game ID goes here

project_folder = str(Path(__file__).parent.resolve())
scrub_number = 1
ts_list = []
s = requests.Session()

for i in range(600):
    scrub_id = f'{scrub_number:06}'
    scrub_url = f"https://cfscrubbed.nfhsnetwork.com/{game_id}/{game_id}_{scrub_id}.ts"

    print(f"Getting {game_id}_{scrub_id}.ts...")

    res = s.get(scrub_url)
    print(f"{game_id}_{scrub_id}.ts downloaded.")

    open(f'{project_folder}/{game_id}_{scrub_id}.ts', 'wb').write(res.content)
    ts_list.append(f'{project_folder}/{game_id}_{scrub_id}.ts')

    scrub_number += 1

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

print("Program done, output complete.")
