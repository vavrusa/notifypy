#!/usr/bin/env python
from threading import Thread

''' Base class for modules.
    '''
class BaseModule (Thread):

   config = None
   notificator = None

   ''' Initialize. '''
   def __init__(self, config, notificator):
      self.config = config
      self.notificator = notificator
      Thread.__init__(self)

   ''' Run module (Thread proxy). '''
   def run(self):
      self.load()

   ''' Load module. '''
   def load(self):
      return False

   ''' Unload module. '''
   def unload(self):
      return False

