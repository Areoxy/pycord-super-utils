from setuptools import setup

f = open("README.md", "r")
README = f.read()

setup(
    name="pycordSuperUtils",
    packages=["pycordSuperUtils"],
    package_data={
        "pycordSuperUtils.assets": ["*"],
        "": ["*.png", "*.ttf"],
        "pycordSuperUtils.music": ["*"],
        "pycordSuperUtils.music.lavalink": ["*"],
    },
    include_package_data=True,
    version="0.3.1",
    license="MIT",
    description="A fork of discordSuperUtils to easily develop discord Bots with pycord",
    long_description=README,
    long_description_content_type="text/markdown",
    author="koyashie07, adam7100 and Areo",
    url="https://github.com/areoxy/pycord-super-utils",
    download_url="https://github.com/areoxy/pycord-super-utils/archive/refs/tags/v0.3.1.tar.gz",
    keywords=[
        "discord",
        "easy",
        "pycord",
        "music",
        "download",
        "links",
        "images",
        "videos",
        "audio",
        "bot",
        "paginator",
        "economy",
        "reaction",
        "reaction roles",
        "database",
        "database manager",
    ],
    install_requires=[
        "py-cord",
        "Pillow",
        "requests",
        "spotipy",
        "aiosqlite",
        "motor",
        "aiopg",
        "aiomysql",
        "discord_components",
        "pytz",
        "wavelink",
        "youtube_dl",
    ],
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
)
