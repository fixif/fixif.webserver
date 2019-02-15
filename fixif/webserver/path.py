# -*- coding: utf-8 -*-

"""This file contains the paths used for the FiXiF server

"""

from pkg_resources import resource_filename

# Paths
class Config:
	"""simple class to store the config"""
	cache = ''          # will be filled by runServer and the config given
	generated = ''      # same
	views = resource_filename('fixif.webserver', 'views/')
	baseURL = ''        # same
	templates = resource_filename('fixif.webserver', 'templates/')
