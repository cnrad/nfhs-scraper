import subprocess
import requests
import os 

game_id = "gam67ba2a837e"
project_folder = "/Users/conrad/Desktop/nfhsscraper"

scrub_number = 1
scrub_id = f'{scrub_number:06}'
scrub_state = True
scrub_url = f"https://cfscrubbed.nfhsnetwork.com/{game_id}/{game_id}_{scrub_id}.ts"

ts_list = []
threads = []

for i in range(600):
    scrub_id = f'{scrub_number:06}'
    scrub_url = f"https://cfscrubbed.nfhsnetwork.com/{game_id}/{game_id}_{scrub_id}.ts"

    print(f"Getting {scrub_id}...")
    res = requests.get(scrub_url)

    if "AccessDenied" in res.text:
        scrub_state = False

    open(f'{project_folder}/{game_id}_{scrub_id}.ts', 'wb').write(res.content)
    ts_list.append(f'{project_folder}/{game_id}_{scrub_id}.ts')

    print(f"{scrub_url} downloaded.")

    scrub_number += 1


for file in ts_list:
    with open(f"{project_folder}/tslist.txt", "a") as txt:
        print(f"Writing {file} to file...")
        txt.write(f'file \'{file}\'\n')


infile = f'{project_folder}/tslist.txt'
outfile = f'{project_folder}/output.mp4'

subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', infile, outfile])

for file in ts_list:
    os.remove(f"{project_folder}/{file}")

print("Program done, output complete.")
