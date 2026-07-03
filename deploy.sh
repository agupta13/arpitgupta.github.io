bundle exec jekyll build
# --chmod forces web-readable perms on the server regardless of local file modes.
# (Without this, restrictive local perms rsync through and Apache returns 403.)
rsync -a --chmod=D755,F644 _site/ arpitgupta@linux.engr.ucsb.edu:~/public_html/
