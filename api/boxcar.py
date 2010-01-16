#!/usr/bin/env python
# -*- coding: utf-8 -*-
from api import BaseAPI
import urllib, urllib2

''' Boxcar Growl API
'''
class API (BaseAPI):

   requester = None

   def __init__(self, config):
      ''' Parent init '''
      BaseAPI.__init__(self, config)

      ''' Initialize AUTH handler '''
      pmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
      pmgr.add_password(None,
                        self.config.get('API/Boxcar', 'url'),
                        self.config.get('API/Boxcar', 'user'),
                        self.config.get('API/Boxcar', 'password'))
      ah = urllib2.HTTPBasicAuthHandler(pmgr)
      self.requester = urllib2.build_opener(ah)

   def notify(self, name, text, service = None):

      ''' Build POST query '''
      data = { 'notification[from_screen_name]' : name,
               'notification[message]' : text }
      if service is not None:
         data['notification[from_remote_service_id]'] = service

      ''' Encode data and send notification. '''
      data = urllib.urlencode(data)
      page = self.requester.open(self.config.get('API/Boxcar', 'url'), data)
      return True
