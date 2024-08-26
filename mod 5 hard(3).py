
import time

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hash_password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hash_password:
                self.current_user = user
        print('Неверный логин или пароль')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        hash_password = hash(password)
        new_user = User(nickname=nickname, password=hash_password, age=age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for new_video in args:
            new_video_unique = True
            for video in self.videos:
                if video.title == new_video.title:
                    new_video_unique = False
                    break
            if new_video_unique:
                self.videos.append(new_video)
            else:
                print(f'Видео с названием "{new_video.title}" уже существует.')

    def get_videos(self, search_word):
        search_word_low = search_word.lower()
        search_videos = []
        for video in self.videos:
            if search_word_low in video.title.lower():
                search_videos.append(video.title)
        return search_videos

    def watch_video(self, name_video):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return
        video_found = False
        for video in self.videos:
            if video.title == name_video:
                video_found = True
                if self.current_user.age < 18 and video.adult_mode:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for _time in range(1, video.duration + 1):
                    print(_time, end=' ')
                    time.sleep(1)
                print('Конец видео')
                break
        if not video_found:
            print('Такого видео не существует')

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self, title,  duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# попытка воспроизвести несуществующее видео:
ur.watch_video('Лучший язык программирования 2024 года!')
