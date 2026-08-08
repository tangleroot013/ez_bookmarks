publish-pages:
	git add index.html
	git diff --cached --quiet || git commit -m "Update GitHub Pages site"
	git push origin main
