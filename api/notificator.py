#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lib

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
         proto = lib.loadClass('api.%s' % api, '%s.API' % api, BaseAPI)
         obj =  proto(self.cfg)
         self.list.append(obj)
         return obj

      except ImportError:
         print '[!!] %s not found.' % api
         return None
      except TypeError:
         print '[!!] %s doesn\'t inherit BaseAPI' % api
         return None

   ''' Notify loaded APIs.
       @param name Message sender.
       @param text Message text.
       @param service Service ID
       '''
   def notify(self, name, text, service = None):
      for api_obj in self.list:
         api_obj.notify(name, text, service)

