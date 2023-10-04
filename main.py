from github.gitController import GitHub

def main():
    rep = GitHub('rodrigo-kenji')
    print(rep.getUserInfo())

if __name__ == '__main__':
    main()
