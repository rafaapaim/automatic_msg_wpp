import requests
import pywhatkit as kit
import datetime
import pyautogui
import PySimpleGUI as sg

from time import sleep


class Screen:
    def __init__(self) -> None:
        sg.theme('DarkBlue17')
        layout = [
            [sg.Text('Sender', size=(10,0)), sg.Input(size=(30,0), key='sender')],
            [sg.Text('Addressee', size=(10,0)), sg.Input(size=(30,0), key='addressee')],
            [sg.Text('Do you want to send advice?')],
            [sg.Checkbox('Yes', key='advice')],
            [sg.Text('Message', size=(10,0)), sg.Input(size=(30,0), key='message')],
            [sg.Text('Hour', size=(10,0)), sg.Input(size=(30,0), key='hour')],
            [sg.Text('Minute', size=(10,0)), sg.Input(size=(30,0), key='minute')],
            [sg.Text('Do you want to close browser after send message?')],
            [sg.Checkbox('Yes', key='close_browser')],
            [sg.Button('Send', size=(10,0)), sg.CloseButton('Close', size=(10,0))]
        ]

        window = sg.Window('Auto Message').layout(layout)

        self.button, self.values = window.Read()

    def start(self) -> None:
        sender = self.values['sender']
        addressee = f'+5551{self.values["addressee"]}'
        send_advice = self.values['advice']
        message = self.values['message']
        hour = int(self.values['hour'])
        minute = int(self.values['minute'])
        close_browser = self.values['close_browser']
        print(self.values)

        if send_advice:
            api_url = 'https://api.adviceslip.com/advice'
            response = requests.get(api_url)
            slip = response.json()['slip']
            kit.sendwhatmsg(f'{addressee}', f'AutoMessage from *{sender}* - \
                            {slip["advice"]}', hour, minute)
        else:
            kit.sendwhatmsg(f'{addressee}', f'AutoMessage from *{sender}* - \
                            {message}', hour, minute)
        
        if close_browser:
            sleep(10)
            pyautogui.click(3818,15, duration=0.5)

screen = Screen()
screen.start()
