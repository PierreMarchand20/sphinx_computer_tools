
Terminal - ZSH
##############

There is a steep learning curve to use a terminal so today, we will see how to improve your terminal experience with the Z shell, also called zsh. It is an alternative to bash, and it is going to be the `default shell on macOS <https://support.apple.com/en-us/HT208050>`_  starting from Catalina 10.5.

Z Shell
===========

We are interested in ``zsh``, which is a shell derived from the Bourne shell ``sh``, like ``bash``. It is the reason why they both share a lot of features. If you already know how to use ``bash`` (``cd``, ``mv``, ``touch``, ``mkdir``, …), don’t worry, you won’t start from scratch again. Note that to make it your default shell, you can use:

.. code:: bash

   chsh -s $(which zsh)

Personally, I mainly use a shell interactively, meaning that I do not write so many shell scripts, so I will mainly focus on this usage. Note that you can use any shell interactively and any other shell in scripts using a `shebang <https://en.wikipedia.org/wiki/Shebang_(Unix)>`__ (``#!/usr/bin/env bash`` for bash) at the beginning of your shell scripts.

Here are some features of zsh that I like and often use (see next `section <#3-plugin-managers>`__ to activate all of them):



-  **Completion** (builtin and improved with `zsh-completions <https://github.com/zsh-users/zsh-completions>`__): just use ``tab`` to complete your command line

   -  **recursive path completion**: no need to write the full directory/file names

   .. asciinema:: zsh_cast/path_expansion.cast
      :rows: 10

   -  **command arguments completion**: ``zsh`` suggests arguments to the command you wrote with a description of each option (for example, ``git`` we saw :ref:`here <sec-git>`) 

   .. asciinema:: zsh_cast/argument_command_completion.cast
      :rows: 25

   -  **command arguments flags**: same as the previous feature, but for flags

   .. asciinema:: zsh_cast/flag_command_completion.cast
      :rows: 25 

   -  **variable expansion**:

   .. asciinema:: zsh_cast/variable_expansion.cast
      :rows: 10 

-  **Better history navigation**: you can search for a command in your history with any substring of this command using up and down arrows (with `history-substring-search <https://github.com/zsh-users/zsh-history-substring-search>`__) 

.. asciinema:: zsh_cast/history_substring_search.cast
    :rows: 20 

-  **Autosuggestion**: the last command starting by what you write is suggested and you can use ``tab`` to autocomplete it (with `zsh-autosuggestions <https://github.com/zsh-users/zsh-autosuggestions>`__)

.. asciinema:: zsh_cast/autosuggestion.cast
    :rows: 15

-  **Syntax highlighting**: a few examples (with `zsh-syntax-highlighting <https://github.com/zsh-users/zsh-syntax-highlighting>`__)

.. asciinema:: zsh_cast/syntax_highlighting.cast
    :rows: 20

-  **Plugin and theme support**: zsh is known for its `plugin managers <#3-plugin-managers>`__ that allows installing/activating the previously cited plugins and many others, but it is also known for its highly customizable `prompt <#4-prompts>`__. We are going to see how to benefit from them in the following.

Plugin managers
===============

As we have seen, some features are available via plugins. You could install them by hand, each repository explains how to do it. Usually you have to download them, source them in your ``.zshrc`` and set some variables. But it can be tricky because the order in which you source them matters, and having a lot of plugins can add a delay when starting a new shell session.

Another possibility is to use a *plugin manager*. There are a lot of them (see `reference <#53-plugin-managers>`__), I personally use `Zim <https://github.com/zimfw/zimfw>`__ that I find fast and easy to use. Besides, it is well-maintained, and the maintainers were quite helpful when I had a question. I tried to use a few other plugin managers, most of them are great, but some added a delay when starting a new shell session, and that is how I tried ``Zim``, which is marketed as `fast <https://github.com/zimfw/zimfw/wiki/Speed>`__. I was also convinced by the fact they `thought <https://github.com/zimfw/zimfw/issues/88>`__ about how their project should grow.

The `installation <https://github.com/zimfw/zimfw#installation>`__ process is quite simple, and default configuration should give you most of the features described previously. To add or remove modules, you need to add a line with ``zmodule`` in ``.zimrc`` and run ``zimfw install``. See documentation `here <https://github.com/zimfw/zimfw#zmodule>`__.

Prompts
=======

The benefit in customizing your prompt is that it allows you to display more information. ``git``, that we introduced in :ref:`here <sec-git>`), is the usual first example. You can display the current branch, and if there are modifications to be committed. But you can also display timing between commands, battery level, and a lot of other information. I personally like to keep it simple, but you do you |:wink:|

Similarly to plugins, you could define a customized prompt by hand. But the risk is to add a delay each time you enter a command because of the loading time of the prompt.

Similar problem, similar solution: people have already defined optimized prompts that allow for customization while avoiding delay most of the time. Two popular prompts are `Spaceship ZSH <https://github.com/denysdovhan/spaceship-prompt>`__ and `Powerlevel10k <https://github.com/romkatv/powerlevel10k>`__. I personally use the latter at the moment, but they are both fast, customizable and easy to use. The `installation <https://github.com/romkatv/powerlevel10k#get-started>`__ process is quite straightforward, and the configuration is done interactively.

Here is an example with Powerlevel10k where I show current folder, current git status (notice the ``?1``, which means there is one file not tracked), python virtual environment, time, and a custom prompt that shows |:star:| with ``my display``.

.. asciinema:: zsh_cast/prompt.cast
    :rows: 10

References
==========

Z Shell
~~~~~~~~~~~~

-  `Website <http://zsh.sourceforge.net>`__ of zsh.
-  `Some features <https://github.com/hmml/awesome-zsh>`__ of zsh
-  `Resources <https://github.com/unixorn/awesome-zsh-plugins#generic-zsh>`__ about zsh.
-  Bash vs zsh on `Stackexchange <https://apple.stackexchange.com/questions/361870/what-are-the-practical-differences-between-bash-and-zsh>`__

Plugin managers
~~~~~~~~~~~~~~~~~~~~

-  Some plugin managers: `zim <https://github.com/zimfw/zimfw>`__, `oh my zsh <https://ohmyz.sh>`__, `antigen <https://github.com/zsh-users/antigen>`__, `zplug <https://github.com/zplug/zplug>`__, `zinit <https://github.com/zdharma/zinit>`__, …
-  Benchmarks for plugin managers: `zim benchmarks <https://github.com/zimfw/zimfw/wiki/Speed>`__, a Reddit `thread <https://www.reddit.com/r/zsh/comments/ak0vgi/a_comparison_of_all_the_zsh_plugin_mangers_i_used/>`__.
-  a Reddit `thread <https://www.reddit.com/r/zsh/comments/bj6rwz/what_is_a_good_ohmyzsh_alternative/>`__ on plugin managers.

Prompts
~~~~~~~~~~~~

-  Customizable and efficient prompts: `Powerlevel10k <https://github.com/romkatv/powerlevel10k>`__, `Spaceship <https://github.com/denysdovhan/spaceship-prompt>`__
