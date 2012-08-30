# -*- coding: utf-8 -*-
#
import sys
import os

from fastkml import kml
from fastkml.geometry import Polygon, MultiPolygon

import pygeoif

try:
    from shapely.geometry.polygon import orient
except ImportError:
    from pygeoif.geometry import orient


def convert(infilename, outfilename=None):
    def convert_polygons(feature):
        if getattr(feature, 'geometry', None):
            if isinstance(feature.geometry, Polygon):
                feature.geometry = orient(feature.geometry, 1.0)
            elif isinstance(feature.geometry,  MultiPolygon):
                polys = []
                for p in feature.geometry.geoms:
                    polys.append(orient(p, 1.0))
                mp = MultiPolygon(polys)
                feature.geometry = mp
        if getattr(feature, 'features', None):
            for f in feature.features():
                convert_polygons(f)
    # main #
    (fname, ext) = os.path.splitext(infilename)
    srcfile = open(infilename, 'r')
    src = kml.KML()
    src.from_string(srcfile.read())
    for feature in src.features():
        convert_polygons(feature)
    xml = '<?xml version="1.0" encoding="UTF-8"?>' + src.to_string()
    if outfilename == None:
        outfilename = fname + '-new.kml'
    out = open(outfilename, 'w')
    out.write(xml)
    out.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        convert(sys.argv[1])
    elif len(sys.argv) == 3:
        convert(sys.argv[1], sys.argv[2])
    else:
        print 'Usage:'
        print 'kml_to_kml <filename> [outputname]'
        print 'converts the kml <filename> into a kml [outputname]'
