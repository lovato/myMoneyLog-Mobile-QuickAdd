'''
Created on 18/10/2012

@author: marco.lovato
'''
import cherrypy
import os.path
import ConfigParser
from mml_datafile_helper import Transactor, Transaction, MML_parser
from jinja2 import Environment, FileSystemLoader

_CURDIR = os.path.join(os.getcwd(), os.path.dirname(__file__))
_CHERRYCONF = os.path.join(_CURDIR, 'cherrypy.conf')
_APPCONF = os.path.join(_CURDIR, 'app.conf')
ENV = Environment(loader=FileSystemLoader('templates'))

#class RootOld(object):
#    @cherrypy.expose
#    def index(self):
#        mmlp = MML_parser(os.path.join(get_mml_folder(), 'data.html'))
#        temp = "<html><body><form action=/add>"
#        temp = temp + 'date: <input name=date type=text><br>value: <
#input name=value type=text><br>Desc: <input name=description type=text><br>\n'
#        temp = temp + '<select name=at_account>\n'
#        for item in mmlp.get_accounts():
#            temp = temp+'<option>'+item+'</option>\n'
#        temp = temp + '</select><br>\n'
#        temp = temp + '<select name=tags>\n'
#        for item in mmlp.get_categories():
#            temp = temp+'<option>'+item+'</option>\n'
#        temp = temp+'</select><br>\n<input type=submit></form></body></html>'
#        return temp
#        #return "<html><body><a href='/add'>oi</a></body></html>"


class Root(object):
    def index(self):
        tmpl = ENV.get_template('root.html')
        mml = MML_parser(os.path.join(get_mml_folder(), 'data.html'))
        return tmpl.render(accounts=mml.get_accounts(), categories=mml.get_categories())
    index.exposed = True


class AddEntry(object):
    def index(self, date=None, account=None, description=None, value=None, tags=None, transaction_type=None, transaction_pending=None):
        transaction = Transaction(date, value, description, tags, account, transaction_type, transaction_pending)
        transactor = Transactor()
        transactor.set_mml_folder(get_mml_folder())
        transactor.append_transaction(transaction.get_formatted())
        #return 'OK'
        raise cherrypy.HTTPRedirect("/feedback")
    index.exposed = True


class UserFeedback(object):
    def index(self):
        tmpl = ENV.get_template('feedback.html')
        return tmpl.render(feedback_message = "Trasa&ccedil;&atilde;o adicionada")
    index.exposed = True

def create_appconf_file():
    config = ConfigParser.RawConfigParser()
    config.add_section('global')
    config.set('global', 'mml_folder', r'C:\YourMMLFolder')
    with open(_APPCONF, 'wb') as configfile:
        config.write(configfile)


def get_mml_folder():
    config = ConfigParser.RawConfigParser()
    config.read(_APPCONF)
    return config.get('global', 'mml_folder')

if __name__ == "__main__":
    _CHERRYAPPCONF = {
        '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(_CURDIR, 'static'),
        }
    }
    cherrypy.config.update(_CHERRYCONF)

    cherrypy.tree.mount(Root(), "", _CHERRYAPPCONF)
    cherrypy.tree.mount(AddEntry(), "/add", _CHERRYAPPCONF)
    cherrypy.tree.mount(UserFeedback(), "/feedback", _CHERRYAPPCONF)
    #cherrypy.tree.mount(Foo(), "/foo", _CHERRYAPPCONF)

    cherrypy.engine.start()
    cherrypy.engine.block()
