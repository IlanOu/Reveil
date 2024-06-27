from src.base.Base import Reveil
from src.actions.MusicPlayer import MusicPlayer


if __name__ == "__main__":
    reveil = Reveil()
    reveil.add_action(MusicPlayer.play, ["https://youtube.com/qdognqpsflsqi"])
    reveil.start()