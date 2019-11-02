

zip_file_path = '/home/co/Desktop/test.zip'

from optparse import OptionParser

parser = OptionParser()
parser.add_option(
    "-f", "--file", dest=zip_file_path,
    help="write report to FILE", metavar="FILE"
)
parser.add_option(
    "-q", "--quiet",
    action="store_false", dest="verbose", default=True,
    help="don't print status messages to stdout"
)

(options, args) = parser.parse_args()
print(options,args)
