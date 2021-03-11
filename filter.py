import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-w', '--wordlist', dest='wordlist', help='Full path for the original wordlist')
    parser.add_option('-o', '--output', dest='output', help='Location of filtered wordlist')
    parser.add_option('-m', '--mask', dest='mask', help="The mask for the filter(Syntax => ?d?l?u?s).\nd => digit\nw => lowercase letters\nu => uppercase letters\ns => symbols")

    (options, _ ) = parser.parse_args()

    if not options.wordlist:
        parser.error('[-] wordlist is not given --help for more information')
    if not options.output:
        parser.error('[-] output location is not given --help for more information')
    if not options.mask:
        parser.error('[-] mask for filter is not given --help for more information')


    return options.wordlist, options.output, options.mask

lists = {
    'd' = list('0123456789'),
    'l' = list('abcdefghijklmnopqrstuvwxyz'),
    'l' = list('abcdefghijklmnopqrstuvwxyz'.upper()),
    's' = list('!@#$%^&*()')
}

