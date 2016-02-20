set foreign_key_checks = 0;

drop table /*! if exists */ addresses;

create table addresses (
  id                integer unsigned  not null auto_increment primary key,
  party_id          integer unsigned  not null,
  address1          varchar(255)      ,
  address2          varchar(255)      ,
  city              varchar(255)      ,
  state             varchar(255)      ,
  zipcode           varchar(10)       ,
  prime             integer unsigned  ,
  
  created           datetime          not null ,
  last_updated      timestamp         not null 
        default current_timestamp on update current_timestamp ,

  foreign key (party_id)  references parties (id)
) 
engine InnoDB default charset=utf8;
;

create trigger addresses_create before insert on addresses
   for each row set new.created = now()
;

load data local infile 'data/addresses.csv' into table addresses
fields terminated by ',' optionally enclosed by '"' ignore 1 lines;

show count(*) warnings;
show warnings;

set foreign_key_checks = 1;

select * from addresses;
