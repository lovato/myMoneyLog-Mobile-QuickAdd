'''
Created on 18/10/2012

@author: marco.lovato
'''
#pylint: disable-msg=R0903,R0201
import cherrypy
import os.path
import ConfigParser
from mml_datafile_helper import Transactor, Transaction, Mmlparser
from jinja2 import Environment, FileSystemLoader

_CURDIR = os.path.join(os.getcwd(), os.path.dirname(__file__))
_CHERRYCONF = os.path.join(_CURDIR, 'cherrypy.conf')
_APPCONF = os.path.join(_CURDIR, 'app.conf')
ENV = Environment(loader=FileSystemLoader('templates'))


class Root(object):
    '''
    Root
    '''
    def index(self):
        '''
        index
        '''
        tmpl = ENV.get_template('root.html')
        mml = Mmlparser(os.path.join(get_mml_folder(), 'data.html'))
        return tmpl.render(accounts=mml.get_accounts(),
                           categories=mml.get_categories())
    index.exposed = True


class AddEntry(object):
    '''
    AddEntry
    '''
    def index(self, date=None, account=None, description=None, value=None,
              tags=None, transaction_type=None, transaction_pending=None):
        '''
        @param date:
        @param account:
        @param description:
        @param value:
        @param tags:
        @param transaction_type:
        @param transaction_pending:
        '''
        transaction = Transaction(date, value, description, tags, account,
                                  transaction_type, transaction_pending)
        transactor = Transactor()
        transactor.set_mml_folder(get_mml_folder())
        transactor.append_transaction(transaction.get_formatted())
        #return 'OK'
        raise cherrypy.HTTPRedirect("/feedback")
    index.exposed = True


class UserFeedback(object):
    '''
    UserFeedback
    '''
    def index(self):
        '''
        index
        '''
        tmpl = ENV.get_template('feedback.html')
        return tmpl.render(feedback_message = "Trasa&ccedil;&atilde;o adicionada")
    index.exposed = True


def create_appconf_file():
    '''
    create_appconf_file
    '''
    config = ConfigParser.RawConfigParser()
    config.add_section('global')
    config.set('global', 'mml_folder', r'C:\YourMMLFolder')
    with open(_APPCONF, 'wb') as configfile:
        config.write(configfile)


def get_mml_folder():
    '''
    get_mml_folder
    '''
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

    cherrypy.engine.start()
    cherrypy.engine.block()
