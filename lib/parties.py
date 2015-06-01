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


        # pull out discipline data from record
        disciplines = _removeDiscipline(record)

        # create parties record
        for k,v in record.items():
            if k == 'party_type':
                record2.party_type_id = self.partyTypes.getId(v)
            else:
                record2[k] = v
        party_id = self.insertRow(record2)

        # create party discipline records
        Party(party_id).updateDisciplines(disciplines)

        return 'Party record created: %s' % party_id

    @lazyproperty
    def partyTypes(self):
        return Attributes(self.db, 'party_types', 'id')

class Party(DataRecord):

    def __init__(self, party_id):
        self.db = db.getInstance()
        DataRecord.__init__(self, self.db, 'parties', party_id)

        self.party_id = party_id

    def update(self, data):

        disciplines = _removeDiscipline(data)

        if data:
            self.setFilters('id=%s' % self.party_id)
            self.updateRows(data)

        self.updateDisciplines(disciplines)

        return 'Party record updated: %s' % self.party_id

    def updateDisciplines(self, discipline_list):

        # check if anything changed:
        if set(discipline_list) == set(self.disciplines):
            return 0

        # Init Datatables:
        partyDisciplines = DataTable(self.db, 'party_disciplines')
        disciplines      = Attributes(self.db, 'disciplines', 'id')

        # remove all disciplines for this party
        partyDisciplines.setFilters({'party_id': self.party_id})
        partyDisciplines.deleteRows()

        # add list of disciplines
        for discipline in discipline_list:
            discipline_id = disciplines.getId(discipline)
            record = odict(party_id=self.party_id,
                           discipline_id=discipline_id,
                           created=datetime.now())
            partyDisciplines.insertRow(record)
        return 1

    @lazyproperty
    def disciplines(self):
        pd = DataTable(self.db,
                       'disciplines d '
                       'join party_disciplines pd on pd.discipline_id = d.id '
                       'join parties p on pd.party_id = p.id')
        pd.setColumns('d.code');
        pd.setFilters({'party_id': self.party_id})
        self.data['disciplines'] = [r['code'] for r in pd.getTable()]
        return self.data['disciplines']

    @lazyproperty
    def affiliations(self):
        pa = DataTable(self.db, 'party_affiliations pa join parties a on pa.affiliation_id = a.id')
        pa.setColumns('a.company');
        pa.setFilters('party_id = %s' % self.party_id)
        self.data['affiliations'] = [r['company'] for r in pa.getTable()]
        return self.data['affiliations']

    # Reference Tables:

    @lazyproperty
    def partyDisciplines(self):
        return DataTable(self.db, 'party_disciplines')

    @lazyproperty
    def partyAffiliations(self):
        return DataTable(self.db, 'party_affiliations')

    @lazyproperty
    def disciplineDt(self):
        return DataTable(self.db, 'disciplines')

def _removeDiscipline(record):
    if 'discipline' in record:
        disciplines = record['discipline'].split(',')
        del record['discipline']
    else:
        disciplines = []
    return disciplines
