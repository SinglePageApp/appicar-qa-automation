import json
from pydal import DAL, Field


CONFIG = json.loads(open('config.json').read())
URI = '{engine}://{host}:{port}/{name}'
db = DAL(URI.format(**CONFIG['DB']))

from automation.data.Model import Model
