#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Exceptions for specific hiera issues."""

from __future__ import print_function, unicode_literals


class HieraError(Exception):
    """Generic Hiera error."""

    def __init__(self, message, returncode=None, output=None):
        """Override instance init so that return code and console output can be
        added to error.
        """
        super(HieraError, self).__init__(message)
        self.returncode = returncode
        self.output = output


class HieraNotFoundError(Exception):
    """Hiera error indicating the hiera CLI could not be found."""
    pass
