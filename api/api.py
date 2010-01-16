#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' API base class.
    '''
class BaseAPI:

   _config = None

   def __init__(self, config):
      self.config = config
      return

   def notify(self, name, text, service = 0):
      return False

   def config(self):
      return self._config



''' Notificator class.
    '''
class Notificator:

   cfg = None
   list = []

   ''' Initialize.
       @param config Configuration.
       '''
   def __init__(self, config):
      self.cfg = config


   ''' Create and register API.
       @param name API identifier string, ex. 'boxcar'.
       '''
   def load(self, api):
      try:
         print ' - %s' % api
         module = getattr(__import__('api.%s' % api), api)
         proto = getattr(module, 'API')
         if not issubclass(proto, BaseAPI):
            print '[!!] API \'%s\' does not inherit BaseAPI.'
            raise ImportError

         obj =  proto(self.cfg)
	 self.list.append(obj)
	 return obj

      except ImportError:
         print '[!!] API \'%s\' not found.' % api
         return None

   ''' Notify loaded APIs.
       @param name Message sender.
       @param text Message text.
       @param service Service ID
       '''
   def notify(self, name, text, service = None):
      for api_obj in self.list:
         api_obj.notify(name, text, service)
    
