from http.client import responses
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None


def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img


def exit_():
    window.destroy()

window = Tk()
window.title('Cats!')
window.geometry('800x600')

label = Label()
label.pack()

# update_button = Button(text='Обновить картинку', command=set_image)
# update_button.pack(anchor="s", padx=10, pady=10)

menu_bar = Menu(window)
window.config(menu = menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu = file_menu)
menu_bar.add_cascade(label='Загрузить фото', command = set_image)
menu_bar.add_separator()
menu_bar.add_command(label='Выход', command = exit_)


url = 'https://cataas.com/cat'

img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

set_image()

window.mainloop()