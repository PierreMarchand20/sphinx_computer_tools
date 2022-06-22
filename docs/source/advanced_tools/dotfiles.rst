Dotfiles
########

If you followed my previous posts, you may find in your ``${HOME}`` directory several files starting with a dot, or dotfiles: ``.gitconfig`` for your git configuration, ``.zsh`` for you zsh configuration, and ``.p10.zsh`` if you tried Powerlevel10k.

Of course, there are probably a lot of other dotfiles from

-  your editor or your terminal (``.vimrc``, ``.bashrc``, etc.),
-  software programs or libraries you use (I have one for `iTerm2 <https://iterm2.com>`__ and `matplotlib <https://matplotlib.org>`__ for example).

This is not an exhaustive list, but ``${HOME}`` is the place where user configurations are usually stored in plain-text files.

The goal
-----------

Since all these dotfiles are just plain-text files, a natural idea is to save them, or to version them, to actually back up your settings, sync them across multiple machines and be able to deploy them quickly. This is particularly useful when getting a new computer, using a remote computer, or for some other reasons we will see in a later post. 😉

That is why, when talking about *dotfiles*, people refer to a :ref:`git <sec-git>` repository that stores all these dotfiles, but also contains some scripts (sometimes called *bootstrap*) to set everything on a new environment:

-  install the dotfiles into ``${HOME}``,
-  install utilities (for example, a plugin manager for ``zsh`` or an enhanced prompt as we have seen in with :ref:`zsh <sec-zsh>`),
-  install libraries (via `Homebrew <https://brew.sh/index_fr>`__ and processing a ``.BrewFiles`` on macOS for example),
-  etc.

And it needs to be easy to deploy, with a one-line command in the terminal for example.

How-to
---------

As always, there are lots of possibilities to achieve this, and it also depends on your particular needs, so you need to try and fail to find what is the best for you.

That being said, there exists several tools to do all the heavy lifting. At the moment, I use `YADM <https://yadm.io>`__ which I find easy to use and well-maintained. I refer to its documentation for more details, but it really feels like using :ref:`git <sec-git>` in your ${HOME}, which could be cumbersome to do directly. Besides, it offers the possibility to run a script, called *boostrap*, when cloning a repository via `YADM <https://yadm.io>`__. You can use it

-  to set up your :ref:`zsh <sec-zsh>` or :ref:`git <sec-git>` (the ``git config`` options),
-  or to install packages using your system/language package manager

   -  on macOS when using `Homebrew <https://brew.sh/index_fr>`__: you can store a `.Brewfile <https://github.com/Homebrew/homebrew-bundle>`__ in your dotfile repository and call ``brew bundle``,
   -  for python when using `pip <https://pip.pypa.io>`__: you can store a `requirements.txt <https://pip.pypa.io/en/stable/user_guide/#requirements-files>`__ file,

-  or to set up your OS settings. In particular, for macOS you can look at this `file <https://github.com/mathiasbynens/dotfiles/blob/master/.macos>`__.

.. warning::

    **Beware**, you should not store confidential information on a remote repository (email, password, …). YADM and tools like such offer some encryption features, use them or do not take any risk.

There exists a lot of tools to manage dotfiles, they all have their own strategy (wrapping git, using symlinks, …). The best thing to do is to try by yourself and check which one fits best your needs, here is a non-exhaustive `list <https://dotfiles.github.io/utilities/>`__.

References
-------------

Lists of dotfiles
~~~~~~~~~~~~~~~~~~~~~~

-  An unofficial `guide <https://dotfiles.github.io>`__ to dotfiles

Other tutorials/introductions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The `missing semester <https://missing.csail.mit.edu/2019/dotfiles/>`__ from MIT
