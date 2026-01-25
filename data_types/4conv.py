# Эта программа создает сообщение,

print("Создание приветственного сообщения")
name = input("Введите ваше имя: ")
age = 25  # Предполагаемый возраст
hobbies = ["чтение", "спорт", "музыка"]

hobbies_to_str = ", ".join(hobbies)

message = "Привет, " + name + "! Тебе " + str(age) + " лет. Твои хобби: " + hobbies_to_str

print(message)