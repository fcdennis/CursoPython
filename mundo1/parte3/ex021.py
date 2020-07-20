from pygame import mixer

mixer.init()
mixer.music.load('mundo1\frei-name-of-names-65690463.mp3')
mixer.music.play()
mixer.event.wait()
