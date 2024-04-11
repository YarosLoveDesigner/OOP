class Exhibit:
    def __init__(self, name, description, year):
        self.name = name  # Создаем атрибут name для хранения названия экспоната
        self.description = description  # Создаем атрибут description для хранения описания экспоната
        self.year = year  # Создаем атрибут year для хранения года создания экспоната

    def display_info(self):
        print(f"Название экспоната: {self.name}")  # Выводим название экспоната на экран
        print(f"Описание: {self.description}")  # Выводим описание экспоната на экран
        print(f"Год создания: {self.year}")  # Выводим год создания экспоната на экран


class ExhibitionRoom:
    def __init__(self, room_number, exhibits):
        self.room_number = room_number  # Создаем атрибут room_number для хранения номера зала
        self.exhibits = exhibits  # Создаем атрибут exhibits для хранения экспонатов в зале

    def add_exhibit(self, exhibit):
        self.exhibits.append(exhibit)  # Добавляем экспонат в список экспонатов зала

    def show_exhibits(self):
        print(f"Экспозиция в зале {self.room_number}:")  # Выводим информацию о зале на экран
        for exhibit in self.exhibits:  # Перебираем экспонаты в зале
            exhibit.display_info()  # Выводим информацию об экспонате на экран


class Museum:
    def __init__(self, name, location, exhibition_rooms):
        self.name = name  # Создаем атрибут name для хранения названия музея
        self.location = location  # Создаем атрибут location для хранения местоположения музея
        self.exhibition_rooms = exhibition_rooms  # Создаем атрибут exhibition_rooms для хранения списка залов

    def add_exhibition_room(self, exhibition_room):
        self.exhibition_rooms.append(exhibition_room)  # Добавляем зал в список залов музея

    def show_rooms(self):
        print(
            f"Музей '{self.name}', расположенный в {self.location}, содержит следующие залы:")  # Выводим информацию о музее на экран
        for room in self.exhibition_rooms:  # Перебираем залы музея
            room.show_exhibits()  # Выводим информацию об экспонатах в каждом зале на экран


# Создаем экспонаты
exhibit1 = Exhibit("Статуя Давида", "Мраморная статуя Микеланджело", 1504)
exhibit2 = Exhibit("Мона Лиза", "Портрет Леонардо да Винчи", 1503)
exhibit3 = Exhibit("Богатырь", "Картина Виктора Васнецова", 1898)

# Создаем залы и добавляем в них экспонаты
room1 = ExhibitionRoom(1, [exhibit1, exhibit2])
room2 = ExhibitionRoom(2, [exhibit3])

# Создаем музей и добавляем в него залы
museum = Museum("Эрмитаж", "Санкт-Петербург", [room1, room2])