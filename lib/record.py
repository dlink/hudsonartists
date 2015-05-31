from vlib.datatable import DataTable
from vlib.odict import odict

DEBUG = 0

class RecordError(Exception): pass

class Record(DataTable):
    '''Preside over a single Db Record'''

    def __init__(self, db, table, id):
        '''Create a Record Object given
              a vlib.db Object, a table name, and a record Id

           Meant to be subclassed, as follows:

           class user(Record):
              def __init__(self, id):
                 Record.__init__(db.getInstance(), 'user', id)
        '''
        self.db    = db      
        self.table = table
        self.id    = id

        DataTable.__init__(self, db, table)
        self.debug_sql = DEBUG
        self._loadData()

    def _loadData(self):
        '''Read a single Db Record and add it to self.__dict__

           So the following examples syntax will work:

             user.first_name,
             message.id
             message.created
        '''
        self.setFilters('id=%s' % self.id)
        results = self.getTable()
        if not results:
            raise RecordError('%s table: Record not found, Id: %s' %
                              (self.table.title(), self.id))

        # store data in a dictionary
        self.data = results[0]

        # store data as properties of self
        self.__dict__.update(results[0])
