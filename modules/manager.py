#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lib
from base import *
import traceback

''' Module manager.
    '''
class Manager:

   cfg = None
   notificator = None
   list = []

   ''' Initialize.
       @param config Configuration.
       '''
   def __init__(self, config, notificator):
      self.cfg = config
      self.notificator = notificator

   ''' Deinitialize.
       '''
   def __deinit__(self):
      self.stop()

   ''' Create and register module.
       @param name Module name.
       '''
   def load(self, name):
      try:
         proto = lib.loadClass('modules.%s.module' % name,
	                       '%s.module.Module' % name,
			       BaseModule)
         obj =  proto(self.cfg, self.notificator)
         self.list.append(obj)
         return obj

      except TypeError:
         print '[!!] %s doesn\'t inherit BaseModule.' % name
	 traceback.print_exc()
	 return None

      except ImportError:
         print '[!!] %s not found.' % name
	 traceback.print_exc()
	 return None

   ''' Start loaded modules.
       '''
   def start(self):
      for mod in self.list:
         mod.start()

   ''' Stop loaded modules.
       '''
   def stop(self):
      print 'Unloading modules ...'
      for mod in self.list:
         mod.unload()

   ''' Run and wait for modules.
       '''
   def run(self):
      self.start()
      for mod in self.list:
         mod.join()
	 print 'Finished:', mod.name
