#!/bin/bash

PACKAGE_FILES=$(find . -type f -name "*.lean" -o -name "*.toml" -o -name "*.md" -o -name "*.yaml" -o -name "*.json" -o -name "*.txt")

# tar --exclude='.lake' -czvf ZetaLogic.tar.gz Main.lean ZetaLogic.lean lakefile.toml lean-toolchain README.md ZetaLogic/
tar --exclude='.lake' -czvf ZetaLogic.tar.gz $PACKAGE_FILES
