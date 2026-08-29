#!/usr/bin/env sh

set -eu

IMAGE_NAME="bog-zachowal-swoj-tekst-builder"
REPO_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

if [ "$#" -gt 1 ]; then
    echo "Usage: $0 [repo_dir]" >&2
    exit 1
fi

if [ "$#" -eq 1 ]; then
    if [ ! -d "$1" ]; then
        echo "Error: repository directory does not exist: $1" >&2
        exit 1
    fi

    REPO_DIR=$(CDPATH= cd -- "$1" && pwd)
fi

podman build --tag "$IMAGE_NAME" --file "$REPO_DIR/Dockerfile" "$REPO_DIR"

podman run \
    --rm \
    --userns=keep-id \
    --volume "$REPO_DIR:/workspace:Z" \
    --workdir /workspace \
    "$IMAGE_NAME" \
    sh -c 'make pdf && make epub && make html && make docx'
