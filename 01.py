from csv import DictWriter, DictReader
from os.path import exists
import csv

filename = "phone.csv"
filename2 = "phone_copy.csv"

def get_data():
    first_name = "Иван"
    last_name = "Иванов"
    phone="+79001234567"
    text = "\n" + first_name + "," + last_name + "," + phone
    return text


def create_file(filename):
    f_w = open(filename, 'w')
    f_w.write("Фамилия,Имя,Отчество")
    f_w.close()

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        #f_r = DictReader(data)
        #return f_r
        with open(filename) as r_file:
            file_reader = csv.reader(r_file, delimiter="\n")
            text = ""
            for row in file_reader:
                #print(row)
                for line in row:
                    str1 = line.rsplit(",")
                    count = 0
                    for el in str1:
                        #print(el)
                        text = text + el
                        count +=1
                        #print(count)
                        #print(len(str1))
                        if count != (len(str1)):
                            text = text + ","
                text = text + "\n"

            return text


def input_file(filename, info):
    with open(filename, 'a') as f_w:
        f_w.write(info)
    f_w.close()

def copy_data(filename):
    with open(filename) as r_file:
        file_reader = csv.reader(r_file, delimiter="\n")
        count = -1
        for row in file_reader:
            count += 1
        return(count)

def copy_data2(filename, row_num):
    with open(filename) as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        count = 0
        count2 = 0
        for row2 in file_reader:
            if int(row_num) == count:
                #print(int(row_num))
                #print(row2)
                f_w = open(filename2, 'a')
                new_row = ""
                for el in row2:
                    new_row += el
                    #print(el)
                    count2 += 1
                    if count2 != (len(row2)):
                        new_row = new_row + ","
                new_row = new_row + "\n"
                f_w.write(new_row)
                f_w.close()
            count += 1



def main2():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(filename):
                create_file(filename)
            info_in = get_data()
            input_file(filename, info_in)
            input_file(filename, info_in)
        elif command == "r":
            if not exists(filename):
                print("Файл не существует! Создайте его!")
                continue
            print(read_file(filename))
        elif command == "c":
            if not exists(filename2):
                f_w = open(filename2, 'w')
                f_w.close()
            rows_num = copy_data(filename)
            if rows_num > 0:
                print(f"Количество записей = {rows_num}")
                print("Введите номер строки для копирования: ")
                command_2 = int(input())
                #print(command_2)
                if 0 <= command_2 <= rows_num:
                    copy_data2(filename, command_2)
                    print("Готово!")
                else:
                    print(f"Такой строки нет в файле. Там всего {rows_num}")

main2()