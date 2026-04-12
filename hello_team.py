team_members = [] #d453fbe1-5bd8-4ce3-a358-48970a6672f5
with open('README.MD', "r", encoding='utf8') as f: #d453fbe1-5bd8-4ce3-a358-48970a6672f5
    for line in f.readlines(): #d453fbe1-5bd8-4ce3-a358-48970a6672f5
        if line[0] == '@': #d453fbe1-5bd8-4ce3-a358-48970a6672f5
            print(f'Hello, Dear teammate {line[1:].strip('\n')}!') #d453fbe1-5bd8-4ce3-a358-48970a6672f5
