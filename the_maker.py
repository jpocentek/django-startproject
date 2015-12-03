# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys

CONFIG_FILES = ('.gitignore', 'setup.py', 'settings.py',)


def run(project_name):
    """
    Replace every placeholder name with actual project name given by user. It
    should be used only once, upon project creation. This file is invoked in
    installation script.
    """
    for root, path, files in os.walk(os.getcwd()):
        for fname in files:
            if fname in CONFIG_FILES:
                with open(os.path.join(root, fname), 'r') as f:
                    data = f.read().replace('{{ PROJECT_NAME }}', project_name)
                with open(os.path.join(root, fname), 'w') as f:
                    f.write(data)


if __name__ == '__main__':
    name = sys.argv[1]
    run(name)
