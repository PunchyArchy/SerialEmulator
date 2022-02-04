""" Модуль для создания эмулятора SerialDevice (например, весовой терминал)
Который отправляет по клиентам заданные данные.
Запустим только на Linux!!!"""

import os, serial, time
from scale_emulator import functions


class SerialEmulator(object):
    def __init__(self, data_source=None, host_port='./somehost',
                 client_port='./someclient', send_timeout=1):
        self.host_port = host_port
        self.socat_proc = functions.init_socat(host_port, client_port)
        self.data_source = data_source
        self.send_timeout = send_timeout
        self.ser = serial.Serial(port=self.host_port)

    def __exit__(self):
        self.socat_proc.kill()

    def get_data(self):
        with open(self.data_source, 'rb') as ds:
            data = ds.readline()
            yield data

    def main(self):
        while True:
            data = self.get_data()
            print('data', data)
            self.ser.write(data)
            time.sleep(1)

