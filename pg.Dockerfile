FROM postgres:13.3
RUN apt update && apt install python3 python3-pip postgresql-plpython3-${PG_MAJOR} -y
ADD init_sql/init.sql /docker-entrypoint-initdb.d/
ADD init_sql/proc.sql /docker-entrypoint-initdb.d/
