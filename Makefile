# SPDX-License-Identifier: Apache-2.0

OUTPUTS = urdf/upkie.urdf

all: $(OUTPUTS)

clean:
	rm -f $(OUTPUTS)

urdf/%.urdf: xacro/%.xacro
	python scripts/xacro_to_urdf.py $< $@
