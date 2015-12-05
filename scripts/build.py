#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WORK_DIR = os.path.join(BASE_DIR, 'static')

BIN_DIR = os.path.join(BASE_DIR, 'node_modules', '.bin')


def print_nice(text):
    """ Print text wrapped in some extra chars to fill standard terminal width.
    """
    print(80*"*")
    print("*{:^78}*".format(text))
    print(80*"*")


def compress_stylesheet(debug=False):
    """ Compress all less files for main stylesheet.
    """
    input_file = os.path.join(WORK_DIR, 'less', 'style.less')
    ext = 'min.css' if debug else 'css'
    output_file = os.path.join(WORK_DIR, 'dist', 'style.{}'.format(ext))
    print(input_file, '==>', output_file)
    cmd = [os.path.join(BIN_DIR, 'lessc'),]
    if debug:
        cmd.append('--clean-css')
    cmd += [input_file, output_file,]
    subprocess.call(cmd)


if __name__ == '__main__':
    print_nice("Compressing stylesheets")
    compress_stylesheet()
    compress_stylesheet(debug=True)
