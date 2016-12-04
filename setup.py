from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(name='asynclib',
      description='Utlity library for working with async python, including'
                  ' some stdlib replacements to be compatible with native '
                  'coroutines.',
      author='Matt Rasband, Nick Humrich',
      author_email='matt.rasband@gmail.com',
      license='Apache-2.0',
      url='https://github.com/wickedasp/asynclib',
      download_url=('https://github.com/wickedasp/asynclib'
                    '/releases/v' + __version__ + '.tar.gz'),
      keywords=(
          'asyncio',
      ),
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3 :: Only',
          'License :: OSI Approved :: Apache Software License',
          'Intended Audience :: Developers',
          'Development Status :: 2 - Pre-Alpha',
          'Topic :: Software Development',
      ],
      setup_requires=[],
      install_requires=[],
      extras_require={},
      tests_require=[],
      entry_points={},
      zip_safe=False)
