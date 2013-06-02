import db_upsert
import github
import rethinkdb as r
import sys


if __name__ == "__main__":
    conn = r.connect()
    conn.use("vim_awesome")

    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = None

    for repo in github.scrape_vim_scripts(num):
        print "Scraped", repo['name']
        db_upsert.upsert_plugin(conn, repo)