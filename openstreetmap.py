from tilecloud.layout.template import TemplateTileLayout
from tilecloud.store.url import URLTileStore


tile_store = URLTileStore([TemplateTileLayout('http://%s.tile.openstreetmap.org/%%(z)d/%%(x)d/%%(y)d.png' % server) for server in 'abc'], content_type='image/png')
