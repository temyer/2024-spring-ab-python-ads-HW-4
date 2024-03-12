CREATE EXTENSION IF NOT EXISTS plpython3u;

create table if not exists osm_record(
    id bigserial primary key,
    city varchar(255) not null,
    year int not null,
    tree_count int not null
);