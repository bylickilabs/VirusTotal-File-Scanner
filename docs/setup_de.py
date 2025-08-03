from setuptools import setup, find_packages

setup(
    name="virustotal_scanner_gui",
    version="1.0.0",
    author="Thorsten Bylicki",
    author_email="bylicki@mail.de",
    description="Lokale GUI-Anwendung zur Dateiprüfung über die VirusTotal API",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bylickilabs/virustotal-scanner",
    project_urls={
        "Bug Tracker": "https://github.com/bylickilabs/virustotal-scanner/issues",
        "Documentation": "https://github.com/bylickilabs/virustotal-scanner/wiki",
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
            "vt-scanner=virustotal_scanner_gui.app:main",
        ],
    },
    package_data={
        "": ["*.md", "*.txt", "config/*", "assets/*"],
    },
    zip_safe=False,
)
