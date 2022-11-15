To follow along
===============

Requirements
------------

This document assumes that you have a unix-like operating system (Linux, macOS, not Windows but see :ref:`sec-setup-windows`), so that you have access to a terminal (see :ref:`Bash <sec-bash>`). To follow along the presentations of each tool, you will need a `source code editor <https://en.wikipedia.org/wiki/Source-code_editor>`_ [#]_. There are a plethora of choices.

In the following, I will often point out how each tool integrates with `VS Code`_ and its extensions, because this is the editor I use and recommend, but taste and colours are not always the same, so here is a non-exhaustive list of other free, cross-platform and multipurpose source editors.

- Editors with text user interface: `emacs <https://www.gnu.org/software/emacs/>`_, `nano <https://www.nano-editor.org>`_, `vim <https://www.vim.org>`_ or `neovim <https://neovim.io>`_.
- Editors with graphical user interface: `gEdit <https://wiki.gnome.org/Apps/Gedit>`_, `Sublime Text <https://www.sublimetext.com>`_.

See this Wikipedia `article <https://en.wikipedia.org/wiki/List_of_text_editors#Text_user_interface>`_ for more editors.

.. _sec-setup-vscode:

Visual Studio Code
------------------

`VS Code`_ is a free code editor that can be used with a great variety of programming languages. One of its main advantages is its great extensibility. On its own, it is a relatively simple source editor, but anyone can write extensions to add new features into VS Code, improving support for programming languages or adding new functionalities, to the point it can become a full `Integrated Development Environment <https://en.wikipedia.org/wiki/Integrated_development_environment>`_ (IDE) for most programming languages.

Where to start
^^^^^^^^^^^^^^

Let's start from the beginning, you need to install VS Code on your workstation and learn how to use its basic editing features. Since I will not do better than the documentation, I refer to their `Setup page <https://code.visualstudio.com/docs/setup/setup-overview>`_ for the installation procedure, while you can look at their `Get Started page <https://code.visualstudio.com/docs/getstarted/introvideos>`_ and `Basic Editing page <https://code.visualstudio.com/docs/editor/codebasics>`_ for basic editing features.

I want to highlight the `Tips and Tricks page <https://code.visualstudio.com/docs/getstarted/tips-and-tricks>`_, where it is mentioned for example that you can learn how to use basic editing (and more) using *walkthroughs* (on the right in the landing page of VS Code). 

.. .. _setup-vscode_walkthroughs:

.. .. figure:: https://code.visualstudio.com/assets/docs/getstarted/tips-and-tricks/getstarted_page.png

..     Landing page of VS Code 
    
In particular, the walkthroughs "Get Started" and "Editor Playground" are really nice, you will learn how to


..
.. .. _setup-vscode_command_palette:
..
.. .. figure:: https://code.visualstudio.com/assets/docs/getstarted/tips-and-tricks/OpenCommandPalatte.gif
..     :align: center
.. 
..     Command palette ``test`` 
.. 
..

- use the command palette ``Ctrl/Cmd+maj+P`` [#]_ to call in VS Code command (and that is very *very* **very** important),
- change the look of the editor,
- save and sync the settings of VS Code,
- use multi-cursor, snippets, intellisense, ...
- and much more!

Extensions to help you start
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you took a look at the previous references, you should know how to install extensions on the marketplace (*View > Extensions* otherwise). I will only give here some extensions that I think are generally useful and that I used to write this document.

- `Project Manager <https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager>`_ can be used to define "Projects" (or auto-detect git repositories and define a project for each one), which in practice means you can open a project folder easily in a VS Code window (either using ``Project Manager: List Projects to Open`` in the command palette, or directly in the Side bar on the left).
- `LTeX <https://marketplace.visualstudio.com/items?itemName=valentjn.vscode-ltex>`_ provides spelling, *styling* and **grammar** checking for several programming languages (:math:`\LaTeX` included) in several languages (more than 20 supported languages!) using `LanguageTool <https://languagetool.org/fr>`_. I wonder if people really understand how amazing it is.
- `Live Share <https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare>`_ enables sharing your editor in real time remotely, meaning you can invite people in your VS Code window, and collaborate directly writing code together. In practice, everyone can independently move around and edit files, you all have a cursor, and you can also follow a particular person as he makes edits and move around in the project. It is obviously useful for pair programming and teaching.
- `Better Solarized <https://marketplace.visualstudio.com/items?itemName=ginfuru.ginfuru-better-solarized-dark-theme>`_ is a good theme (a look for VS Code) I use, but again, taste and colours are not always the same. The point is you can use another theme than the default one.
- `Draw.io Integration <https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio>`_ to integrate `diagram.net <https://app.diagrams.net>`_ in VS Code, which means you have a graphical interface in VS Code to draw diagrams and more.
- `:emojisense: <https://marketplace.visualstudio.com/items?itemName=bierner.emojisense>`_ to easily insert emojis (Why not? 😛 )


I will recommend more specific extensions when introducing each tool later on.

.. _sec-setup-windows:

About Windows
-------------

I recommend using a unix-like operating system to code, because most of the tools for programmers are tailored for this.

If you still want to use Windows, there are actually alternatives to a full unix-like system.

- Recent versions of Windows actually comes with an "embedded Linux kernel", this feature is called `Windows Subsystem for Linux <https://docs.microsoft.com/en-us/windows/wsl/>`_ (WSL). You can run a GNU/Linux environment directly on Windows, but this is not enabled by default. I refer to its documentation for the `installation <https://docs.microsoft.com/en-us/windows/wsl/install>`_, but I want to highlight the tutorial part of the documentation, and more precisely the page on `Best practices for set up <https://docs.microsoft.com/en-us/windows/wsl/setup/environment>`_ which gives a lot of information.
- There exist tools that provide a unix-like environment on top of Windows: `Cygwin <https://cygwin.com>`_ and `MinGW-w64 <https://www.mingw-w64.org>`_ for example.
- Another option is to install Linux with a dual boot, but it may be quite involved.

In the context of this document, I suspect the first solution is easier to use since it is directly supported by Microsoft, and the goal is just to try the tools introduced later on. Besides, :ref:`sec-setup-vscode` has support for WSL via the `Remote -WSL <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl>`_ extension.



.. [#] Or at least you need to be able to modify files somehow. But if you are here, I guess you will not just use bash commands to do that, so a source editor is probably more suited. 

.. [#] It means ``Ctrl``, except on macOS where ``Cmd`` should be used instead.
