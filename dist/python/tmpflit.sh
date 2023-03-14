#!/bin/sh
#
# Copyright 2023 Inria
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

PROJECT_NAME=upkie_description

if [ "$#" -lt 1 ]; then
    echo "usage: same as flit"
    echo ""
    echo "examples:"
    echo "  $0 build"
    echo "  $0 publish --repository testpypi"
    echo ""
    flit --help
    exit 1
fi

BASEDIR=$(dirname 0)
COMMAND=$@
SRCDIR=${BASEDIR}/../..
TMPDIR=$(mktemp -d)

echo "[debug] COMMAND=${COMMAND}"
echo "[debug] SRCDIR=${SRCDIR}"
echo "[debug] TMPDIR=${TMPDIR}"

for folder in meshes urdf; do
    mkdir -p ${TMPDIR}/${PROJECT_NAME}/$(dirname ${folder})
    cp -r ${SRCDIR}/${folder} ${TMPDIR}/${PROJECT_NAME}/${folder}
done

cp ${BASEDIR}/${PROJECT_NAME}/*.py ${TMPDIR}/${PROJECT_NAME}/
cp ${BASEDIR}/README.md ${TMPDIR}/README.md
cp ${BASEDIR}/pyproject.toml ${TMPDIR}/pyproject.toml

cd ${TMPDIR} && flit ${COMMAND}
