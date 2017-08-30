import json
from RiotAPI import RiotAPI

def main():
    api = RiotAPI('RGAPI-c37da3d7-1f4f-4a31-8e3f-2e948759ba54')

    summ = api.get_summoner_by_name('dyrus')
    parsed_summ = json.dumps(summ, indent=4)

    print parsed_summ
    print summ['id'], summ['name']

    rmatch = api.get_recent_matches(summ['accountId'])
    parsed_rmatch = json.dumps(rmatch, indent=4)
    print parsed_rmatch

if __name__ == "__main__":
    main()
