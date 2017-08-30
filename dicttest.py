import RiotConsts as Consts

def main():
    str =  Consts.URL['base'].format(
        proxy=Consts.REGIONS['north_america1'],
        url='boop'
    )

    print str

if __name__=="__main__":
    main()
