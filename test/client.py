#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Verify hiera.HieraClient class."""

from   __future__ import print_function, unicode_literals

import mock
import unittest
import uuid

import hiera
import hiera.exc


class HieraClientTests(unittest.TestCase):
    __doc__

    def create_client(self, *args, **kwargs):
        """Helper to create a new hiera client.

        By default, patches _validate function so a non-existent config file may
        be used.

        :param patch_validate: bool optional switch to enable _validate patching
        :rtype: :class:`hiera.HieraClient`
        """
        patch_validate = kwargs.pop('patch_validate', True)
        if patch_validate:
            with mock.patch.object(hiera.HieraClient, '_validate'):
                return hiera.HieraClient(*args, **kwargs)
        else:
            return hiera.HieraClient(*args, **kwargs)

    def test_init(self):
        """Verify init with default params is successful."""
        h = self.create_client('my-config.yml')
        self.assertEqual('my-config.yml', h.config_filename)
        self.assertEqual('hiera', h.hiera_binary)
        self.assertEqual({}, h.environment)

    def test_init__environment(self):
        """Verify init stores all extra keyword arguments as environment variables."""
        expected_env = {'environment': 'unittest',
                        'host'       : 'ima-superstar',
                        'random_key' : 'these-flashing-lights-are-bright!',
                        }
        h = self.create_client('my-config.yml',
                               environment='unittest',
                               host='ima-superstar',
                               random_key='these-flashing-lights-are-bright!')
        self.assertEqual(expected_env, h.environment)

    def test_init__nonexistent_config(self):
        """Verify HieraError is raised when config file does not exist."""
        with self.assertRaises(hiera.exc.HieraError):
            self.create_client('/path/to/a/fake/config/{0}'.format(uuid.uuid4()),
                               patch_validate=False)

    def test_repr(self):
        """Simple smoke test that verifies __repr__ is not busted."""
        h = self.create_client('my-config.yml')
        self.assertIsNotNone(str(h))

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
