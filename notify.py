#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser, os
import api, modules

# Defaults
config_path = '~/.notifypy.cfg'

# Read configuration
header = 'NotifyPy (configuration: %s)' % config_path
print header
print ''.center(len(header), '-')
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
api_list = cfg.get('Global', 'api').split(' ')
print 'Loading APIs (%s) ...' % ' '.join(api_list)
notificator = api.Notificator(cfg)
for api_id in api_list:
   notificator.load(api_id)

# Load modules
mod_list = cfg.get('Global', 'modules').split(' ')
print 'Loading modules (%s) ...' % ' '.join(mod_list)
manager = modules.Manager(cfg, notificator)
for mod_id in mod_list:
   manager.load(mod_id)

# Run modules
print 'Running %i modules.' % len(manager.list)
manager.run()
