'''
Created on 18/10/2012

@author: marco.lovato
'''


class Transactor():
    last_transaction = None

    def append_transaction(self, line, datafile='data.html'):
        self.last_transaction = line
        return True

    def get_last_transaction(self, datafile='data.html'):
        return self.last_transaction

    def remove_last_transaction(self, datafile='data.html'):
        return "removed"

if __name__ == "__main__":
    pass
