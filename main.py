from __future__ import unicode_literals
import youtube_dl
import PySimpleGUI as sg

layout = [
    [sg.Text("Insira a URL", size=(12, 1)), sg.InputText()],
    [sg.Button("Baixar")]
]

window = sg.Window("Made by José de Brito", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    ydl_opts = {
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([values[0]])
        layout.append([sg.Text("Baixando...")])

