import tempfile
from urllib.request import urlretrieve


def process(url):
    with tempfile.NamedTemporaryFile("w+t") as temp:
        urlretrieve(url, temp.name)
        temp.seek(0)
        return "\n".join(
            word.rstrip()
            for word in temp.readlines()
            if "a" in word
            and "e" in word
            and "i" in word
            and "o" in word
            and "u" in word
        )


print(
    process(
        "https://gist.githubusercontent.com/reuven/9ea704169a2b633d8afd27fc340ad8c5/raw/7b255766069e4229a4a2498f429ecd01bb820f11/words.txt"
    )
)
