import setuptools

setuptools.setup(
    name='pyperclip-termux',
    version='0.0.1',
    description='pyperclip patch for termux-api',
    long_description=open('README.md').read().strip(),
    author='BlackCatDevel0per',
    author_email='bcdev@mail.ru',
    url='https://github.com/kittyandrew/pyperclip-termux',
    packages=setuptools.find_packages(),
    install_requires=['pyperclip'],
    license='Apache 2.0',
    keywords='pyperclip termux',
    classifiers=[
        "Development Status :: 4 - Beta",
    ],
    python_requires='>=3.6',
)
