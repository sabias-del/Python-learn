


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(
    ["Не могу я тебе в день рождения",
     "Дорогие подарки дарить",
     "Но зато в эти ночи весенние "]
)

bull_on_parade = Song([
    "Далеко-далеко на лугу пасется?",
    "Пейте, дети, молоко будете здоровы!"
])

happy_bday.sing_me_a_song()

bull_on_parade.sing_me_a_song()