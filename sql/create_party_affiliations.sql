set foreign_key_checks = 0;
 
drop table /*! if exists */ party_affiliations;

create table party_affiliations (
    id             integer unsigned  not null primary key,
    party_id       integer unsigned  not null,
    affiliation_id integer unsigned  not null,

    created        datetime          not null,
    last_updated   timestamp         not null 
         default current_timestamp on update current_timestamp,

    foreign key (party_id)       references parties(id),
    foreign key (affiliation_id) references parties(id)
)
engine InnoDB default charset=utf8;
;

load data local infile 'data/party_affiliations.csv' into table party_affiliations
fields terminated by ',' optionally enclosed by '"' ignore 1 lines;

show count(*) warnings;
show warnings;

set foreign_key_checks = 1;

select * from party_affiliations;


