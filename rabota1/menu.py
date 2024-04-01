import configparser
root_dir = str(input('Задайте корневую папку: '))
config = configparser.ConfigParser()

config.add_section('Settings')
config.set('Settings', 'root', root_dir)

with open('config.ini', 'w') as config_file:
    config.write(config_file)

config.read('config.ini')
