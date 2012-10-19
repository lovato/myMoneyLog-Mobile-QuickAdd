'''
Created on 18/10/2012

@author: marco.lovato
'''
import cherrypy, os.path
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))

class Dummy():
    def dummyfunc(self,param):
        return param
    
class Root:
    def index(self):
        return "Hello, world!"
    index.exposed = True
    
class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

if __name__ == "__main__":
    # Use the configuration file tutorial.conf.
    
    global_conf = {
        'global': {
        'server.socket_host': 'localhost',
        'server.socket_port': 8080,
        },
        }
    application_conf = {
        '/style.css': {
        'tools.staticfile.on': True,
        'tools.staticfile.filename': os.path.join(_curdir,
        'style.css'),
        }
        }
    
    cherrypy.config.update(global_conf)
    cherrypy.root = Root()
    cherrypy.server.start()