# -*- coding: utf-8 -*-

import torch
import torch.nn as nn


def fill_ninf(t):
    return t.float().fill_(float('-inf')).type_as(t)


def Linear(in_features, out_features, bias=True):
    m = nn.Linear(in_features, out_features, bias)
    nn.init.xavier_uniform_(m.weight)
    if bias:
        nn.init.constant_(m.bias, 0.)
    return m
