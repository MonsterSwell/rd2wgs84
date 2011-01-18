Translates Rijksdriehoekscoordinaten to WGS84
====================
Uses transformation formulae provided in Transformatieformules.pdf (from dekoepel.nl)
Specifically, formula 6 and table 4 from the pdf is used.

Usage:
---------------------
    > python rd2wgs84.py 233883.131 582065.167 #coordinates of martinitoren
    [53.219383166978588, 6.5682005290780019]

    > python convertgeojson.py foo.geo.json #geojson file with rijksdriehoekscoordinaten
    wgs84.foo.geo.json

Originally made by: Henkjan Faber (henkjan.faber@blue-chips.nl)
geojson converter by Kilian Valkhof

