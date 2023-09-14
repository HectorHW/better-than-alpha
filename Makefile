include .env


.PHONY: build
build: build-pack

.PHONY: build-pack
build-pack:
	poetry run bta-build build $(BTA_ENABLED_FEATURES) | zip betterthanalpha.zip -@


.PHONY: install
install:
	cp betterthanalpha.zip ${BTA_TEXTUREPACK_FOLDER}

.PHONY: all
all: build install
