#!/bin/sh
# Simple start script used by some PaaS providers
exec gunicorn -w 4 -b 0.0.0.0:3000 app:app
