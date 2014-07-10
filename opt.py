
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-f','--file',dest='filename', help='write repirt to FILE', metavar='FILE')
parser.add_option('-q','--quiet',
        action='store_false', dest='verbose', default=True, help="don t print status message to stdout")

(options, args) = parser.parse_args()
if options.filename:
    print "you file:", options.filename
if options.verbose:
    print "you verbose:", options.verbose

