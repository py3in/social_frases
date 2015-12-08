#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals # Tenho dúvidas se necessário.
#
#title           : frases_curtas.py 
#description     : This script will make scraping the web 
#                : for use in social networks
#author          : @Py3in 
#date start      : 20151113
#last update     : by github
#version         : 0.2 alfa     
#usage           : python frases_curtas.py --help 
#notes           : Install python 2.7+ for to use this script.
#python_version  : 2.7.6 - (default, Jun 22 2015, 17:58:13) 
import re
import random
from time import sleep

try:
    from splinter import Browser
except ImportError:
    print('please, install splinter\npip install splinter')
try:
    from lxml import html
except ImportError:
    print('please, install lxml\npip install lxml')

# Global vars temporary... future via argparse 

# in future via argparse 
url_start = "http://pensador.uol.com.br/frases_curtas/"

# In future via argparse 
prefix_file_tmp = "fc_tmp_"

# Global counter on clicks
last_visit = 0 

# Attention: Max limit counter clicks for tests. 
# Move none when in production 
max_clicks = 10 


# Zero left for compose file temp. 
# Warning for your site > 1000 page clicks...
def zero_left(last_visit):

    z = "0000" + str(last_visit)
    zl = z[-4:]
    return zl

# Security use: Random sleep for new click (defaut 3, 15)
r_min = 3  # in future via argparse 
r_max = 15 # in future via argparse
def random_click():

    _r = random.randint(r_min, r_max)
    sleep(_r)
    end_sleep = "Return of sleep " 
    return end_sleep

def save_next_page_clicked(last_visit,browser.html):
    file_grv = prefix_file_tmp+zero_left(last_visit)+".html"
    file_tmp = browser.html.encode('utf8')
    f = open(file_grv, 'wb')
    f.write(file_tmp) 
    f.close()
    

with Browser() as browser:
    browser.visit(url_start)
    snpc = save_next_page_clicked(last_visit,browser.html)

    # Aqui vai entrar o while. 
    # Ainda estudando como dividir as etapas abaixo em funções. 

    last_visit = last_visit + 1  
    print last_visit 
    print " vou dormir " 
    next_click = random_click()
    print str(next_click)

    link_found = browser.find_link_by_partial_text('Próxima')
    link_found.first.click()
    file_grv = prefix_file_tmp+zero_left(last_visit)+".html"
    file_tmp = browser.html.encode('utf8')
    f = open(file_grv, 'wb')
    f.write(file_tmp) 
    f.close()
    last_visit = last_visit + 1  
    print last_visit 
    print " vou dormir " 
    next_click = random_click()
    print str(next_click)
    link_found = browser.find_link_by_partial_text('Próxima')
    link_found.first.click()
    file_grv = prefix_file_tmp+str(last_visit)+".html"
    file_tmp = browser.html.encode('utf8')
    f = open(file_grv, 'wb')
    f.write(file_tmp) 
    f.close()
    last_visit = last_visit + 1  
