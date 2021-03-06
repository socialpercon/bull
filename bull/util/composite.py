#!/usr/bin/python  
# -*- coding: utf-8 -*-

class composite_cls():
    def __init__(self,*args):
        self.args = args

    def call(self, func,*args,**kwargs):
        for item in self.args:
            func(item,*args,**kwargs)

def composite(*args):
    return composite_cls(*args)