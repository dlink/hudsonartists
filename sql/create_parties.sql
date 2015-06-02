set foreign_key_checks = 0;

drop table /*! if exists */ parties;

create table parties (
  id                integer unsigned  not null auto_increment primary key,
  party_type_id     integer unsigned  not null ,
  first_name        varchar(255)      not null ,
  middle_name       varchar(255)      not null ,
  last_name         varchar(255)      not null ,
  company           varchar(255)      ,
  email             varchar(255)      ,
  website           varchar(255)      ,

  created           datetime          not null ,
  last_updated      timestamp         not null
	default current_timestamp on update current_timestamp ,

  unique key name (first_name, middle_name, last_name, company),
  foreign key (party_type_id)  references party_types (id)
)
engine InnoDB default charset=utf8;
;

load data local infile 'data/parties.csv' into table parties
fields terminated by ',' optionally enclosed by '"' ignore 1 lines;

show count(*) warnings;
show warnings;

set foreign_key_checks = 1;

select * from parties;
