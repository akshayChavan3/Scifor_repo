import tkinter as tk
from tkinter import ttk
from googletrans import Translator
import requests


def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text


def translate():
    src_lang = source_lang_combo.get()
    dest_lang = dest_lang_combo.get()
    input_text = input_text_entry.get("1.0", "end-1c")

    if src_lang == dest_lang:
        translated_output_label.config(text="Source and destination languages are the same!")
        return

    translated_text = translate_text(input_text, src_lang, dest_lang)
    translated_output_label.config(text=translated_text)


# Create main window
root = tk.Tk()
root.title("Offline Translator")

# Language options
languages = (
    'Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque',
    'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano',
    'Chichewa', 'Chinese', 'Corsican'
)

# Source language selection
source_lang_label = tk.Label(root, text="Select source language:")
source_lang_label.grid(row=0, column=0, padx=10, pady=5)
source_lang_combo = ttk.Combobox(root, values=languages)
source_lang_combo.grid(row=0, column=1, padx=10, pady=5)
source_lang_combo.current(0)

# Destination language selection
dest_lang_label = tk.Label(root, text="Select destination language:")
dest_lang_label.grid(row=1, column=0, padx=10, pady=5)
dest_lang_combo = ttk.Combobox(root, values=languages)
dest_lang_combo.grid(row=1, column=1, padx=10, pady=5)
dest_lang_combo.current(0)

# Input text entry
input_text_label = tk.Label(root, text="Enter text to translate:")
input_text_label.grid(row=2, column=0, padx=10, pady=5)
input_text_entry = tk.Text(root, height=5, width=30)
input_text_entry.grid(row=2, column=1, padx=10, pady=5)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.grid(row=3, columnspan=2, padx=10, pady=5)

# Output label
translated_output_label = tk.Label(root, text="")
translated_output_label.grid(row=4, columnspan=2, padx=10, pady=5)

root.mainloop()
