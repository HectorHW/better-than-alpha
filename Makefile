FILES=pack.png pack.txt terrain.png
.PHONY: build-xcf
build-xcf:
	cat build.gs | gimp -n -i -b -

.PHONY: pack
pack:
	zip alphacolors.zip $(FILES)

.PHONY: build
build: buid-xcf pack
