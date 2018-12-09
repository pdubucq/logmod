# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:28:20 2018

@author: pasca
"""
from mcptools.maas import logging

import pandas as pd
import numpy as np

logger=logging.getLogger(__name__)

def run():
    logger.info('Starting to run')
    x=pd.DataFrame(np.random.randint(
            low=0, high=10, size=(5, 5)),
    columns=['a', 'b', 'c', 'd', 'e'])    
    logger.result('Random Matrix' + x.to_string().replace('\n',';'))
    params=pd.Series(data=[0,2,4,1,4e4], 
                     index=['test_mode', 'no. runs', 'nT', 'sdff', 'P_nom'])
    for p in params.iteritems():
        logger.result(f"{p[0]},{p[1]}")
    logger.result(f'Total result in EUR,{102e4}')
    logger.info('All done.')