import configparser

def read_config(section, key):
    config = configparser.ConfigParser()
    config.read('../ConfigurationFiles/Config.cfg')
    return config.get(section, key)

def get_element_locator(section, key):
    config = configparser.ConfigParser()
    config.read('../ConfigurationFiles/Elements.cfg')
    return config.get(section, key)
