with open('reddit_links.txt') as result:
        uniqlines = set(result.readlines())
        with open('reddit_links_no_dupes.txt', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))