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


