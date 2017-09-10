# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox
import subprocess


def shutdown():
    try:
        subprocess.call(u'shutdown -s -t {}'.format(int(minutes.get())))
    except ValueError:
        error_message = u'Вы ввели неверное колличество минут. Введите целое число.'
        tkMessageBox.showwarning(title=u'Ошибка', message=error_message)


def abort():
    subprocess.call('shutdown -a')

root = Tkinter.Tk()

minutes = Tkinter.Entry(root)
minutes.grid(row=1, column=1, columnspan=2)
Tkinter.Button(root, text=u'Выключить компютер', command=shutdown).grid(row=2, column=1, columnspan=2)
Tkinter.Button(root, text=u'Отменить выключение', command=abort).grid(row=3, column=1, columnspan=2)

if __name__ == '__main__':
    root.mainloop()
