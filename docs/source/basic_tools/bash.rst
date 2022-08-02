.. _sec-bash:

Terminal - Bash
###############

One crucial tool a developer needs is a *terminal*. It is a tool to interact differently with your computer, i.e., using a `command line interface (CLI) <https://en.wikipedia.org/wiki/Command-line_interface#Anatomy_of_a_shell_CLI>`_. In other words, it allows you to give text commands to the operating system, instead of manipulating graphical elements (windows, icons, …). While the latter is easier to begin with, the former has the advantages to allow scripting and automation of your tasks, to use less resources, and it only uses the keyboard which can make you more efficient.

.. only:: not latex

    Live examples are available via `asciinema <https://asciinema.org>`__ files. Note that there are not just videos, you can also copy/paste displayed command lines. Try to understand and to reproduce them in your own terminal.


Terminology
===========

.. figure:: ../_static/svg/terminal_bash/terminal.drawio.svg

   Terminology

-  `Command-line interpreter <https://en.wikipedia.org/wiki/Command-line_interface>`__, or *shell*: a program that processes commands, which allows users to access operating system’s services. The syntax (command’s names, arguments, …) is specific to the shell. Examples of shells: ``sh``, ``bash`` (the most common), ``fish``, and ``zsh`` which is discussed :ref:`here <sec-zsh>`. A command is typically its name with eventually some arguments. For example,

   .. code-block:: bash

      echo 'Hello World!'

   where ``echo`` is the command we wish to execute, and ``'Hello World!'`` is its argument. Here the command just prints its argument, give it a try 😉

   .. note:: Commands can have multiple arguments, delimited by whitespace characters, and even options, usually with a long name ``--option1`` and a short name ``-opt1`` (note the number of dashes). For example:
      
      .. code-block:: bash

         echo -e 'Little darling\nThe smiles returning to the faces' 'Little darling'

      will print all its arguments and the flag ``-e`` enables the interpretation of the escape character ``\n``.

-  `Terminal <https://en.wikipedia.org/wiki/Terminal_emulator>`__, or *terminal emulator*: a text interface to a shell. In other words, it is the software in which users can access to the command-line interface. Before, terminal refereed to a physical hardware with a keyboard and a monitor. They are now mostly *virtual*, and in practice, it is the window in which we can interact with a shell. Examples of terminals (see `list <https://en.wikipedia.org/wiki/List_of_terminal_emulators>`__):

   -  on macOS: `Terminal.app <https://en.wikipedia.org/wiki/Terminal_(macOS)>`__, `iTerm2 <https://www.iterm2.com>`__, …
   -  on Linux: `Konsole <https://konsole.kde.org>`__, `GNOME terminal <https://en.wikipedia.org/wiki/GNOME_Terminal>`__, …
   -  on Windows: `Windows Terminal <https://devblogs.microsoft.com/commandline/introducing-windows-terminal/>`__, `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`__, …

-  `Command prompt <https://en.wikipedia.org/wiki/Command-line_interface#Command_prompt>`__: a sequence of characters in the command-line interface (CLI) that tells you the shell is ready to accept a command. It *prompts* you to give a command. It usually contains other information (path of the current directory, hostname, …).

Filesystem
==========

Files are usually displayed in a hierarchical tree structure, where each node is a directory. In :ref:`directory_hierarchy`, you can see a typical filesystem for an operating system with two users, Alice and Bob. Both of them have their own directory, called *home directory*, where they can put their documents, install their software programs, etc. Every file and directory is under the *root* directory ``/``, which is literally the root of the hierarchical tree structure.

.. _directory_hierarchy:

.. figure:: ../_static/svg/terminal_bash/directory_hierarchy.drawio.svg

   Directory hierarchy

Every process (shell, commands that are executed, ...) has a *current working directory*, which is simply the directory in which it is working from. For example, a user starting a new shell will usually have the home directory as current working directory.

Now that we understand that each directory and file are parts of a hierarchical tree structure, we need to locate them in this structure. To do that, we use a *path*, a string of characters composed by directory names and a delimiting character: ``/`` on Unix systems. There are two types of path:

- *absolute path*, which corresponds to the location starting from the root directory. For example ``/home/Alice/textfile.txt``.
- *relative path*, which corresponds to the location starting from the current working directory. Assuming the latter is ``/home/Bob``, the relative path to ``textfile.txt`` would be ``../Alice/textfile.txt``, where ``..`` refers to the parent directory.

Navigation
==========

Once you have started a shell session, the first thing you can try is to check where you are on your laptop with the command ``pwd`` (**p**\ rint **w**\ orking **d**\ irectory).

