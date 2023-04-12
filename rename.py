# yt-dlp -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "https://www.youtube.com/playlist?list=OLAK5uy_nYkTcWLQkJ6qsws91O5UFvNkIsvweu1sw"

import re
import os


title_file = f"title"
with open(title_file) as file:
    titles = file.read().splitlines()
    for filename in os.listdir("."):
        if filename.startswith("0"):
            index = int(filename[0:3])
            kanji = titles[11 + 6 * index]
            kanji = kanji.replace("/", "⁄")
            kanji = kanji.replace("-", "–")
            kanji = kanji.replace("?", "？")
            kanji = kanji.replace("!", "！")

            new_name = f"{index:03} - {kanji} - {filename[6:]}"
            try:
                print(new_name)
                os.rename(f"{filename}", f"{new_name}")
            except OSError as err:
                print("OS Error: {0}{1} already exists.".format(err, new_name))
