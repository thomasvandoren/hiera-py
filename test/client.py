#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Verify hiera.HieraClient class."""

from   __future__ import print_function, unicode_literals

import mock
import unittest

import hiera


class HieraClientTests(unittest.TestCase):
    __doc__

    def test_init(self):
        """Verify init with default params is successful."""
        self.fail('no')

    def test_init__environment(self):
        """Verify init stores all extra keyword arguments as environment variables."""
        self.fail('no')

    def test_init__nonexistent_config(self):
        """Verify HieraError is raised when config file does not exist."""
        self.fail('no')

    def test_repr(self):
        """Simple smoke test that verifies __repr__ is not busted."""
        self.fail('no')

    def test_hiera(self):
        """Verify hiera returns output of subprocess command when successful."""
        self.fail('no')

    def test_hiera__whitespace(self):
        """Verify hiera strips whitespace from suprocess output when successful."""
        self.fail('no')

    def test_hiera__missing_hiera(self):
        """Verify HieraNotFoundError is raised when hiera binary is not found."""
        self.fail('no')

    def test_hiera__failed(self):
        """Verify HieraError raised when hiera subprocess command fails."""
        self.fail('no')

    def test_hiera__empty(self):
        """Verify None is returned when hiera output is empty string."""
        self.fail('no')
