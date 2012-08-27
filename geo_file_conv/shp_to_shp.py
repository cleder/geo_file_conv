# Build a new shx index file
# Sometimes shx files become corrputed or go missing.
# You can build a new shx index using pyshp.
import os
import shapefile

def convert(infilename, outfilename=None):
    # Explicitly name the shp and dbf file objects
    # so pyshp ignores the missing/corrupt shx
    (shapeName, ext) = os.path.splitext(infilename)
    try:
        shp = open("%s.shp" % shapeName, "rb")
    except IOError:
        raise shapefile.ShapefileException("Unable to open %s.shp" % shapeName)
    try:
        dbf = open("%s.dbf" % shapeName, "rb")
    except IOError:
        raise shapefile.ShapefileException("Unable to open %s.dbf" % shapeName)
    r = shapefile.Reader(shp=shp, shx=None, dbf=dbf)
    w = shapefile.Writer(r.shapeType)
    # Copy everything from reader object to writer object
    w._shapes = r.shapes()
    w.records = r.records()
    w.fields = list(r.fields)
    # saving will generate the shx
    if outfilename == None:
        outfilename = shapeName + '-withshx'
    w.save(outfilename)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        convert(sys.argv[1])
    elif len(sys.argv) == 3:
        convert(sys.argv[1], sys.argv[2])
    else:
        print 'Usage:'
        print 'shp_to_shp <filename> [outputname]'
        print 'converts the shapefile <filename> into a shapefile with shx [outputname]'