.. code-block:: bash
   
   pwd


It will print out the absolute path to your current directory, something like ``/home/YourName``. To change the current directory, you can use ``cd`` (**c**\ hange **d**\ irectory) followed by the (absolute or relative) path of its new location. For example, if we want to go the root directory.

.. code-block:: bash
   
   cd /

Then, you can check that you are at the root directory using again ``pwd``.

.. tip:: 
   - Calling ``cd`` without argument changes the current directory to your home repository.
   - Calling ``cd -`` changes the current directory to its previous location.
   - Calling ``cd ~`` changes the current directory to the home directory.
   - Calling ``cd ..`` changes the current directory to its parent directory.

.. note:: 
   - You can make a path combining different shortcuts, for example ``cd ~/../..`` will change the current directory to the root directory in the previous :ref:`example <directory_hierarchy>` (home directory, then go up two levels).


To know where to go, you may need to know what are the files and directory contained in a given directory. You can use ``ls`` (**l**\ ist **f**\ iles) to print them out.

.. only:: not latex

   Here is a small example illustrating the previous commands where the structure is the same as in :ref:`directory_hierarchy`.

   .. asciinema:: ../_static/asciicast/bash/navigation_output.cast
      :rows: 14

Change 
==========================

We can now start to modify the hierarchical structure adding and removing files and directories.

- To create an empty file named ``my_textfile.txt``, use ``touch``

.. code-block:: bash

   touch my_textfile.txt

- To create an empty directory name ``my_directory``, use ``mkdir`` (**m**\ a\ **k**\ e **dir**\ ectory)

.. code-block:: bash

   mkdir my_directory

- To remove a file name ``my_textfile.txt``, use ``rm`` (**r**\ e\ **m**\ ove)

.. code-block:: bash

   rm my_textfile.txt

- To remove a directory named ``my_directory``, use ``rm`` (**r**\ e\ **m**\ ove) with the flag ``-r`` or ``--recursive`` to allow recursive deletion of the directory's content

.. code-block:: bash

   rm -r directory

.. warning:: Be careful when deleting files and directories, it is quite involved/impossible to recover what you delete with ``rm`` (no recycle bin), and you risk breaking your system by deleting the wrong file or directory. 

.. only:: not latex

   Here is a small example illustrating the previous commands where the structure is the same as in :ref:`directory_hierarchy`.

   .. asciinema:: ../_static/asciicast/bash/change_structure_output.cast
      :rows: 17

Tips and tricks
===============

.. rubric:: Autocompletion 
   
Use ``tab`` to autocomplete paths. When writing the beginning of path, hit ``tab`` to autocomplete interpretation, if there is not a unique possibility, it will display the different possibility.

.. only:: not latex

   .. asciinema:: ../_static/asciicast/bash/autocompletion_output.cast
      :rows: 7

   In this example, I hit ``tab`` on the second line to avoid writing the long name of the directory.


.. rubric:: Backward research
   
Use ``ctrl-r`` to look for previous command calls.

.. only:: not latex
      
   .. asciinema:: ../_static/asciicast/bash/backward_search_output.cast
      :rows: 7

   In this example, I hit ``ctrl-r`` once, I then start to write ``tou`` so that it displays the last command starting by *tou*, and finally hit again ``ctrl-r`` to search for the previous command starting by *tou*.

References
===========


.. rubric:: Terminology

-  Wikipedia for `command-line interface <https://en.wikipedia.org/wiki/Command-line_interface#Anatomy_of_a_shell_CLI>`__, `terminal emulator <https://en.wikipedia.org/wiki/Terminal_emulator>`__
-  Questions on StackEchange: `Unix&Linux <https://unix.stackexchange.com/questions/4126/what-is-the-exact-difference-between-a-terminal-a-shell-a-tty-and-a-con>`__ and `superuser <https://superuser.com/questions/144666/what-is-the-difference-between-shell-console-and-terminal>`__
-  `List <https://en.wikipedia.org/wiki/List_of_terminal_emulators>`__ of terminal emulators
-  `Video <https://www.youtube.com/watch?v=hMSByvFHOro>`__ of Luke Smith defining the terminology.

.. rubric:: Filesystem

- Wikipedia for Unix and Unix-like filesystems: `Filesystem Hierarchy Standard <https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard>`_
- Wikipedia for `home directory <https://en.wikipedia.org/wiki/Home_directory>`_, `root directory <https://en.wikipedia.org/wiki/Root_directory>`_, `working directory <https://en.wikipedia.org/wiki/Working_directory>`_, `path <https://en.wikipedia.org/wiki/Path_(computing)>`_
