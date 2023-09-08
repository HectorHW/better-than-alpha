# Better than alpha

This repository contains simple texturepack that brings old grass and other textures to minecraft. It is intended to be used on top of Better Than Adventure mod.

**I AM ASSOCIATED WITH NEITHER MOJANG NOR BETTER THAN ADVENTURE CREATORS. ALL INCLUDED RESOURCES BELONG TO APPROPRIATE COPYRIGHT HOLDERS.**

## Building

Texturepack is split into xcf files for easier editing. In order to build it you will need make and gimp as well as zip to package all resources. If you are on debian-based distribution, install them with `sudo apt install gimp make zip`.

After installing all dependencies issue `make build` to build and package the texturepack.

In case you are making changes, you may want to define path to your minecraft's `texturepacks` folder inside `.env` via variable `BTA_TEXTUREPACK_FOLDER`. This will allow you to use `make install` to easily copy texturepack and `make all` to rebuild and copy it.

## Configuration

TODO - it may be possible to configure which changes to include in the future.
