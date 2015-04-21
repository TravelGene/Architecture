import os
from setuptools import setup


LONG_DESC = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


setup(name='scrapy-redis',
      version='0.5.1',
      description='Redis-based components for Scrapy',
      long_description=LONG_DESC,
      author='Rolando Espinoza La fuente',
      author_email='',
      url='',
      packages=['scrapy_redis'],
      license='BSD',
      install_requires=['Scrapy>=0.14', 'redis>=2.4'],
      classifiers=[
          'Programming Language :: Python',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
      ],
     )

