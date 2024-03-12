import requests

from src.open_street_map.exceptions import CityNotFoundException, OSMException


class OSM:
    OSM_URL = "http://overpass-api.de/api/interpreter"

    def get_tree_count(self, year: int, city: str) -> int:
        data = """
            [out:json][date:'%s-01-01T00:00:00Z'][maxsize:1073741824];
            area["name:en"="%s"]->.a;
            (node["natural"="tree"](area.a););
            out count;
        """ % (
            str(year),
            city,
        )

        result = requests.post(OSM.OSM_URL, data=data, timeout=60)
        result.raise_for_status()

        body = result.json()

        elements = body["elements"]

        if not elements:
            raise OSMException(body["remark"])

        total = elements[0]["tags"]["total"]

        if total == "0":
            raise CityNotFoundException(f"Provided city cannot be found: {city}")

        return total
