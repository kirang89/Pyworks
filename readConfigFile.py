from configobj import ConfigObj

config = ConfigObj('configuration.ini')
print "Name: " + config.get('name')
print "Age: " + config.get('age')

