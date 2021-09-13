# Diskrita 

Diskrita simply interfaces with the Discord Game SDK to set your activity to be Krita.

## Supported platforms

As far as I'm aware, Diskrita supports all major platforms running on x86-64 hardware. This includes Windows, Linux and Mac OSX.

## Installing

### From source code

#### Step 1. Get the source code

##### Cloning the repository

To clone the repository, you need [git](https://git-scm.com) to be installed.
Run the following command to install it.
```
git clone https://github.com/tecc/Diskrita.git
```

##### Downloading files from GitHub

[Download here](https://github.com/tecc/Diskrita/archive/refs/heads/dev.zip).
That is a direct link to GitHub's packaged archive.

#### Step 2. Install it to Krita

##### Installing using a zip file

###### Step 2.1. Build Diskrita

Building Diskrita is easy - simply run [bundle.py](./bundle.py) with Python 3 or above. It will make an installable. Run this in the source directory:

```
python3 bundle.py
```

###### Step 2.2. Install it to Krita

> To-do

##### Installing the files manually

> To-do

#### Step 3. Restart Krita

Annoyingly, Krita requires that you restart the application when you install a new plugin (or update one, for that matter).

## Licence

Diskrita is licensed under the [MIT licence](./LICENCE.txt).

Under the hood it's powered by [LennyPhoenix's py-discord-sdk library](https://github.com/LennyPhoenix/py-discord-sdk). All of the files belonging to PDK are located in [diskrita/dsdk](./diskrita/dsdk), and are licenced under the MIT licence as well.
