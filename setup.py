import setuptools

with open('README.md') as readme_file:
    readme = readme_file.read()

setuptools.setup(
        name='tsudo',
        python_requires='>3',
        version='0.0.4',
        author='Giovan Isa Musthofa',
        author_email='giovanism@outlook.co.id',
        description='Tsundere wrapper for sudo command.',
        long_description=readme,
        long_description_content_type='text/markdown',
        url='https://github.com/giovanism/tsudo',
        license='WTFPL',
        packages=setuptools.find_packages(),
        scripts=('scripts/tsudo',),
        install_requires=(
            'pexpect',
            ),
        classifiers=(
            'Programming Language :: Python :: 3',
            'Operating System :: Unix',
            'Environment :: Console',
            'Environment :: Plugins',
            'Topic :: System :: Systems Administration',
            ),
        )

