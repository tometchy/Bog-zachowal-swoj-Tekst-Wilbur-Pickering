#!/usr/bin/env sh

set -eu

IMAGE_NAME="bog-zachowal-swoj-tekst-builder"
REPO_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

podman build --tag "$IMAGE_NAME" --file "$REPO_DIR/Dockerfile" "$REPO_DIR"

podman run \
    --rm \
    --userns=keep-id \
    --volume "$REPO_DIR:/workspace:Z" \
    --workdir /workspace \
    "$IMAGE_NAME" \
    sh -c 'make pdf && make epub && make html && make docx'
