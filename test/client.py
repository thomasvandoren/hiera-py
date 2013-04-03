#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Verify hiera.HieraClient class."""

from   __future__ import print_function, unicode_literals

import mock
import subprocess
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

    @mock.patch.object(hiera.HieraClient, '_command')
    @mock.patch('subprocess.check_output')
    def test_hiera(self, mock_sub, mock_command):
        """Verify hiera returns output of subprocess command when successful."""
        h = self.create_client('my-config.yml')
        mock_sub.return_value = 'some-value'

        actual_value = h._hiera('some-key')

        self.assertEqual('some-value', actual_value)
        mock_sub.assert_called_once_with(mock_command.return_value,
                                         stderr=subprocess.STDOUT)

    @mock.patch('subprocess.check_output')
    def test_hiera__whitespace(self, mock_sub):
        """Verify hiera strips whitespace from suprocess output when successful."""
        h = self.create_client('my-config.yml')
        mock_sub.return_value = '  \t\n\r\nsome-value   '

        actual_value = h._hiera('some-key')

        self.assertEqual('some-value', actual_value)

    @mock.patch('subprocess.check_output')
    def test_hiera__missing_hiera(self, mock_sub):
        """Verify HieraNotFoundError is raised when hiera binary is not found."""
        h = self.create_client('my-config.yml')
        mock_sub.side_effect = OSError('kaboom!')

        with self.assertRaises(hiera.exc.HieraNotFoundError):
            h._hiera('some-key')

    @mock.patch('subprocess.check_output')
    def test_hiera__failed(self, mock_sub):
        """Verify HieraError raised when hiera subprocess command fails."""
        h = self.create_client('my-config.yml')
        mock_sub.side_effect = subprocess.CalledProcessError(
            1, ['command here'], output=None)

        with self.assertRaises(hiera.exc.HieraError):
            h._hiera('some-key')

    @mock.patch('subprocess.check_output')
    def test_hiera__empty(self, mock_sub):
        """Verify None is returned when hiera output is empty string."""
        h = self.create_client('my-config.yml')
        mock_sub.return_value = ''

        actual_value = h._hiera('some-key')

        self.assertIsNone(actual_value)

    def test_command(self):
        """Verify command returns expected list."""
        h = self.create_client('my-config.yml')
        expected_command = ['hiera', '--config', 'my-config.yml', 'some-key']

        actual_command = h._command('some-key')

        self.assertEqual(expected_command, actual_command)

    def test_command__environment(self):
        """Verify command includes environment list."""
        env = {'environment': 'unittest',
               'fqdn'       : 'ima-superstar',
               }
        h = self.create_client('my-config.yml', **env)
        expected_command = ['hiera', '--config', 'my-config.yml', 'some-key',
                            'environment=unittest', 'fqdn=ima-superstar']

        actual_command = h._command('some-key')

        self.assertEqual(expected_command, actual_command)
