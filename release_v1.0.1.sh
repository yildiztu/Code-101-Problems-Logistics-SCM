#!/bin/bash

# Release Script for Version 1.0.1
# Creates a proper Git release with tagging

echo "🚀 Starting release process for version 1.0.1..."
echo ""

# Check if we're on main branch
current_branch=$(git branch --show-current)
if [ "$current_branch" != "main" ]; then
    echo "⚠️  Warning: You're on branch '$current_branch', not 'main'"
    echo "Switching to main branch..."
    git checkout main
fi

# Pull latest changes
echo "📥 Pulling latest changes from remote..."
git pull origin main

# Check working directory is clean
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  Working directory is not clean. Please commit or stash changes first."
    git status
    exit 1
fi

# Create release tag
echo "🏷️  Creating release tag v1.0.1..."
git tag -a v1.0.1 -m "Release version 1.0.1

🎯 Codebase Organization Complete:
• Clean and organized project structure
• All helper scripts moved to /scripts folder
• Essential files remain in root directory
• Part I and Part II problem folders properly structured
• Ready for production use

📊 Statistics:
• 173 files organized in /scripts folder
• Essential documentation files in root
• Clean git history with proper .gitignore

✅ This release represents a fully organized and production-ready codebase."

# Push tag to remote
echo "📤 Pushing tag to remote repository..."
git push origin v1.0.1

# Push main branch (ensure it's up to date)
echo "📤 Pushing main branch to remote..."
git push origin main

echo ""
echo "✅ Release v1.0.1 created successfully!"
echo ""
echo "🎯 Release Summary:"
echo "  • Tag: v1.0.1"
echo "  • Branch: main"
echo "  • Remote: origin"
echo ""
echo "📋 To verify the release:"
echo "  git tag -l"
echo "  git show v1.0.1"
echo ""
echo "🌐 You can also create a GitHub Release at:"
echo "  https://github.com/yildiztu/Code-101-Problems-Logistics-SCM/releases/new"
echo "  Select tag: v1.0.1"
echo "  Title: Release v1.0.1"
echo "  Description: Codebase organization complete - production ready"
echo ""
echo "🚀 Your release is now live!"
