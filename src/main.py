# Импорт load_dotenv.
from dotenv import load_dotenv 

# Импорт библиотеки для работы с окружением.
import os  

# Загрузка переменных из .env
load_dotenv(dotenv_path=r"C:\Users\sobnt\OneDrive\Desktop\DATA SCIENE - ЯНДЕКС ПРАКТИКУМ\Git\testproject\.env")

# Теперь переменные доступны через os.environ
AUTHOR = os.getenv('AUTHOR')

print ("Hello from repository!!!")

def print_author(AUTHOR):
	print(f"Автор проекта: {AUTHOR}")

print_author(AUTHOR)
