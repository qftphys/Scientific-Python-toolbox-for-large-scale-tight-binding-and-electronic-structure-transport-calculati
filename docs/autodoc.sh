#!/bin/bash

# Default options
skip_commit=0

# Create documentation...
# Parse options

# Get top-level directory of repository
top_dir=`git rev-parse --show-toplevel`

# Move to the source top directory
pushd $top_dir

# Ensure that the current repo state is saved...
git stash

# Get latest tag version on master
git checkout master
tag=`git describe --abbrev=0`
doc_tag=$tag
head_tag=`git describe`
git checkout gh-pages

while [[ $# -gt 0 ]]; do
    opt=$1
    shift

    case $opt in
	--tag|-t)
	    tag=$1
	    doc_tag=$head_tag
	    shift
	    ;;
	--skip-commit|-sc)
	    skip_commit=1
	    ;;
	*)
	    echo "Unrecognized option: $opt"
	    ;;
    esac
    
done



# Check if the current documentation is the same
# If so, quit immediately
cur_tag=`head -1 docs/doc.tag`

if [[ $doc_tag == $cur_tag ]]; then
    echo "The current documented tag is the same as the latest available tag."
    echo "Will not update documentation..."
    exit 1
fi

# Now we can safely update the documentation tag
echo "$doc_tag" > docs/doc.tag

# Create a temporary directory
tmpdir=`mktemp -d`
echo "... temporary directory: $tmpdir"

# Create a trap, to circle back
trap "rm -r $tmpdir ; git reset --hard HEAD ; git checkout gh-pages ; popd" SIGINT SIGTERM 1

# Prepare temporary documentation folder where settings are
# stored.
# Essentially this is equivalent to the entire gh-pages branch
docdir=gh-pages-docs

# Create temporary stash
# This is necessary as the docs/doc.tag has been updated.
# Consequently we must *fake* a commit.
hashid=`git stash create`
git archive --prefix=$docdir/ -o $tmpdir/gh-pages.tar.gz $hashid

# Re-create the docs/doc.tag to be able to switch branches
git checkout docs/doc.tag

# Move to the latest committed version
# We first checkout master, in case the user has specified 
# a custom tag
git checkout master
git checkout $tag

# Extract the just created tar of the documentation repository
tar xfz $tmpdir/gh-pages.tar.gz

# Create additional directories (only if they do not already exist)
mkdir -p $docdir/docs/build
mkdir -p $docdir/docs/static
mkdir -p $docdir/docs/templates

# Now move into the documentation folder and create the documentation
# that we can then copy to the gh-pages branch
pushd $docdir/docs

# Update API documentation
sphinx-apidoc -fe \
	      -o source ../../

# Create the HTML pages
make html

# tar the html output to an tar.gz file
tar cfz $tmpdir/html.tar.gz --directory build/html .

# Create the manual.pdf
#make latexpdf

# Run coverage check
make coverage
# Store the coverage file
mv build/coverage/python.txt $tmpdir/coverage.txt

popd

# Quick exit if not needed
if [[ $skip_commit -eq 1 ]]; then
    exit 0
fi

rm -r $docdir

# Jump back to the gh-pages branch
git checkout gh-pages

# Remove everything but the docs folder and README.md
git rm -rf [^dR]*

# Extract documentation
tar xfz $tmpdir/html.tar.gz
mv $tmpdir/coverage.txt .

# Now we can safely update the documentation tag
echo "$doc_tag" > docs/doc.tag
# Add everything (including updated tag)
git add .buildinfo docs/doc.tag
# Add all created html files
git add * 
git commit -s -m "Released documentation of $doc_tag"

# Clean-up
rm -r $tmpdir

# Notify how to revert the commit
echo "To uncommit (softly) the documentation do:"
echo "  git reset HEAD~1"
echo "To uncommit the documentation do:"
echo "  git reset --hard HEAD~1"

