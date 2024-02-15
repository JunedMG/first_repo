from configparser import ConfigParser


config = ConfigParser()
config.read('config.properties')


name = config.get('details', 'name')
email = config.get('details', 'email')


print(f'Hi there, my name is {name} and emaid id is {email}')
