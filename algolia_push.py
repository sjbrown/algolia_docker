#! /usr/bin/env python3

import os
import sys
import json
from algoliasearch.search_client import SearchClient

client = SearchClient.create(
    os.environ['ALGOLIA_ID'],
    os.environ['ALGOLIA_ADMIN_KEY'],
)

#                        INDEX NAME HERE
index = client.init_index('test_index')

objList = json.load(open(sys.argv[1], 'rb'))

index.save_objects(objList)
