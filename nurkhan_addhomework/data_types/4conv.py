# Эта программа создает сообщение,

print("Создание приветственного сообщения")
name = input("Введите ваше имя: ")
age = 25  # Предполагаемый возраст
hobbies = ["чтение", "спорт", "музыка"]

hobbies_str = ", ".join(hobbies)

message = f"Привет, {name} ! Тебе {age} лет. Твои хобби: {hobbies_str}"

print(message)
