#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:38:39 2020

@author: hassan
"""

from django.urls import path
from .views import store,cart,checkout,update_item,process_order

name = 'store'
urlpatterns =[
        path('',store,name='store'),
        path('cart/',cart,name='cart'),
        path('checkout/',checkout,name='checkout'),
        path('update_item/',update_item,name='update_item'),
        path('process_order/',process_order,name='process_order'),
        
        ]