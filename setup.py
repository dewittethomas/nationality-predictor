import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Thomas Dewitte",
    author_email="thomasdewittecontact@gmail.com",

    name='nationality_predictor',
    version='1.0.1',
    license="MIT",
    url='https://github.com/dewittethomas/nationality_predictor',
    python_requires='>= 3.5',
    
    description='An API for predicting nationality from a name',
    long_description=README,
    long_description_content_type="text/markdown",

    package_dir={"nationality_predictor": "nationality_predictor"},
    install_requires=["requests>=2.22.0", "pycountry>=19.8.18"],
    
    packages=setuptools.find_packages(),

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)