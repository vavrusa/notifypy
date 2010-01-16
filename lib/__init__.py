#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Create and register API.
    @param path Module path.
    @param cls  Class path
    @param super Superclass for validation.
    '''
def loadClass(path, cls, super = None):
   module = __import__(path)
   cls = cls.split('.')
   proto = module
   for i in cls:
      proto = getattr(proto, i)
   if not issubclass(proto, super):
      raise TypeError

   return proto
