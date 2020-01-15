#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from datetime import datetime
from Copyright import Copyright 
class TestCopyright(unittest.TestCase):
    def test_DEFAULT_NAME(self):
        self.assertEqual('{{AuthorName}}', Copyright.DEFAULT_NAME)

    def test_Generate(self):
        self.assertEqual(
            '© {} {}'.format(datetime.now().strftime('%Y'), Copyright.DEFAULT_NAME),
            Copyright.Generate())
    def test_Generate_name_pos(self):
        name = 'MyName'
        self.assertEqual(
            '© {} {}'.format(datetime.now().strftime('%Y'), name),
            Copyright.Generate(name))
    def test_Generate_name_kw(self):
        name = 'MyName'
        self.assertEqual(
            '© {} {}'.format(datetime.now().strftime('%Y'), name),
            Copyright.Generate(name=name))
    def test_Generate_name_TypeError(self):
        with self.assertRaises(TypeError):
            Copyright.Generate(0)

    def test_init(self):
        c = Copyright()
        self.assertEqual(Copyright, type(c))
        self.assertEqual('{{AuthorName}}', c.DefaultName)
        self.assertEqual(Copyright.DEFAULT_NAME, c.DefaultName)
    def test_init_default_name_pos(self):
        def_name = 'MyDefaultName'
        c = Copyright(def_name)
        self.assertEqual(def_name, c.DefaultName)
    def test_init_default_name_kw(self):
        def_name = 'MyDefaultName'
        c = Copyright(default_name=def_name)
        self.assertEqual(def_name, c.DefaultName)
    def test_init_default_name_TypeError(self):
        with self.assertRaises(TypeError):
            c = Copyright(0)

    def test_DefaultName_set(self):
        def_name = 'MyDefaultName'
        c = Copyright()
        c.DefaultName = def_name
        self.assertEqual(def_name, c.DefaultName)
    def test_DefaultName_set_TypeError(self):
        c = Copyright()
        with self.assertRaises(TypeError):
            c.DefaultName = 0

    def test_generate(self):
        self.assertEqual(
            '© {} {}'.format(datetime.now().strftime('%Y'), '{{AuthorName}}'),
            Copyright().generate())
    def test_generate_name_pos(self):
        name = 'test_name'
        self.assertEqual(
            '© {} {}'.format(datetime.now().strftime('%Y'), name),
            Copyright().generate(name))
    def test_generate_name_kw(self):
        name = 'test_name'
        self.assertEqual(
            '© {} {}'.format(datetime.now().strftime('%Y'), name),
            Copyright().generate(name=name))
    def test_generate_name_TypeError(self):
        with self.assertRaises(TypeError):
            Copyright().generate(0)


if __name__ == '__main__':
    unittest.main()

