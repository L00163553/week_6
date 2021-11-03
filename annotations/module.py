"""
# 
# File          : module.py
# Created       : 01/11/21 11:13 AM
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""


class Module:
    """module class where module name and id"""

    module_name: str

    def __init__(self, name):
        self.module_name = name
