import configparser
import os
import sys

config = configparser.ConfigParser()
config.read('config.ini')
root_dir = config.get('Settings', 'root')
pwd = root_dir
num = 0

def starts():
    '''Меню '''
    print('1. Создание папки (с указанием имени)')
    print('2. Удаление папки по имени')
    print('3. Перемещение файлов')
    print('4. Переименование файлов')
    print('5. Создание файла')
    print('6. Удаление файла по имени')
    print('7. Запись в файл')
    print('8. Смена директории')
    print('9. Выход из программы\n\n')  

    try:
        num = int(input('Введите номер желаемой операции: '))
    except:
        print('Неверный формат ввода.\n')
        sys.exit()

    def make_dir():   
        ''' Создание папки (с указанием имени)'''
        name = str(input('Введите название папки для создания: '))
        try:    
            os.mkdir(os.path.join(pwd, name))
            print('Папка создана.\n')
        except Exception:
            print('Неверное название папки или папка вне корневой директории.\n')

    def delete_dir():
        '''Удаление папки по имени'''
        name = str(input('Введите название папки для удаления: '))
        try:    
            os.rmdir(os.path.join(pwd, name))
            print('Папка удалена.\n')
        except Exception:
            print('Неверное название папки или папка вне корневой директории.\n')

    def remove_file():
        '''Перемещение файлов '''
        name = str(input('Введите название файла для перемещения: ')) 
        new_place = str(input('Введите куда переместить папку: '))   
        try:
            os.replace(os.path.join(pwd, name), os.path.join(pwd, new_place))
            print('Папка перемещена.\n')
        except Exception:
            print('Неверное название  или папка вне корневой директории.\n')  

    def rename_file():
        '''Переименование файлов'''
        name = str(input('Введите название файла для переименования: ')) 
        new_name = str(input('Введите новое имя файла: '))  
        try:
            os.rename(os.path.join(pwd, name), os.path.join(pwd, new_name))
            print('Файл переименован.\n')
        except Exception:
            print('Неверное название папки или папка вне корневой директории.\n')   

    def delete_file():
        '''Удаление файла по имени'''
        name = str(input('Введите название файла для удаления: '))
        try:    
            os.remove(os.path.join(pwd, name))
            print('Файл удален.\n')
        except Exception:
            print('Неверное название папки или папка вне корневой директории.\n')

    def make_file():
        '''Создание файла '''
        name = str(input('Введите название файла для создания: '))
        try:
            file = open(os.path.join(pwd, name), "w")
            print('Файл создан.\n')  
        except Exception:
            print('Неверное название папки или папка вне корневой директории.\n')    

    def write_file():
        '''Запись в файл '''
        name = str(input('Введите название файла для записи: '))
        text = str(input('Введите текст который нужно записать: '))
        try:
            file = open(os.path.join(pwd, name), "w")
            file.write(f"{text}")
            print('Текст записан.\n')  
        except Exception:
            print('Неверное название папки или папка вне корневой директории.\n') 

    def change_dir():
        '''Смена директории '''
        pr = str(input('Введите директорию.'))
        os.chdir(os.path.join(pwd, pr))
        print("Текущая директория изменилась на folder:", os.getcwd())

    match num:

        case 1:
            make_dir()
            starts()
        
        case 2:
            delete_dir()
            starts()

        case 3:
            remove_file()
            starts()

        case 4:
            rename_file()
            starts()

        case 5:
            make_file()
            starts()

        case 6:
            delete_file()
            starts()

        case 7:
            write_file()
            starts()

        case 8:
            change_dir() 
            starts()

        case 9:
            sys.exit()

    
starts()


