# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:26:07 2018

@author: pasca
"""

from src import model
from mcptools.maas import logging

logging.config.fileConfig('src/logging.ini')
#%%

logger=logging.getLogger(__name__)
logger.debug('Starting execution')
model.run()
