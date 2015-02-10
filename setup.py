from setuptools import setup

setup(name='cylon.py',
      version='0.0.1',
      description='Next generation project-cylon',
      url='https://github.com/gigapixel/project-cylon',
      author='Peerapat S.',
      author_email='gigapixel7@gmail.com',
      license='MIT',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
      ],
      packages=['cylon'],
      entry_points={
          'console_scripts': [
          'cylon=cylon.command:main', 'behack=cylon.behack:main'
      ]},
      install_requires=[
          'pyyaml',
          'behave',
          'selenium'
      ],
      zip_safe=False)
