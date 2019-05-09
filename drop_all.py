#!/usr/bin/env python3

from eurovote import create_app
app = create_app()
app.app_context().push()

from eurovote import db
db.drop_all()
db.create_all()

print('Done.')
