-- 7/17/2015, Add auto_increment to address id

alter table addresses
  modify column id integer unsigned  not null auto_increment
;
