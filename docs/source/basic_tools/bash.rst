Terminal - Bash
###############

One crucial tool a developer needs is a *terminal*. It is a tool to interact differently with your computer, i.e., using a `command line interface <https://en.wikipedia.org/wiki/Command-line_interface#Anatomy_of_a_shell_CLI>`_. In other words, it allows you to give text commands to the operating system, instead of manipulating graphical elements (windows, icons, …). While the latter is easier to begin with, the former has the advantages to allow scripting and automation of your tasks, to use less resources, and it only uses the keyboard which can make you more efficient.

Terminology
===========

{{< figure src=“terminal.drawio.svg” title=“Terminology” lightbox=“true” >}}

-  `Command-line interpreter <https://en.wikipedia.org/wiki/Command-line_interface>`__, or *shell*: a program that processes commands, which allows users to access operating system’s services. The syntax (command’s names, arguments, …) is specific to the shell. Examples of shells: ``sh``, ``bash`` (the most common), ``fish``, and ``zsh`` which is the focus of this post.
-  `Terminal <https://en.wikipedia.org/wiki/Terminal_emulator>`__, or *terminal emulator*: a text interface to a shell. In other words, it is the software in which users can access to the command-line interface. Before, terminal refereed to a physical hardware with a keyboard and a monitor. They are now mostly *virtual*, and in practice, it is the window in which we can interact with a shell. Examples of terminals (see `list <https://en.wikipedia.org/wiki/List_of_terminal_emulators>`__):

   -  on macOS: `Terminal.app <https://en.wikipedia.org/wiki/Terminal_(macOS)>`__, `iTerm2 <https://www.iterm2.com>`__, …
   -  on Linux: `Konsole <https://konsole.kde.org>`__, `GNOME terminal <https://en.wikipedia.org/wiki/GNOME_Terminal>`__, …
   -  on Windows: `Windows Terminal <https://devblogs.microsoft.com/commandline/introducing-windows-terminal/>`__, `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`__, …

-  `Command prompt <https://en.wikipedia.org/wiki/Command-line_interface#Command_prompt>`__: a sequence of characters in the command-line interface that tells you the shell is ready to accept a command. It *prompts* you to give a command. It usually contains other information (path of the current directory, hostname, …).


References
===========

-  Wikipedia for `command-line interface <https://en.wikipedia.org/wiki/Command-line_interface#Anatomy_of_a_shell_CLI>`__, `terminal emulator <https://en.wikipedia.org/wiki/Terminal_emulator>`__
-  Questions on StackEchange: `Unix&Linux <https://unix.stackexchange.com/questions/4126/what-is-the-exact-difference-between-a-terminal-a-shell-a-tty-and-a-con>`__ and `superuser <https://superuser.com/questions/144666/what-is-the-difference-between-shell-console-and-terminal>`__
-  `List <https://en.wikipedia.org/wiki/List_of_terminal_emulators>`__ of terminal emulators
-  `Video <https://www.youtube.com/watch?v=hMSByvFHOro>`__ of Luke Smith defining the terminology.
