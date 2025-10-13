# SPDX-License-Identifier: Apache-2.0

OUTPUTS = urdf/upkie.urdf urdf/upkie_camera.urdf

# Help snippet adapted from:
# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help:
	@grep -P '^[a-zA-Z0-9_-]+:.*? ## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "    \033[36m%-24s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: $(OUTPUTS)  ## Build all URDF files

.PHONY: clean
clean:  ## Remove URDF files
	rm -f $(OUTPUTS)

.PHONY: rebuild
rebuild: clean build  ## Rebuild all URDF files

urdf/%.urdf: xacro/%.xacro
	python scripts/xacro_to_urdf.py $< $@
