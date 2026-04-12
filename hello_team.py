team_members = []
with open('README.MD', "r", encoding='utf8') as f:
    for line in f.readlines():
        if line[0] == '@':
            print(f'Hello, Dear teammate {line[1:].strip('\n')}!')
