FILES=pack.png pack.txt terrain.png

.PHONY: build
build: build-xcf pack

.PHONY: build-xcf
build-xcf:
	cat build.gs | gimp -n -i -b -

.PHONY: pack
pack:
	zip alphacolors.zip $(FILES)






