from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from ...models import Game
import ast

def convert_release_date(epoch):
    return datetime.fromtimestamp(epoch / 1000 + 1).strftime('%Y')

class Command(BaseCommand):
    args = ''
    help = 'Update Game Database'
    def handle(self, *args, **options):
        from igdb_api_python.igdb import igdb
        igdb = igdb('0cc499afcdb8b8076835350cd909f9f1')
        result = igdb.platforms({
            'ids': '6',
            'fields': 'games'
        })
        games = ast.literal_eval(result.content)
        games = [str(g) for g in games[0]['games']]

        i = 0
        content = []
        while i < 1000:
            result = igdb.games({
                'ids': games[i + 1:min(i + 1000, 23769)],
                'fields': ['name', 'first_release_date', 'url', 'cover', 'summary'],
            })
            content += (ast.literal_eval(result.content))
            i += 1000

        Game.objects.all().delete()
        for game in content:
            try:
                game['year'] = convert_release_date(game['first_release_date'])
                g = Game(id=game['id'], name=game['name'], year=game['year'], url = game['url'])
            except KeyError:
                g = Game(id=game['id'], name=game['name'], url = game['url'])
            try:
                if game['cover']['url'][0] == 'h':
                    g.cover_url = game['cover']['url'].replace('t_thumb','t_cover_big')
                else:
                    g.cover_url = 'https:' + game['cover']['url'].replace('t_thumb','t_cover_big')

            except KeyError:
                pass
            try:
                g.summary=game['summary']
            except KeyError:
                pass
            g.save()