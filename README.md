# Better than alpha

This repository contains simple texturepack that brings old grass and other textures to minecraft. It is intended to be used on top of Better Than Adventure mod.

**I AM ASSOCIATED WITH NEITHER MOJANG NOR BETTER THAN ADVENTURE CREATORS. ALL INCLUDED RESOURCES BELONG TO APPROPRIATE COPYRIGHT HOLDERS.**

## Building

Texturepack is split into psd files for easier editing. In order to build it you will need make as well as zip to package all resources. If you are on debian-based distribution, install them with `sudo apt install gimp make zip`. You will also need [poetry](https://python-poetry.org/docs/#installation) to install python dependencies.

`cp .env.example .env` file and make changes if necessary (see `Configuration`). Install python dependencies using `poetry install`.

After installing all dependencies issue `make build` to build and package the texturepack. Alternatively, run build script direcly via `bta-build build <features>`.

In case you are making changes, you may want to define path to your minecraft's `texturepacks` folder inside `.env` via variable `BTA_TEXTUREPACK_FOLDER`. This will allow you to use `make install` to easily copy texturepack and `make all` to rebuild and copy it.

## Configuration

Provided build script allows to select which features you want included in resulting texturepack. To see all features type `bta-build list` of simply pay a visit to [features.py](buildscript/features.py). Specify individual features via `bta-build build <features>` eg `bta-build build grass stone`. If using makefile, you can change `BTA_ENABLED_FEATURES` in [`.env`](.env.example). Additionally, you can type `bta-build build all` or set `BTA_ENABLED_FEATURES=all` if using make (current default) to build with all features enabled.
