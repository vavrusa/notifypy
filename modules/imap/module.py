#!/usr/bin/env python
# -*- coding: utf-8 -*-
import email, email.header
from modules import BaseModule
import gprowl

def decode_header(raw):
   h = email.header.decode_header(raw)[0]
   if h[1] != None:
      return h[0].decode(h[1])

   return h[0]

''' IMAP module.
    Notifies of new messages.
    '''
class Module (BaseModule, gprowl.GmailIdleNotifier):

   name = 'IMAP'

   def __init__(self, config, notificator):
      BaseModule.__init__(self, config, notificator)
      gprowl.GmailIdleNotifier.__init__(self)

   def start(self):
      BaseModule.start(self)

   def load(self):
      gprowl.GmailIdleNotifier.start(self)

   def unload(self):
      pass

   ''' Do not use. '''
   def getProwlApiKey(self):
      pass

   def getGmailUserName(self):
      gprowl.username = self.config.get('Module/IMAP', 'user')

   def getGmailPassword(self):
      gprowl.password = self.config.get('Module/IMAP', 'password')

   def sendProwlMessage(self, message):

      ''' Decode message '''
      mail = email.message_from_string(message)
      mfrom = decode_header(mail['From']).encode('utf-8')
      msubj = decode_header(mail['Subject']).encode('utf-8')

      ''' Parse format '''
      text = self.config.get('Module/IMAP', 'text')
      text = text.replace('%from', mfrom)
      text = text.replace('%subject', msubj)
      text = text.replace('%body', '')
      self.notificator.notify(self.config.get('Module/IMAP', 'name'), text)
