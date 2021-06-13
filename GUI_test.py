#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ===========================================================================================>
#                                                                             >
# Author: Juan Sebastian Diaz Boada                                                          >
# Creation Date:                                                                   >
# ===========================================================================================>
# hello_psg.py

import PySimpleGUI as sg

layout = [[sg.Text("Drug 1"),sg.Text("Drug 2")], [sg.Button("Calculate")]]

# Create the window
window = sg.Window("Demo", layout,margins=(500, 400))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
