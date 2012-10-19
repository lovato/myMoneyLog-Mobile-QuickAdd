'''
Created on 18/10/2012

@author: marco.lovato
'''
import cherrypy
import os.path
import ConfigParser

_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
_cherryconf = os.path.join(_curdir, 'cherrypy.conf')
_appconf = os.path.join(_curdir, 'app.conf')


class Root(object):
    def index(self):
        return "<html><body><a href='/oi'>oi</a></body></html>"
    index.exposed = True


class AddEntry(object):
    def index(self):
        return "Era isso!"
    index.exposed = True


def create_appconf_file():
    config = ConfigParser.RawConfigParser()
    config.add_section('global')
    config.set('global', 'sync_folder', 'C:\YourSyncFolder')
    with open(_appconf, 'wb') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    config = ConfigParser.RawConfigParser()
    config.read(_appconf)
    sync_folder = config.get('global', 'sync_folder')

#    application_conf = {
#        '/style.css': {
#        'tools.staticfile.on': True,
#        'tools.staticfile.filename': os.path.join(_curdir,
#        'style.css'),
#        }
#        }

    cherrypy.config.update(_cherryconf)

    cherrypy.tree.mount(Root(), "", "")
    cherrypy.tree.mount(AddEntry(), "/add", "")

    cherrypy.engine.start()
    cherrypy.engine.block()
