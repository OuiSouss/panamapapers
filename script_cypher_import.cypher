//create Intermediairies

using periodic commit
load csv with headers from
'file:///Intermediaries.csv' as csv

create (:Intermediary:Global{name:csv.name, internal_id:csv.internal_id,address:csv.address,valid_until:csv.valid_until,country_codes:csv.country_codes,countries:csv.countries,status:csv.status,node_id:toInt(csv.node_id),sourceID:csv.sourceID});



//create Addresses

using periodic commit
load csv with headers from
'file:///Addresses.csv' as csv

create (:Address:Global{address:csv.address, icij_id:csv.icij_id,valid_until:csv.valid_until,country_codes:csv.country_codes,countries:csv.countries,node_id:toInt(csv.node_id),sourceID:csv.sourceID,note:csv.note});


//create Entities
using periodic commit
load csv with headers from
'file:///Entities.csv' as csv
create (:Entity:Global{name:csv.name,original_name:csv.name,former_name:csv.former_name,jurisdiction:csv.juridisdiction,jurisdiction_description:csv.jurisdiction_description,company_type:csv.company_type,address:csv.address,internal_id:csv.internal_id,incorporation_date:csv.incorporation_date,inactivation_date:csv.inactivation_date,struck_off_date:csv.struck_off_date,dorm_date:csv.dorm_date,status:csv.status,service_provider:csv.service_provider,ibcRUC:csv.ibcRUC,country_codes:csv.country_codes,countries:csv.countries,note:csv.note,valid_until:csv.valid_until,node_id:toInt(csv.node_id),sourceID:csv.sourceID});



//create Officers

using periodic commit
load csv with headers from
'file:///Officers.csv' as csv
create (:Officer:Global{name:csv.name, icij_valid:csv.icij_valid,valid_until:csv.valid_until,country_codes:csv.country_codes,countries:csv.countries,node_id:toInt(csv.node_id),sourceID:csv.sourceID,note:csv.note});

create index on :Global(node_id);

create constraint on (o:Intermediary) assert o.node_id is unique;
create constraint on (o:Address) assert o.node_id is unique;
create constraint on (o:Entity) assert o.node_id is unique;
create constraint on (o:Officer) assert o.node_id is unique;
