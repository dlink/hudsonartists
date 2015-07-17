-- 7/9/2015, Fix foreign key on addresses.party_id

alter table addresses
   drop foreign key addresses_ibfk_1
;

alter table addresses
   add foreign key (party_id)  references parties (id)
;
