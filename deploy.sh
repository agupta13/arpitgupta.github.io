# Always publish the latest CV build from the applications repo (Overleaf-synced).
cp ../arpitg_applications/cv/cv.pdf pdfs/cv.pdf
bundle exec jekyll build
# Normalize perms locally so Apache can read them once rsynced.
# (Restrictive local modes otherwise carry over and Apache returns 403; macOS
# ships BSD rsync 2.6.9, which lacks the --chmod=D/F prefixes, so we chmod here.)
find _site -type d -exec chmod 755 {} +
find _site -type f -exec chmod 644 {} +
rsync -a _site/ arpitgupta@linux.engr.ucsb.edu:~/public_html/
