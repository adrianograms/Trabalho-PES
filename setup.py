from distutils import setup

setup(
    name='vgit',
    version='0.1',
    description='visual git',
    license="MIT",
    author='Grams & Mulling, Inc.',
    packages=['foo'],
    install_requires=['gi', 'pygit2', 'radon', 'coverage'],
)
