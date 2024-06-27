from src.base.Waker import Waker
from src.actions.MusicPlayer import MusicPlayer


if __name__ == "__main__":
    waker = Waker()
    waker.add_action(MusicPlayer.play, ["https://youtube.com/qdognqpsflsqi"])
    waker.start()