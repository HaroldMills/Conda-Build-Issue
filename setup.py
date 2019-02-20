from setuptools import find_packages, setup


setup(
    name='conda_build_issue',
    version='2.0.0',
    description='Conda build issue',
    author='Harold Mills',
    author_email='harold.mills@gmail.com',
    packages=find_packages(),
    install_requires=['pysoundfile'],
    entry_points={'console_scripts': ['hello=conda_build_issue.hello:main']},
    zip_safe=False
)
