'''
Created on 18/10/2012

@author: marco.lovato
'''

import shutil
#import ConfigParser


class Transaction:
    date = None
    value = None
    description = None
    tags = None
    account = None
    type = ""
    pending = ""

    def __init__(self, date, value, description, tags, account, type, pending):
#        print date
#        print value
#        print description
#        print tags
#        print account
#        print type
#        print pending
        self.date = date
        self.value = value
        self.description = description
        self.tags = tags
        self.account = account
        if type == "minus":
            self.type = "-"
        if pending == "yes":
            self.pending = "?"

    def get_formatted(self):
        return self.date + self.pending + "\t" + self.pending + self.value + "\t" + self.description + "\t" + self.tags + "\t" + self.account + "\t"


class Transactor:
    last_transaction = None
    mml_folder = None
    datafile = None
    datafile_size = 0

    def set_datafile(self, datafile):
        import os.path
        self.datafile = os.path.join(self.mml_folder, datafile)
        self._count_lines()

    def set_mml_folder(self, folder):
        self.mml_folder = folder
        self.set_datafile('data.html')

    def append_transaction(self, newline):
        import os
        self.last_transaction = newline

        shutil.copy(self.datafile , self.datafile + '.new')
        with open(self.datafile + '.new') as infile:
            with open(self.datafile, "w") as outfile:
                for i, line in enumerate(infile):
                    if i == self.datafile_size - 1:
                        outfile.write(newline + "\n")
                    outfile.write(line)
            #shutil.move(self.datafile + '.new', self.datafile)
            os.remove(self.datafile + '.new')
        return True

#    def append_transaction(self, line):
#        self.last_transaction = line
#        with open(self.datafile, "a") as myfile:
#            myfile.write('\n' + self.last_transaction)
#        return True

    def get_last_transaction(self):
        return self.last_transaction

    def remove_last_transaction(self):
        return "removed"

    def _count_lines(self):
        self.datafile_size = sum(1 for line in open(self.datafile))


class MML_parser:
    _favorecidos = []
    _categories = []
    _accounts = []
    _file_data = None
    _datafile = None

    def _load_file_data(self):
        with open(self._datafile) as infile:
            self._file_data = infile.readlines()

    def _parse_favorecidos(self):
        self._favorecidos = None

    def _parse_accounts_categories(self):
        self._categories = []
        self._accounts = []
        for line in self._file_data:
            if 'valor inicial\t' in line:
                try:
                    lixo, valid_data = line.split('valor inicial\t')
                    valid_data = valid_data[:-1]
                    if valid_data.startswith("\t"):
                        valid_data = valid_data[1:]
                        self._accounts.append(valid_data)
                    if valid_data.endswith("\t"):
                        valid_data = valid_data[:-1]
                        self._categories.append(valid_data)
                except:
                    pass

    def __init__(self, datafile):
        self._datafile = datafile
        self._load_file_data()
        self._parse_accounts_categories()
        self._parse_favorecidos()

    def get_favorecidos(self):
        return sorted(self._favorecidos)

    def get_categories(self):
        return sorted(self._categories)

    def get_accounts(self):
        return sorted(self._accounts)


if __name__ == "__main__":
    mmlp = MML_parser('U:\Marco\mymoneylog\data.html')
    print mmlp.get_accounts()
    print mmlp.get_categories()
