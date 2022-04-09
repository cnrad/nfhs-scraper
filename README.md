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

Run the Python file, and let the magic of computers do it's thing. It can take a while.

-------------------------------
##### Feel free to star this repo ⭐
