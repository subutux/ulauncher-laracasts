# Ulauncher Laracasts Extension

Ulauncher extension for quick access to the Laracasts epsisodes and series.

## Overview

Once you install this extension, just start Ulauncher and type: `lc`. That will start the extension.

![image-20210324143208241](./screenshots/init.png)

From there you can type your search query like `Resourc`:

![image-20210324143400975](./screenshots/resource.png)



## Installation

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/subutux/ulauncher-laracasts
```

## Development

```
git clone git@github.com:subutux/ulauncher-laracasts.git
cd ulauncher-laracasts
make attach
```

The `make attach` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder. _If the extensions folder does not exist, create it and run the command again._

Make sure Ulauncher is not running and from command line run:

```sh
ulauncher --no-extensions --dev -v |& grep "laracasts"
```

This will start ulauncher with all the extensions disabled which will make it easier to look for logs.

You then have to start the Laravel extension manually. In the output of the previous command you should find something similar to this:

```sh
VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/ulauncher-laracasts PYTHONPATH=/usr/lib/python3/dist-packages /usr/bin/python3 /home/mabasic/.cache/ulauncher_cache/extensions/ulauncher-laracasts/main.py
```

Copy and run that command in another terminal window.

Your extension should now be running. To see your changes, just Ctrl+C and re-run the last command.

## License

Ulauncher Laravel Extension is open-source software licensed under the [MIT license](https://opensource.org/licenses/MIT).