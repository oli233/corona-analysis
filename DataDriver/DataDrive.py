import redis
import json

import datetime


class DataDrive():

    def __init__(self, HOST, PORT, PASS):
        self.datapool = redis.Redis(host=HOST,
                                    port=PORT, password=PASS)

    def pack(self, date, value):
        # key = str(key)
        value = str(value)
        self.datapool.set(str(date), value)

    def number_formatter(self, number):

        # comma = True
        offset = -3
        if number == "":
            return number

        if number[0] == '+':
            number = number[1:]

        while (',' in number):
            number = number.replace(',', '')

        # first make sure its a number
        if not number.isnumeric():
            print("trying to convert a string isnt numeric")
            return ""

        return int(number)
        # return number

    def dataoftoday(self):
        today = str(datetime.datetime.now().date())
        print(today)
        return self.lookup(today, '')


    def lookup(self, date, country):

        value = self.datapool.get(date).decode('UTF-8')
        value = value.replace("\'", "\"")
        # print(value)

        data = json.loads(str(value))

        # print(data)
        for item in data:
            if item['country'] == country:
                return item
            elif country == '':
                return data

        return 'invalid'

    def ls(self):
        # for key in self.datapool.scan_iter():
        #     print(key.decode('UTF-8'))
        # print(self.datapool.keys())

        for key in self.datapool.scan_iter():
            print(key)

        # self.datapool.get(b'2020-04-21')

    def rm(self):
        for key in self.datapool.scan_iter("*"):
            self.datapool.delete(key)

