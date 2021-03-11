def print_logo(location = 'logo.txt'):
    with open(location, 'r') as logo:
        for line in logo.readlines():
            print(line)

print_logo()