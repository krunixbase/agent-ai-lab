#!/bin/bash

set -e

echo "Creating snapshot for version v1.0.0..."

# Create directory structure
mkdir -p versions/v1/docs/architecture

# List of root-level files to copy
FILES=(
  "ARCHITECTURE.md"
  "ARCHITECTURE_DIAGRAM.md"
  "SYSTEM_DESIGN.md"
  "INDEX.md"
  "GLOSSARY.md"
  "GOVERNANCE_MODEL.md"
  "RISK_MODEL.md"
  "SECURITY_MODEL.md"
  "ROADMAP.md"
  "RELEASE_NOTES.md"
)

echo "Copying root-level documentation files..."

for FILE in "${FILES[@]}"; do
  if [ -f "$FILE" ]; then
    cp "$FILE" versions/v1/
    echo "✔ Copied $FILE"
  else
    echo "⚠ Warning: $FILE not found, skipping."
  fi
done

echo "Copying full architecture documentation (12 layers)..."

if [ -d "docs/architecture" ]; then
  cp -R docs/architecture/* versions/v1/docs/architecture/
  echo "✔ Architecture folder copied"
else
  echo "⚠ Warning: docs/architecture/ not found!"
fi

echo "Snapshot created successfully!"
echo "Location: versions/v1/"
