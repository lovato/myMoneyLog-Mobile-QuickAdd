'''
Created on 18/10/2012

@author: marco.lovato
'''
#pylint: disable-msg=R0903,R0201
import shutil
import os.path
import re


class Transaction:
    '''
    class
    '''
    date = None
    value = None
    description = None
    tags = None
    account = None
    signal = ""
    pending = ""

    def __init__(self, date, value, description, tags,
                 account, signal, pending):
        '''
        @param date:
        @param value:
        @param description:
        @param tags:
        @param account:
        @param signal:
        @param pending:
        '''
        self.date = date
        self.value = value
        self.description = description
        self.tags = tags
        self.account = account
        if signal == "minus":
            self.signal = "-"
        if pending == "yes":
            self.pending = "?"

    def get_formatted(self):
        '''
        get_formatted
        '''
        result = self.date + self.pending + "\t"
        result = result + self.signal + self.value + "\t"
        result = result + self.description + "\t" + self.tags + "\t"
        result = result + self.account
        return result


class Transactor:
    '''
    class
    '''
    last_transaction = None
    mml_folder = None
    datafile = None
    datafile_size = 0

    def __init__(self):
        pass

    def set_datafile(self, datafile):
        '''
        @param datafile:
        '''
        self.datafile = os.path.join(self.mml_folder, datafile)
        self._count_lines()

    def set_mml_folder(self, folder):
        '''
        @param folder:
        '''
        self.mml_folder = folder
        self.set_datafile('data.html')

    def append_transaction(self, newline):
        '''
        @param newline:
        '''
        self.last_transaction = newline

        shutil.copy(self.datafile, self.datafile + '.tmp')
        with open(self.datafile + '.tmp') as infile:
            with open(self.datafile, "w") as outfile:
                for i, line in enumerate(infile):
                    if i == self.datafile_size - 1:
                        outfile.write(newline + "\n")
                    outfile.write(line)
            #shutil.move(self.datafile + '.new', self.datafile)
            infile.close()
            outfile.close()
            os.remove(self.datafile + '.tmp')
        self._count_lines()
        infile.close()
        outfile.close()
        return True

    def get_last_transaction(self):
        '''
        get_last_transaction
        '''
        with open(self.datafile, "r") as infile:
            for i, line in enumerate(infile):
                if i == self.datafile_size - 2:
                    self.last_transaction = line
        infile.close()
        return self.last_transaction

    def remove_last_transaction(self):
        '''
        remove_last_transaction
        '''
        return False

    def _count_lines(self):
        '''
        _count_lines
        '''
        if not os.path.exists(self.datafile):
            with open(self.datafile, 'w') as outfile:
                outfile.write('<html>\n</html>')
                outfile.close()
        self.datafile_size = sum(1 for line in  # @UnusedVariable
                                 open(self.datafile, 'r'))
        return self.datafile_size


class Mmlparser:
    '''
    class
    '''
    _favorecidos = []
    _categories = []
    _accounts = []
    _file_data = None
    _datafile = None

    def _load_file_data(self):
        '''
        _load_file_data
        '''
        with open(self._datafile) as infile:
            self._file_data = infile.readlines()


    # def _parse_datafile(self):
    #     '''
    #     _parse_favorecidos
    #     '''
    #     self._categories = []
    #     self._accounts = []
    #     for line in self._file_data:
    #         if 'valor inicial\t' in line:
    #             valid_data_array = line.split('valor inicial\t')
    #             valid_data = valid_data_array[1]
    #             valid_data = valid_data[:-1]
    #             if valid_data.startswith("\t"):
    #                 valid_data = valid_data[1:]
    #                 self._accounts.append(valid_data)
    #             if valid_data.endswith("\t"):
    #                 valid_data = valid_data[:-1]
    #                 self._categories.append(valid_data)
    #         else:
    #             self._favorecidos.append(line)

    def _parse_datafile(self):
        '''
        _parse_favorecidos
        '''
        self._categories = []
        self._accounts = []
        for line in self._file_data:
            if '\t' in line:
                line_elements = line.split('\t')
                if line_elements[2] == 'valor inicial':
                    if line_elements[3] == '':
                        self._accounts.append(line_elements[4][:-1])  # just to remove trailing n\
                    else:
                        self._categories.append(line_elements[3])
                else:
                    self._favorecidos.append(line_elements[2])
        self._accounts = set(self._accounts)
        self._categories = set(self._categories)
        self._favorecidos = set(self._favorecidos)

    def __init__(self, datafile):
        '''
        @param datafile:
        '''
        self._datafile = datafile
        self._load_file_data()
        self._parse_datafile()
        self._fix_favorecidos()

    def _fix_favorecidos(self):
        _favorecidos = []
        for item in self._favorecidos:
            parsed_item = re.sub(r' \d+/\d+$', r'', item)
            parsed_item = parsed_item.split('-')[0].strip()
            _favorecidos.append(parsed_item)
        self._favorecidos = set(_favorecidos)

    def get_favorecidos(self):
        '''
        get_favorecidos
        '''
        return sorted(self._favorecidos)

    def get_categories(self):
        '''
        get_categories
        '''
        return sorted(self._categories)

    def get_accounts(self):
        '''
        get_accounts
        '''
        return sorted(self._accounts)


if __name__ == "__main__":
#    MMLP = Mmlparser(r'U:\Marco\mymoneylog\data.html')
    MMLP = Mmlparser(r'C:\Users\user\Dropbox\mymoneylog\data.html')
    print MMLP.get_accounts()
    print MMLP.get_categories()
    print MMLP.get_favorecidos()