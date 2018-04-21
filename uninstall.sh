pip3 uninstall edict
git rm -r dist
git rm -r build
git rm -r edict.egg-info
rm -r dist
rm -r build
rm -r edict.egg-info
git add .
git commit -m "remove old build"
