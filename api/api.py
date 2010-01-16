#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback

# API base
class BaseAPI:

   _config = None

   def __init__(self, config):
      self.config = config
      return

   def notify(self, name, text, service = 0):
      return False

   def config(self):
      return self._config

''' API Loader
  Create and register API.
  @param name API identifier string, ex. 'boxcar'.
  @param config Configuration. '''
def load(api, config):
   try:
      print ' * %s' % api
      module = getattr(__import__('api.%s' % api), api)
      proto = getattr(module, 'API')
      if not issubclass(proto, BaseAPI):
         print '[!!] API \'%s\' does not inherit BaseAPI.'
         raise ImportError
      return proto(config)

   except ImportError:
      print '[!!] API \'%s\' not found.' % api
      traceback.print_exc()
      return None



