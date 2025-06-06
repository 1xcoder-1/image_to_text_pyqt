from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-image-to-text',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='tsjoker14311211@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt GUI example of image to text using image-to-text model',
    url='https://github.com/1xcoder-1/image_to_text_pyqt.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.14',
        'transformers',
    ]
)
