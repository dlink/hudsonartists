from vlib import db
from vlib.datatable import DataTable

from datarecord import DataRecord

class Parties(DataTable):

    def __init__(self):
        self.db = db.getInstance()
        DataTable.__init__(self, self.db, 'parties')

class Party(DataRecord):

    def __init__(self, party_id):
        self.db = db.getInstance()
        DataRecord.__init__(self, self.db, 'parties', party_id)
