set foreign_key_checks = 0;
 
drop table /*! if exists */ party_disciplines;

create table party_disciplines (
    id             integer unsigned  not null auto_increment primary key,
    party_id       integer unsigned  not null,
    discipline_id  integer unsigned  not null,

    created        datetime          not null,
    last_updated   timestamp         not null 
         default current_timestamp on update current_timestamp,

    foreign key (party_id) references parties (id),
    foreign key (discipline_id) references disciplines (id)
)
engine InnoDB default charset=utf8;
;

source data/insert_party_disciplines.sql;

show count(*) warnings;
show warnings;

set foreign_key_checks = 1;

select * from party_disciplines;


