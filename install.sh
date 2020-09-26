mkdir tasker
mv tasker.py tasker/
mv README.md tasker
cd tasker
touch notes.txt completed.txt
chmod +x tasker.py
pip installer --user click
echo "Installation complete"
echo "Now you need to add current directory as home"
