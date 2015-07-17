set foreign_key_checks = 0;

drop table /*! if exists */ phones;

create table phones (
  id                integer unsigned  not null  primary key ,
  party_id          integer unsigned  not null,
  phone_type_id     integer unsigned  not null,
  number            varchar(255)      ,
  prime             integer unsigned  ,
  
  created           datetime          not null ,
  last_updated      timestamp         not null 
        default current_timestamp on update current_timestamp ,

  foreign key (party_id) references parties (id),
  foreign key (phone_type_id) references phone_types (id)

) 
engine InnoDB default charset=utf8;
;

load data local infile 'data/phones.csv' into table phones
fields terminated by ',' optionally enclosed by '"' ignore 1 lines;

show count(*) warnings;
show warnings;

set foreign_key_checks = 1;

select * from phones;
