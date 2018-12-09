# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 17:05:22 2018

@author: pasca
"""

import logging
import logging.config

# This logger has a custom level that is always active by having a level above
# critical (level 50)
RESULT_LEVELV_NUM = 51 
logging.addLevelName(RESULT_LEVELV_NUM, "RESULT")
def result(self, msg, *args, **kws):
    if self.isEnabledFor(RESULT_LEVELV_NUM):
        self._log(RESULT_LEVELV_NUM, msg, args, **kws)

# Add function to scopes logging library        
logging.Logger.result= result