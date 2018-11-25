from setuptools import setup, find_packages

setup(name='donkeypart_common',
      version='0.1',
      description='donkey car part to use the pi camera',
      long_description="no long description given",
      long_description_content_type="text/markdown",
      url='https://github.com/autorope/donkeypart_picamera',
      author='Will Roscoe',
      author_email='wroscoe@gmail.com',
      license='MIT',
      install_requires=[
                        ],

      extras_require={'dev': ['pytest-cov']},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='selfdriving cars donkeycar diyrobocars datastore',
      packages=find_packages(exclude=(['tests', 'docs', 'site', 'env'])),
      )
