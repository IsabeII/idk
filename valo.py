import os
import win32api
import win32con

def open_explorer_and_drive(path):
    os.startfile(path)
drive_d_path = "C:\\Riot Games"

if os.path.exists(drive_d_path):
    open_explorer_and_drive(drive_d_path)
    while True:
        result = win32api.MessageBox(0, "valorant löschen ?", "kys", win32con.MB_YESNO)

        if result == win32con.IDYES:
            break

        else:
            pass
    open_explorer_and_drive(drive_d_path) 
else:
    print("Das Laufwerk D existiert nicht Womp WOMP.")
