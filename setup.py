from distutils.core import setup

setup(
    name='gdax-client',
    version='1.0.0',
    packages=[
        'gdax_client',
    ],
    url='https://github.com/captain13128/gdax-client',
    license='',
    author='',
    author_email='',
    description='',
    install_requires=[
        "websocket-client==0.46.0",
        "sortedcontainers==2.1.0",
    ]
)
