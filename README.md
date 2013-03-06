
Markey
======

**[Markey](https://github.com/skpdvdd/Markey)** is a [markdown](http://daringfireball.net/projects/markdown/) parser package for [Sublime Text 2](http://www.sublimetext.com/).

Installation
------------

Markey relies on [node](http://nodejs.org/) and [marked](https://github.com/chjj/marked). Installation under Arch Linux:

    sudo pacman -S nodejs
    sudo npm install -g marked

To install Markey, clone the repository inside Sublime Text's `Packages` folder, e.g.:

    cd ~/.config/sublime-text-2/Packages/
    git clone git://github.com/skpdvdd/Markey.git

Configuration
-------------

The file `Markey.sublime-settings` contains a default configuration that should work out of the box. The only thing you need to change is the path to the CSS file you want to use for formatting the HTML. To do so edit `Markey.sublime-settings` or better create a file called `Markey.sublime-settings` inside the `Packages/User` folder, and change what you want, like so:

    {
        "markdown_css_path" : "path/to/your/css/file",
    }

Usage
-----

Markey understands everything [marked](https://github.com/chjj/marked) does. Math is also supported (using [MathJax](http://www.mathjax.org/)). Syntax:

    inline math: $$y=kx+d$$
    display math: \[ e=mc^2 \]

Code highlighting is supported via [highlight.js](http://softwaremaniacs.org/soft/highlight/en/). Example:

    ```python
    print('hello')
    ```

Call Markey to convert the currently open buffer to markdown. You might want to add a key binding, e.g.:

    { "keys": ["alt+m"], "command": "markey" }

The parsed file will be opened in a new default browser window. The Python version Sublime Text 2 uses currently does not support all browsers, at least not on Linux. To account for this you can specify the browser name to call manually in the configuration file (e.g. `chromium`).

If the `auto_convert` setting is `true` Markey will be called automatically if a file with the ending `.md`, `.markdown` or `.mdown` is saved. If you do not want this behaviour, set the setting to `false`.

Calling Markey will open a new browser even if the file is already open. Install the [LiveReload](https://github.com/dz0ny/LiveReload-sublimetext2) plugin if you don't want this behaviour.

License
-------

Markey is released under the [zlib license](http://www.zlib.net/zlib_license.html).