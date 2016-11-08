#!/usr/bin/env python
# coding: utf-8
import imp
import inspect
mod_name = 'test_k_means'
mod_path = '/home/saemundur/git/scikit-learn/sklearn/cluster/tests/test_k_means.py'
try_mod = imp.load_source(mod_name,mod_path)
try_mod.gather_tests_and_run_as_one()
# mod_funcs = dict(inspect.getmembers(try_mod,inspect.isfunction))
# for key,val in mod_funcs.items():
#     if key.startswith('test_'):
#         val()