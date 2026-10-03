import sys


def load_file(file):
    d = {}
    with open(file, mode='r') as f:
        for i, line in enumerate(f):
            key = chr(32 + i // 9)
            if i % 9 == 0:
                d[key] = []
            else:
                d[key].append(line.rstrip('\n'))
    return d


def render_word(word, d):
    print('\n'.join(''.join(d[c][i] for c in word) for i in range(8)))


# Из бонусных сделал только fs.
def main():
    string = sys.argv[1]
    file = sys.argv[2] if len(sys.argv) > 2 else 'standard'
    file += '.txt'

    if string == '':
        return

    d = load_file(file)

    words = string.split('\\n')

    if all(word == '' for word in words):
        print('\n' * (len(words) - 1), end='')
        return

    for word in words:
        if word == '':
            print()
        else:
            render_word(word, d)

main()