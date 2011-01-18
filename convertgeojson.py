import os
import sys
import math
import simplejson
import rd2wgs84


def convertGeoJson(filename):
    """
    Translates GeoJson files in rijksdriehoeks format to WGS84
    Assumes a valid GeoJson file
    """

    geofile = open(filename)
    jsonFile = simplejson.loads(geofile.read())

    for i in jsonFile["features"]:
        for j in i["geometry"]["coordinates"]:
            for k in j:
                if type(k[0]).__name__=='float':
                    newk = rd2wgs84.convert(k[0], k[1])
                    k[0] = newk[1]
                    k[1] = newk[0]
                else:
                    for l in k:
                        newl = rd2wgs84.convert(l[0], l[1])
                        l[0] = newl[1]
                        l[1] = newl[0]

    newGeofile = open("wgs84." + geofile.name, "w")
    newGeofile.write(simplejson.dumps(jsonFile))
    newGeofile.close()

if __name__ == "__main__":
    try:
        convertGeoJson(sys.argv[1])
    except:
      print "Please supply a (valid) file"

