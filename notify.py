#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser, os
import api

# Defaults
config_path = '~/.notifypy.cfg'

# Read configuration
print 'Configuration:', config_path
cfg = ConfigParser.ConfigParser()
if len(cfg.read(os.path.expanduser(config_path))) is 0:

   # Initialize default config
   cfg.read('default.cfg')
   with open(os.path.expanduser(config_path), 'wb') as cfgout:
      cfg.write(cfgout)
   print 'Creating config \'%s\' ...' % config_path

# Check first run
if cfg.has_option('Global', 'first-run'):
   print '[!!] Please remove \'first-run\' option before use.'
   exit(1)

# Load APIs
print 'Loading APIs ...'
notificator = api.Notificator(cfg)
for api_id in cfg.get('Global', 'api').split(' '):
   notificator.load(api_id)

# Test notify
notificator.notify('autor', 'pokusna zprava')
