# Resolve the problem!!
import re

def run():
    # Start coding here
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        cont2 = ''.join(re.findall(r'[a-z]', f.read()))
        print(cont2)

if __name__ == '__main__':
    run()
