import configparser

def read_config(section, key) -> str:
   config = configparser.ConfigParser()
   config.read('test_config.ini')
   return config[section][key]