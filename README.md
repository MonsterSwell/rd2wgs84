Translates Rijksdriehoekscoordinaten to WGS84
Uses transformation formulae provided in Transformatieformules.pdf (from dekoepel.nl)
Specifically, formula 6 and table 4 from the pdf is used.



>>> martinitoren = [ 233883.131, 582065.167 ]
>>> coords = RD_to_WGS84(martinitoren[0], martinitoren[1])
>>> print "Martinitoren : %s, %s" % (coords[0], coords[1])
>>> Martinitoren : 53.219383167, 6.56820052908

Made by: Henkjan Faber (henkjan.faber@blue-chips.nl)

