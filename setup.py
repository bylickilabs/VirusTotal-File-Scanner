from setuptools import setup, find_packages

setup(
    name="VirusTotal-File-Scanner",
    version="1.0.0",
    author="Thorsten Bylicki",
    author_email="bylicki@mail.de",
    description="A local GUI application for scanning files using the VirusTotal API",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bylickilabs/VirusTotal-File-Scanner",
    project_urls={
        "Bug Tracker": "https://github.com/bylickilabs/VirusTotal-File-Scanner/issues",
        "Documentation": "https://github.com/bylickilabs/VirusTotal-File-Scanner/wiki",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.31.0",
        "PySimpleGUI>=4.60.5",
        "python-dotenv>=1.0.1",
        "tqdm>=4.66.1",
        "babel>=2.14.0",
        "qrcode>=7.4.2",
        "Pillow>=10.3.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "vt-scanner=VirusTotal-File-Scanner.app:main",
        ],
    },
    package_data={
        "": ["*.md", "*.txt", "config/*", "assets/*"],
    },
    zip_safe=False,
)
