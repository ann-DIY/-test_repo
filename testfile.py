print('this is my test file before I build my website')
git init #initialize git respository in your home directory
git config --global user.username ann-DIY #update this with your actual github username
git add testfile.py #replace testfile.py with any file in your home directory you want to upload: 
git commit -m "test commit" #this commits the file and adds a message (required)

git remote add origin https://github.com/ann-DIY/-test_repo.git #update with your link
git push origin master
