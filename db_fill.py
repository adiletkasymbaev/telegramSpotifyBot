from db_models import Song
from db_config import session

song1 = Song(
    author="50 Cent", 
    name="Window Shopper", 
    path="./songs/50 Cent - Window Shopper.mp3"
)

song2 = Song(
    author="Kanye West", 
    name="Stronger", 
    path="./songs/Kanye West - Stronger.mp3"
)

song3 = Song(
    author="Lady Gaga", 
    name="Judas", 
    path="./songs/Lady Gaga - Judas.mp3"
)

song4 = Song(
    author="Dean Martin", 
    name="Let It Snow", 
    path="./songs/Dean Martin - Let It Snow! Let It Snow! Let It Snow!.mp3"
)

session.add(song1)
session.add(song2)
session.add(song3)
session.add(song4)
session.commit()