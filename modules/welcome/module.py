#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules import BaseModule
import socket, datetime

''' Welcome module.
    Sends message on load.
    '''
class Module (BaseModule):
 
   name = 'Welcome'

   def load(self):
      dt = datetime.datetime.now()
      text = self.config.get('Module/Welcome', 'text')
      text = text.replace('%name', socket.gethostname())
      text = text.replace('%now', dt.strftime('%d.%m. %H:%M'))
      self.notificator.notify(self.config.get('Module/Welcome', 'name'),
		              text)

   def unload(self):
      pass


