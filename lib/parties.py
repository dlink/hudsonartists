from datetime import datetime

from vlib import db
from vlib.datatable import DataTable
from vlib.odict import odict
from vlib.utils import lazyproperty

from datarecord import DataRecord

from attributes import Attributes

class Parties(DataTable):

    def __init__(self):
        self.db = db.getInstance()
        DataTable.__init__(self, self.db, 'parties')

        self.party_type_id = None # This will get overwritten by subclases

    def add(self, record):
        # default record
        record2 = odict(first_name='',
                        middle_name='',
                        last_name='',
                        created=datetime.now(),
                        party_type_id=self.party_type_id)

        for k,v in record.items():
            if k == 'party_type':
                record2.party_type_id = self.partyTypes.getId(v)
            else:
                record2[k] = v
        party_id = self.insertRow(record2)
        return 'Party record created: %s' % party_id

    @lazyproperty
    def partyTypes(self):
        return Attributes(self.db, 'party_types', 'id')

class Party(DataRecord):

    def __init__(self, party_id):
        self.db = db.getInstance()
        DataRecord.__init__(self, self.db, 'parties', party_id)
