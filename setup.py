# -*- coding: utf-8 -*-
from distutils.core import setup
import sys


# tar無法度下傷長的檔案名，所以愛用zip
# python setup.py sdist --format=zip upload
try:
    # travis攏先`python setup.py sdist`才閣上傳
    sys.argv.insert(sys.argv.index('sdist') + 1, '--format=zip')
except ValueError:
    # 無upload
    pass

setup(
    name='KIPsupin_doc2yaml',
    packages=['詞頻doc'],
    version='0.0.1',
    description=' 教育部臺灣閩南語字詞頻調查工作資料轉換工具',
    author='薛丞宏',
    author_email='ihcaoe@gmail.com',
    url='https://github.com/sih4sing5hong5/KIPsupin_doc2yaml',
    download_url='https://github.com/sih4sing5hong5/KIPsupin_doc2yaml',
    keywords=['詞頻', '臺語', ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
    install_requires=[
        'beautifulsoup4',
        'lxml',
    ],
      scripts=['詞頻doc/轉換doc到json']
)
