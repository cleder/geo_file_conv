# -*- coding: utf-8 -*-
#
import sys
import pygeoif
from fastkml import kml
import shapefile

def convert(infilename, outfilename='doc.kml', namecolumn=0):
    sf = shapefile.Reader(infilename)
    k = kml.KML()
    doc = kml.Document(name=infilename)
    k.append(doc)
    for sr in sf.shapeRecords():
        if sr.shape.points:
            pm = kml.Placemark(name=unicode(sr.record[namecolumn]),
                    description= "test")
            if not hasattr(sr.shape, '__geo_interface__'):
                import ipdb; ipdb.set_trace()

            pm.geometry = pygeoif.as_shape(sr.shape)
            doc.append(pm)
            if  sr.shape.__geo_interface__ != pygeoif.as_shape(sr.shape).__geo_interface__:
                #import ipdb; ipdb.set_trace()
                print sr.record
                print len(sr.shape.__geo_interface__['coordinates']),  len(pygeoif.as_shape(sr.shape).__geo_interface__['coordinates'])
                print sr.shape.__geo_interface__['type'],  pygeoif.as_shape(sr.shape).__geo_interface__['type']
                #for i in range(0,len(sr.shape.__geo_interface__['coordinates'])):
                #    print sr.shape.__geo_interface__['coordinates'][i] == pygeoif.as_shape(sr.shape).__geo_interface__['coordinates'][i]



    xml = '<?xml version="1.0" encoding="UTF-8"?>' + k.to_string()
    #try:
    #    xml = xml.decode('utf-8', 'ignore')
    #except:
    #    pass
    #xml =  xml.encode('utf-8')
    out = open(outfilename, 'w')
    out.write(xml)
    out.close()



if __name__ == "__main__":
    if len(sys.argv) == 2:
        convert(sys.argv[1])
    elif len(sys.argv) == 3:
        convert(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        convert(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    else:
        print 'Usage:'
        print 'shp_to_kml <filename> [outputname] [column number from which to extract the name]'
        print 'converts the shapefile <filename> into a KML File'

