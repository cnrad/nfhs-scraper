# nfhs-scraper

*Disclaimer: I am in no way responsible for what you choose to do with this script and guide. I do not endorse avoiding paywalls or any illegal activity relating to this matter, I am simply providing a Python script to those who are interested.*

#### NFHS Network is "the leader in streaming Live and On Demand high school sports." 
In short, you need to pay $10 a month for a subscription to watch these games. 
As an athlete, I didn't want to spend $10 a month to watch my own games, **with ads** in it, so I made this. 

## Usage

Download the provided `main.py` Python file, so you can run it **yourself**. Remember, whatever you do is your choice and your responsibility.

Navigate to https://www.nfhsnetwork.com/, and find your school and sport, and select the game video you'd like to download.

#### In the last portion of the url, you will find the **game ID**. 

> e.g. `https://www.nfhsnetwork.com/events/cool-high-school-cool-town/gam4576a0f402` -> game ID is `gam4576a0f402`

\
**In the `main.py` file, do 2 things:**
- Change the `game_id` variable to your game ID.
- Change the `scrub_count` variable to however much of the game you'd like to download. The game footage sometimes goes until 1-2 hours after the game ends, so you can usually omit this by lowering the count. 
  - *Scrubs are **10 seconds** long each, you figure out how many of them you want to get your desired video length.*

Run the Python file, and let the magic of computers do it's thing. It can take a while, but the video will be saved to `output.mp4` in the same directory as the project, by default.



## How it works

With only a bit of reverse engineering, it isn't too hard to understand how NFHS streams video to the user, and why this script works.

NFHS requires a subscription to watch the videos, and with this subscription comes an API key used to fetch the stream. In this case, you need a valid API key to fetch the stream, which is a .m3u8 file that looks a little something like this:
```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGET-DURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXT-INF:10.000000,
gamed408a95df_000000.ts
#EXT-INF:10.000000,
gamed408a95df_000001.ts
#EXT-INF:10.000000,
gamed408a95df_000002.ts

...and so on
```

Here, we notice a few things.
- a) each media file is 10 seconds long, as specified by EXT-INF and EXT-X-TARGET-DURATION
- b) the media files are incremental, meaning we don't need the .m3u8 stream at all to construct one ourselves

In the network tab, while watching the game, I could see my browser making a request to these files, which are hosted at `https://cfscrubbed.nfhsnetwork.com/`. I tried downloading one of these files myself, and was able to do so successfully with no authentication needed. So, hypothetically, I could download every file and then patch them together into one big video. 

Hence, nfhs-scraper. :)

-------------------------------
##### Feel free to star this repo ⭐
