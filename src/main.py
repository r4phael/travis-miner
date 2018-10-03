from optparse import OptionParser
import travis_miner

# Create the CLI parser
usage = "usage: %prog [options] arg"
parser = OptionParser()

# Add the available options to the parser
parser.add_option("-i", "--input_path", dest="input_path",  help="Path to the input file with projects")
parser.add_option("-o", "--output_path", dest="output_path", help="Path to the output file")

# Parse the CLI args
(options, args) = parser.parse_args()

# options.output_path = '/home/r4ph/PycharmProjects/travis-miner/data/'
# options.input_path = '/home/r4ph/PycharmProjects/travis-miner/data/projects.csv'

miner = travis_miner.TravisMiner(options.input_path, options.output_path)
miner.collect_projects()





