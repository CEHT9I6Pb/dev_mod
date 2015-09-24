import telnetlib
import time

# -*- coding: utf8 -*-
__author__ = 'Михаил'

# запрос ip устройства
device_ip = input("Введите IP устройства: ")


# print(device_ip)

# заходим на устройство по telnet
def open_telnet_conn(device_ip):
    try:
        # задаем параметры входа
        username = 'admin'
        password = 'voxtel'

        # порт для входа (по умолчанию для telnet - 23)
        port = 23

        # определяем timeout соединения
        connection_timeout = 5

        # определяем timeout ожидания
        reading_timeout = 5

        # определение функции входа
        connection = telnetlib.Telnet(device_ip, port, connection_timeout)

        # одидаем запроса логина
        router_output = connection.read_until()