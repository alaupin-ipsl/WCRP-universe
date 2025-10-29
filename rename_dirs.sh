#!/bin/bash
# Rename all directories with hyphens to underscores

BASE_DIR="${1:-/Users/daniel.ellis/WIPwork/WCRP-universe/src-data}"
DRY_RUN=false

# Parse arguments
for arg in "$@"; do
    case $arg in
        --dry-run|-n)
            DRY_RUN=true
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [directory] [--dry-run]"
            echo ""
            echo "Rename all directories with hyphens to underscores"
            echo ""
            echo "Options:"
            echo "  --dry-run, -n    Show what would be renamed without doing it"
            echo "  --help, -h       Show this help message"
            echo ""
            echo "Example:"
            echo "  $0 /path/to/dir --dry-run"
            exit 0
            ;;
    esac
done

if [[ "$DRY_RUN" == true ]]; then
    echo "🔍 DRY RUN MODE - No changes will be made"
    echo ""
fi

if [[ ! -d "$BASE_DIR" ]]; then
    echo "❌ Directory not found: $BASE_DIR"
    exit 1
fi

echo "Searching for directories with hyphens in: $BASE_DIR"
echo ""

# Find all directories with hyphens (excluding hidden dirs)
# Sort by depth (deepest first) to avoid renaming parents before children
mapfile -t DIRS < <(find "$BASE_DIR" -type d -name "*-*" ! -path "*/.*" | awk '{ print length, $0 }' | sort -rn | cut -d' ' -f2-)

if [[ ${#DIRS[@]} -eq 0 ]]; then
    echo "✅ No directories with hyphens found!"
    exit 0
fi

echo "Found ${#DIRS[@]} directories with hyphens:"
for dir in "${DIRS[@]}"; do
    rel_path="${dir#$BASE_DIR/}"
    echo "  - $rel_path"
done
echo ""

SUCCESS=0
FAILED=0
SKIPPED=0

for OLD_PATH in "${DIRS[@]}"; do
    OLD_NAME=$(basename "$OLD_PATH")
    PARENT_DIR=$(dirname "$OLD_PATH")
    NEW_NAME="${OLD_NAME//-/_}"
    NEW_PATH="$PARENT_DIR/$NEW_NAME"
    
    # Check if target already exists
    if [[ -e "$NEW_PATH" ]]; then
        echo "⚠️  Skipping $OLD_NAME: $NEW_NAME already exists"
        ((SKIPPED++))
        continue
    fi
    
    if [[ "$DRY_RUN" == true ]]; then
        echo "Would rename: $OLD_NAME → $NEW_NAME"
        ((SUCCESS++))
    else
        if mv "$OLD_PATH" "$NEW_PATH" 2>/dev/null; then
            echo "✅ Renamed: $OLD_NAME → $NEW_NAME"
            ((SUCCESS++))
        else
            echo "❌ Failed to rename: $OLD_NAME"
            ((FAILED++))
        fi
    fi
done

echo ""
echo "═══════════════════════════════════════"
echo "Summary:"
echo "  ✅ Successful: $SUCCESS"
if [[ $SKIPPED -gt 0 ]]; then
    echo "  ⚠️  Skipped: $SKIPPED"
fi
if [[ $FAILED -gt 0 ]]; then
    echo "  ❌ Failed: $FAILED"
fi
echo "  📁 Total: ${#DIRS[@]}"
echo "═══════════════════════════════════════"

if [[ "$DRY_RUN" == true ]]; then
    echo ""
    echo "To apply these changes, run without --dry-run"
fi
