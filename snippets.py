"""Snippets app based on Snippely Air app database"""

from os import environ
import psycopg2
import psycopg2.extras
import urlparse
from collections import namedtuple

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict


def get_groups():
    '''
    groups = OrderedDict()
    conn = sqlite3.connect('data/application.db')
    conn.row_factory = row_factory
    db = conn.cursor()
    grps = db.execute('select name,id from groups').fetchall()
    grps.sort()
    for grp in grps:
        titles = db.execute('select id, title from snippets where group_id=?', (grp.id,)).fetchall()
        alltitles = {}
        for each in titles:
            snips = db.execute('select content from snips where snippet_id=?', (each.id,)).fetchall()
            alltitles[each.title] = snips
        groups.update({grp.name: alltitles})
    conn.close()
    return groups
    '''
    groups = OrderedDict()
    conn = psycopg2.connect("dbname='snippets-heroku' user='chris' host='localhost'")
    db = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    db.execute("""select name, id from groups""")
    grps = db.fetchall()
    #grps.sort()
    for grp in grps:
        db.execute("""select id, title from snippets where group_id={}""".format(grp['id']))
        titles = db.fetchall()
        alltitles = {}
        for each in titles:
            db.execute("""select content from snips where snippet_id={}""".format(each['id']))
            snips = db.fetchall()
            alltitles[each['title']] = snips
        groups.update({grp['name']: alltitles})
    conn.close()
    return groups


def get_content():
    '''
    conn = sqlite3.connect('data/application.db')
    conn.row_factory = row_factory
    db = conn.cursor()
    content = db.execute('select * from snips').fetchall()
    conn.close()
    return content
    '''
    #conn = psycopg2.connect("dbname='snippets-heroku' user='chris' host='localhost'")

    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ['DATABASE_URL'])
    conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname))

    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("""select * from snips""")
    rows = cur.fetchall()
    conn.close()
    return rows
