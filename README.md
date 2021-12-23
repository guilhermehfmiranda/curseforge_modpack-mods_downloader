# Diclaimer
Tested on Windows 10 w/ Python 3.9

# What? Why? How?
## What is it?
A Python program to automatically download a list of mods for Minecraft - Java Edition from curseforge.com based on the contents of a modpack's manifest.json and modlist.html.
## Why is it?
I didn't want to download a custom Minecraft launcher just to download a batch of mods listed in a modpack, neither wanted to manually click the mod's link, select the version chosen by the modpack's creator, press download and save.
## How it works?
In short, webscrapping used to download mods.
### Step 1 > json
```
Opens [ manifest.json ] and mounts an array with it's content.
Filter's the [ fileID ] values from the previous array into a new array.
```
### Step 2 > BeautifulSoup
```
Opens [ modlist.html ] and mounts an array with it's content.
Filter's the [ a ] tags from the previous array.
Mounts a new array with their [ href ] values.
```
### Step 3 > selenium's webdriver - take 1
```
Configure chrome webdriver's options.
Opens chrome webdriver.
```
### Step 4 > selenium's webdriver - take 2
```
For each mod entry in the previous array:
    prints to the console the next to-start download mod's name
    mounts it's [ url ] w/ specific path to start download on page load
    opens said [ url ] in the webdriver
    waits 10 seconds before starting the next loop (and the next download)
After the last loop, waits for user input in the console to kill the webdriver's process,
only requiring the user to check if all was downloaded already
```

# Steps to Run it (first time)
## Install [ pipenv ]
```
pip install --user pipenv
```
## Install all dependencies (including dev)
```
pipenv install --dev
```
<!-- ### Installing a package
```
pipenv install <package>
```
## Uninstalling all dependencies (including dev)
```
pipenv uninstall --dev
```
### Uninstalling all dev packages
```
pipenv uninstall --all-dev
```
### Uninstalling a package
```
pipenv uninstall <package>
```
## Locking packages
```
pipenv lock
``` -->
## Install [ chromedriver ]
Google it and place the executable that matches [ YOUR ] chrome web browser's version in the [ chromedriver ] folder
## [ manifest.json ] and [ modlist.html ]
Place them in the same folder as [ main.py ]
## Run [ main.py ] with [ pipenv ]
```
pipenv run py main.py
```