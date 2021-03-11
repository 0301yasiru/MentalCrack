# create a program to port forward

from termcolor import colored
from itertools import chain, combinations, product
from functools import partial
from datetime import datetime

indexes = [i for i in range(20)]

char_ch = {
        'a' : ['a','@'],
        'o' : ['o', 'O'],
        'l' : ['l', '!', 'i', '1'],
        'i' : ['i', '!', 'l', '1'],
        'A' : ['a','@'],
        'O' : ['o', 'O'],
        'L' : ['l', '!', 'i', '1'],
        'I' : ['i', '!', 'l', '1'],
    }

def print_logo(location = 'logo.txt'):
    with open(location, 'r') as logo:
        for line in logo.readlines():
            print(line)

def powerset(set_):
    s = list(set_)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def capitalize(s, ind):
    split_s = list(s)
    for i in ind:
        try:
            split_s[i] = split_s[i].upper()
        except IndexError:
            pass
    return "".join(split_s)

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def replace_itter(original, replacement, indexes):
  for i, index in enumerate(indexes):
    original[index] = replacement[i]
  return original

def get_letter_combination(key_):
  change_lets = []

  key_flip_supset = list(powerset(char_ch.keys()))[1:]
  for sub_flip_comb in key_flip_supset:
      temp_key = list(key_)

      for master in sub_flip_comb:

          if master in temp_key:
              slaves = char_ch[master]
              indexes = find(key_, master)
              possible_replacements  = list(product(slaves, repeat=len(indexes)))[1:]

              for replacement in possible_replacements:
                temp_key = replace_itter(temp_key, replacement, indexes)
                change_lets.append("".join(temp_key))

  return list(set(change_lets))

def run_single_word_posibilities(key):
    posibilities = []

    # make posiible uppercases
    for subset in powerset(indexes[:len(key)]):
        key_ = capitalize(key, subset)
        posibilities.append(key_)

    # make possible letter changes
    pre_length = len(posibilities)
    for key_ in posibilities[:pre_length]:
        posibilities.extend(get_letter_combination(key_))
    
    # make first three letters
    pre_length = len(posibilities)
    for key_ in posibilities[:pre_length]:
        for length in range(1,len(key_) - 1):
            if key_[:length] not in posibilities[pre_length:]:
                posibilities.append(key_[:length])
    
    return posibilities


def func(list_, joiner): 
    return joiner.join(list_)

def get_list_combinations(a,b,joiners, sufficses):
    huge_data = []
    for suffix in sufficses:
        for joiner in joiners:
            data  = list(map(partial(func, joiner = joiner), list(product(a,b))))
            huge_data.extend(list(map(lambda string : string + suffix, data)))
    return huge_data
            
print_logo()

keys      = input("Enter Keywords about the target -> ").replace(' ', '').split(',')
joiners   = [''] + input("Enter joinerds between keys     -> ").replace(' ', '').split(',')
sufficses = [''] + input("Enter possible suffixes         -> ").replace(' ', '').split(',')

# generate all lists for keywords
counter = 0
start_time = datetime.now()
print('[+] Paswords are generating!!')

with open('wordlist.txt', 'w') as output:
    lists = []
    for key in keys:
        s = run_single_word_posibilities(key)
        #output.write('\n'.join(s))
        #output.write('\n')
        for suffix in sufficses:
            output.write('\n'.join(list(map(lambda string : string + suffix, s))))
            output.write('\n')
            counter += len(s)

        lists.append(s)


    permutations = list(product( indexes[:len(lists)], repeat = 2 ))
    for p in permutations:
        str_ = get_list_combinations(lists[p[0]], lists[p[1]], joiners, sufficses)
        counter += len(str_)
        output.write('\n'.join(str_))
        output.write('\n')

print('[+] Done password generating')
print('[*] Time Took     -> {} secs'.format((datetime.now() - start_time).seconds))
print('[*]Password count -> {}'.format(counter))

#keys = input().strip().replace(" ", '').split(',')