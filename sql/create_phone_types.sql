set foreign_key_checks = 0;
 
drop table /*! if exists */ phone_types;

create table phone_types (
    id             integer unsigned  not null primary key,
    code           varchar(15)       not null,
    name           varchar(45)       not null,
    description    varchar(255)      ,
    active         integer unsigned  not null,

    created        datetime          not null,
    last_updated   timestamp         not null 
         default current_timestamp on update current_timestamp,

    unique key codes (code)
)
engine InnoDB default charset=utf8;
;

load data local infile 'data/phone_types.csv' into table phone_types
fields terminated by ',' optionally enclosed by '"' ignore 1 lines;

show count(*) warnings;
show warnings;

set foreign_key_checks = 1;

select * from phone_types;


