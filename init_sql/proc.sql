create or replace FUNCTION most_freq_city() RETURNS varchar(255) AS $$
q = plpy.prepare("""
    select
    	city,
        count(id) as c
    from osm_record
    group by city
    order by c desc
    limit 1;
""")

result = plpy.execute(q)
return result[0]["city"]

$$ LANGUAGE plpython3u;
