#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:19:52 2026

@author: diegoalvarez
"""

import numpy as np
import pandas as pd

class LinearModel:
    
    def __init__(self) -> None: 
        pass
    
    def get_linear_coefs(self, R: pd.DataFrame, F: pd.DataFrame) -> tuple:
        
        X = (np.column_stack([
            np.ones(len(F)),
            F.to_numpy()]))

        coef  = np.linalg.lstsq(X, R.to_numpy(), rcond = None)[0]
        alpha = coef[0 , :]
        B     = coef[1:, :].T
        
        return alpha, B