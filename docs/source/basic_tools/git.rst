.. _sec-git:

Git
###

Git is an essential tool to collaborate and version your code. That is why, we will take the time to understand its benefits, and how to use it. The presentation will be organized around what git allows you to do: versioning, remote backup, synchronization and collaborative work.

Each one of these usages will require the previous ones. For example, you need to know how to version your code to use a remote backup, but you do not need to know a priori how to use git for collaborative work. So that, you can start by reading just what you need. If you want to go further, I give some :ref:`references <git_ref>` to other concepts in git that I do not talk about here.

Note that I present command lines to use git, but there exists a lot of graphical interfaces (see this `list <https://git-scm.com/downloads/guis>`__), but understanding how git works is still necessary to use them. You can also find a `presentation <https://pierremarchand20.github.io/slides/2019_01_10_infomath_git>`_ I did a few years ago on git with a similar approach.

.. only:: not latex

    Live examples are available via `asciinema <https://asciinema.org>`__ files. Note that there are not just videos, you can also copy/paste displayed command lines. Try to understand and to reproduce them in your own terminal.



Setup
--------

Configuration
^^^^^^^^^^^^^

We refer to this `page <https://git-scm.com/book/fr/v2/Démarrage-rapide-Installation-de-Git>`__ for installation instructions, but before, check if you do not already have it. Then, the first thing you need to do is to configure git. You should at least set your identity as follows:

.. code:: bash

   git config --global user.name "Username"
   git config --global user.email username@mail.com

Each modification you make to your repository will be associated with this identity.

The flag ``--global`` just means that this identity will be used in all the repository you work with on your system. You can always set local configuration to override it, and you can also set other types of configuration variables like the editor used to write commit messages, diff tool and so on. We refer to this `page <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>`__ if you want to go further, but it should be enough at first. You can check your configuration with ``git config --list``.






Create repository
^^^^^^^^^^^^^^^^^

To start locally a repository, go to the folder you want to work with, here ``YourRepository``, and use ``git init`` to initialize your git repository.

This will create a hidden folder ``.git`` with all the information of the repository. You should not modify anything in ``.git``.

.. only:: not latex

    .. asciinema:: ../_static/asciicast/git/git_setup_output.cast
        :rows: 21

    .. note:: 
        
        Remark that when the repository is created, ``(main #)`` is added to the command prompt. This is because I slightly customized my prompt command, as first mentioned :ref:`previously <sec-bash-variables>`. To add this information to the prompt command, I used `git-prompt.sh <https://github.com/git/git/blob/main/contrib/completion/git-prompt.sh>`_ as described `here <https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-Bash>`__. It will show the name of the current branch (I will explain what it means in the next section) and the state of the local repository.

Versioning
----------

The first benefit of using git is that it allows you to *version* your source code. It means that git will track your files, save their history efficiently, and give you the possibility to easily navigate through the different versions of your files. Using git, you can forget about versioning your files numbering their name like ``file1.txt``, ``file2.txt``, ``filefinal.txt``, ``filefinal1.txt``, … and all the redundancy it implies.

Note that you can do it **locally**, even if in practice most people also use a remote to back up their repository. This will be discussed afterward, and we will keep it local for the moment.

Create History
^^^^^^^^^^^^^^

Firstly, you need to put a file, here ``FirstFile.txt``, in your repository and ask git to track it. To do so, you need two commands:

.. code:: bash

   git add FirstFile.txt
   git commit FirstFile.txt -m "first file added"

The first command makes the file ``FirstFile.txt`` *staged*, and the second one commit this version of the file in the repository’s history, with a small comment. The repository’s history can be represented as a graph/tree, where each commit is a node, containing a state of the whole repository, a comment describing the commit, a unique commit ID (a hexadecimal number of 40 digits), the commit date, the committer’s name, and email address.

Note that if you do not add the ``-m`` flag followed by a string, ``git`` will open your editor (default to ``nano``) for you to write a commit message instead.

In :numref:`fig-versioning`, you can see an illustration of a simple history. Each rectangle represents a commit, so a snapshot in the history of your repository with all the associated information, in particular, a commit ID. The commit ``291bb0`` is the first one, followed by ``e9b2d0`` which has a pointer to the previous state. That is why there is an arrow from ``e9b2d0`` to ``291bb0``. Then, ``main`` is the tip of the history, and represents a *branch*. A branch represents a linear history of your repository, and in practice it is a pointer to the last state of a linear history. Here, we only have one branch. Finally, ``HEAD`` is the actual state on your computer, if you open a file tracked by this repository, its state will be the one of the commit ``HEAD`` points to. In this example, ``HEAD`` points to ``main``, so the last state of the history.

Here, the name of the branch I created is called ``main`` [#]_.

.. _fig-versioning:
.. figure:: ../_static/svg/git/versioning.drawio.svg
   :align: center

   Versioning


.. note:: 
    Why do you need two commands just to update your repository?

    It is usually the first point that confuses people discovering git. I refer to some :ref:`discussions <git_references_specific_discussions>` on the subject, but the bottom line is that the staged area (so, the files you used ``git add`` on) allows reviewing your changes before committing them to the repository’s history. It also allows separating multiple changes in meaningful commits.

    For example, if you add a feature to your code, and fix a bug at the same time. You can add only the changes related to your fix, review them, commit them with a specific description, and then do the same for your new feature. Remember that your commit messages need to be descriptive enough to easily navigate the repository’s history.

.. only:: not latex

    .. asciinema:: ../_static/asciicast/git/first_file_output.cast
        :rows: 29

Navigating through the history
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you populated your history’s repository, you may want to go back and check previous states of your repository. The current state on your computer (not necessarily the last one) is called ``HEAD``, see :numref:`git-fig-current`.

.. _git-fig-current:

.. figure:: ../_static/svg/git/HEAD_1.drawio.svg

    Current state to last commit

The command ``git log`` shows your repository’s history, i.e., commit messages, commit IDs, committer’s names, and email addresses. And, ``git log -2`` will only show the information for the two last commits.

To navigate through your history, you can use

-  relative references: to check out the second generation ancestor of ``HEAD`` use ``HEAD~2``, see :numref:`fig-git_checkout_head2`.

-  to return to the last state of your repository, ``git checkout main``, see :numref:`fig-git_checkout_main`.

-  absolute references: using the commit ID, ``git checkout e9b2d0`` (first characters are enough), see :numref:`fig-git_checkout_e9b2d0`


.. _fig-git_checkout_head2:
.. figure:: ../_static/svg/git/HEAD_3.drawio.svg

    ``git checkout HEAD~2``

.. _fig-git_checkout_main:
.. figure:: ../_static/svg/git/HEAD_1.drawio.svg

    ``git checkout main``

.. _fig-git_checkout_e9b2d0:
.. figure:: ../_static/svg/git/HEAD_2.drawio.svg

    ``git checkout e9b2d0``




.. only:: not latex

    Taking a similar example, we have three commits, starting from the last one, we navigate using

    -  relative reference (``HEAD~2``)
    -  branch name (``main``)
    -  an absolute reference

    .. asciinema:: ../_static/asciicast/git/navigating_output.cast
        :rows: 30

    .. note:: Remark how ``HEAD`` is said to be on main when on the third commit, but not the others.

.. tip:: 
    You are lost? ``git status`` will tell you where you are and what you can do.


Back up
--------

Another advantage of git is the possibility to back up your repository in a remote server. It is said to be a *distributed* version-control system (unlike SVN for example), because both your local repository and the remote repository will have the full history after each synchronization.

Set up the remote
^^^^^^^^^^^^^^^^^

First, you need to create a remote repository in `GitHub <https://github.com>`__, `GitLab <https://about.gitlab.com>`__, `Bitbucket <https://bitbucket.org/>`__ or some other providers (or your own git server).

.. _git-fig-github:

.. figure:: ../_static/png/git/github.png
   :alt: GitHub

   GitHub

Providers will usually give you instructions on how to set up your repository (see :numref:`git-fig-github` for example). In any case, we need to add the remote URL to the local repository with

.. code:: bash

   git remote add origin https://github.com/PierreMarchand20/YourRepository.git

The remote is then referenced as ``origin``. And, we need to push the local commits to the remote

.. code:: bash

   git push -u origin main

We have now a remote branch ``origin/main``, which is the copy on the remote ``origin`` of ``main`` as described in :numref:`git-fig-remote`.

.. _git-fig-remote:

.. figure:: ../_static/svg/git/remote.drawio.svg

    Remote added

.. note:: The example uses a https URL, but you can also connect to a git server via a :ref:`sec-ssh` URL. This can be useful to avoid having to give a username and a password each time you want to update the remote repository.

.. only:: not latex

    .. asciinema:: ../_static/asciicast/git/remote_output.cast
        :rows: 30

    .. note:: Remark how ``origin/main`` appears now when using ``git log``.

    .. note:: For the sake of the demonstration, I used a "local" remote repository. But in your case, you should use ``git remote add origin <url>`` instead, where ``<url>`` is an url to a repository on a git server.

Working with a remote repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, we create a new commit locally, so that the branch ``main`` is further than the branch ``origin/main`` on the remote (see :numref:`fig-git-local-new-commit`).

.. _fig-git-local-new-commit:
.. figure:: ../_static/svg/git/remote_1.drawio.svg

    Local new commit

We just need to do ``git push`` to update ``origin/main`` (by default, git will push to ``origin/main``, no need to specify it).

.. only:: not latex

    .. asciinema:: ../_static/asciicast/git/sync_output.cast
        :rows: 30
    .. note::  Remark that ``origin/main`` appears on the third commit, while ``HEAD`` and ``main`` are on the fourth commit after ``git commit``.

Synchronization
---------------

Having a remote repository, you can also use it to synchronize a repository on several computers, let’s say ``Computer 1`` and ``Computer 2``.

.. _sec-git-update-from-remote:

Update from remote
^^^^^^^^^^^^^^^^^^

Imagine you create a new commit locally on ``Computer 2``, then you push this new commit to the remote repository. This time, it is ``origin/main`` that is further than ``main`` from the point of view of ``Computer 1``! We are in the situation illustrated by :numref:`git-fig-remote-2`.

.. _git-fig-remote-2:

.. figure:: ../_static/svg/git/remote_2.drawio.svg

    Repository on ``Computer 1``


To update your local repository, you just need to call ``git pull`` on ``Computer 1``, and it will update ``main`` adding the last commits from ``origin/main``. This is called a *fast-forward merge*, because there is no divergent branches, git just needs to update the local copy of ``origin/main`` to get the last changes and to move the pointer of the local branch (here ``main``) forward to the tip of the remote branch (here ``origin/main``).

.. note:: ``git pull`` can be seen as the combination of two commands:

    - ``git fetch`` for the local branch. In our case, it updates the local copy of ``origin/main``.
    - ``git merge``, which in the present case will do a fast-forward merge.

.. _sec-git-issue:

Issue
^^^^^

Something wrong can quickly happen with bad practices. Imagine you do a new commit locally on both computers. You push your new local commits from ``Computer 2`` to the remote repository. This time, ``main`` and ``origin/main`` have diverged from the point of view of ``Computer 1``, which is described in :numref:`git-fig-remote-3`.

.. _git-fig-remote-3:

.. figure:: ../_static/svg/git/remote_3.drawio.svg

    Repository on ``Computer 1`` with diverged ``main`` branches

Two remarks here:

-  It is usually what people discovering git fear the most! But note that it is not specific to git, if you modify one file locally on two computers, you will also have to deal with this situation. Actually, git will tell you that there is an issue if you try ``git push`` on ``Computer 1``, and it will help you solve the issue. So git is a tool to help you deal with this situation, instead of doing everything by hand.
-  That being said, you should avoid this situation because it is more likely to break your code. In the case where you are just synchronizing several computers of yours, you can always ``git pull`` when starting to work on one computer, add/commit all your modifications, and ``git push`` when you have finished. You should not be in this situation if you follow this workflow.

In case you still encounter this situation (you forgot to commit a change, or to push at the end of a working session for example), we refer to the next section.

Collaboration
-------------

If you want to collaborate with someone else, or if you work with a team on a project, then the previous :ref:`issue <sec-git-issue>` may occur more often. It is very likely that your coworkers will commit some changes while you are also working on the repository, so that, you will be in the situation described in the :numref:`git-fig-remote-3` with divergent branches. To avoid this, you need to adopt a workflow, i.e., a way to work all together with the git repository. There are several solutions depending on how you work with your team/coworkers, the number of contributors, etc. It is an advanced subject, and I give some pointers for more information in the :ref:`references <git_references_specific_discussions>`.

But here are some general considerations shared by most of them. They usually aim at:

-  making the history’s repository/tree as flat as possible. This makes it easier to navigate between commits,
-  avoiding situations with diverging branches, and thus, limiting the risks of breaking your code.

And, they usually rely on one of the two following git operations, if not both: ``git merge`` and ``git rebase``. Both commands allow merging two branches, but the outcome is different as we will see.

.. _git-collaboration-merge:

Merge
^^^^^

Merging is used automatically by git when pulling from a remote which is further than the local branch. But it can also be used to merge two different branches locally. Actually, ``git pull`` means ``git fetch``, which updates locally the remote branch (here, the local copy of ``origin/main``), followed by ``git merge``, between the remote branch (the local copy of ``origin/main``) and the local branch (``main``).

Let us take an example. We have a file ``FirstFile.txt`` that contains the following three lines:

.. code:: text

   This is the first file
   This is the first file
   This is the first file

On ``Computer 1``, we modify it to

.. code:: text

   This is the first file - modified by Computer 1
   This is the first file
   This is the first file

On ``Computer 2``, we modify it to

.. code:: text

   This is the first file
   This is the first file
   This is the first file - modified by Computer 2

The first line is modified by ``Computer 1``, and the third line is modified by ``Computer 2``.

Now, we commit both changes locally, we push the modifications by ``Computer 2``, and pull on ``Computer 1``. Note that git is safe, if you try to push changes from ``Computer 1``, it will be rejected because ``main`` on ``Computer 1`` is behind ``origin/main``. When pulling on ``Computer 1``, because the modifications from both computers are not overlapping, git actually proceeds to merge automatically the changes, and create a commit stating the merge. Then, you just need to push on ``Computer 1``, and pull on ``Computer 2``, and we obtain a history as :numref:`git-fig-merging`.

.. _git-fig-merging:
.. figure:: ../_static/svg/git/merge.drawio.svg

    Merging

.. note:: This is the default behaviour of git when calling ``git pull``, but in recent versions, it also displays a warning explaining how to use rebase (see next :ref:`section <sec-git-rebase>`) instead of merge when the changes do not overlap. You can configure the default behaviour with ``git config --global pull.rebase true`` to change it to use rebase. You can also disable the default strategy to reconcile divergent branches (so no ``merge`` or ``rebase``), and only enable :ref:`fast-forward merges <sec-git-update-from-remote>` with ``git config --global pull.ff only``.


.. only:: not latex

    We reproduce exactly this example given with one repository shared by two computers, represented here by two different folders on the same computer for the sake of the demonstration. The repository is one commit further on ``Computer 2`` and on ``Computer 1``, compared to the remote. But the two changes do not overlap.

    .. asciinema:: ../_static/asciicast/git/automerge_output.cast
        :rows: 35

    .. note::  If you try to reproduce this example, ``git`` will open your editor to write a commit message (``nano`` by default). But for auto merges like this, the commit message is already written and you can just close your editor. I removed this behaviour of opening the editor in case of auto merge for the sake of the live example, but you should keep this behaviour.


Let us look at the case where the modifications are overlapping. On ``Computer 2``, we do the following change instead:

.. code:: text

   This is the first file - modified by Computer 2
   This is the first file
   This is the first file

If we commit locally on both computers, and we push on ``Computer 2``. Then, when pulling on ``Computer 1``, auto merging fails, and ``FirstFile.txt`` contains now:

.. code:: bash

   <<<<<<< HEAD
   This is the first file - modified by Computer 1
   =======
   This is the first file - modified by Computer 2
   >>>>>>> 438c30414304658df44ef2dfd735abea47c7025a
   This is the first file
   This is the first file

We see the change from the local ``HEAD`` (so, ``Computer 1``), and the change from the commit on the remote (so, ``Computer 2``). We just need to modify ``FirstFile.txt`` as we want, then stage it and commit.

.. only:: not latex


    We reproduce again the example with one repository shared by two computers, represented here by two different folders on the same computer. The repository is one commit further on ``Computer 2`` and on ``Computer 1``, compared to the remote. But the two changes overlap.

    .. asciinema:: ../_static/asciicast/git/merge_output.cast
        :rows: 35

.. _sec-git-rebase:

Rebase
^^^^^^

While ``git merge`` creates a new commit, as illustrated :ref:`here <git-fig-merging>`, ``git rebase`` changes the base of one branch to put it after the last commit of the other branch. Taking the same example illustrated :ref:`here <git-fig-remote-3>`, we can do ``git fetch origin`` on ``Computer 1`` to update the local copy of ``origin/main``, and then ``git rebase origin/main``. Git will start an "interactive rebase", reviewing each commit from the diverged part of ``main``, one after the other, to check if there are overlapping differences with ``origin/main``. 

If there are overlapping differences between a commit from ``main`` and ``origin/main``, you need to fix them, then use ``git add`` with the fixed files which will modify the current reviewed commit and use ``git rebase --continue`` to go onto the next commit to review in the interactive rebase. 

With the example from :numref:`git-fig-remote-3`, using a rebase strategy instead of merge will produce a linear history, see :numref:`git-fig-rebase`.

.. _git-fig-rebase: 

.. figure:: ../_static/svg/git/rebase.drawio.svg

    Rebasing

where the diverged commit ``e9b2d0a`` is now behind ``30f00e3``. We moved the base of ``main`` to the tip of ``origin/main``. 

.. note:: In recent versions of git, you can use ``git pull`` instead of using ``git fetch`` and ``git rebase`` to apply the same strategy. As mentioned in :ref:`git-collaboration-merge`, you need to change its default behaviour with ``git config --global pull.rebase true`` to do so.

This is particularly useful to avoid an additional commit, and in the case of two different branches, it allows preserving both history. But, there is one `golden rule <https://www.atlassian.com/git/tutorials/merging-vs-rebasing#the-golden-rule-of-rebasing>`_ when using ``git rebase``. It should **not be used with public branches** For example, you should not rebase ``origin/main`` instead of ``main``, because it would modify the commit history of the branch shared with other workstation/people.

.. only:: not latex

    .. asciinema:: ../_static/asciicast/git/rebase_output.cast

    In this example, the default behaviour of ``git pull`` is set to rebase. Don't mind the ``sed`` command, it is just to modify a file directly from the terminal, you could use an editor you want instead.

Notes for VS Code users
-----------------------

VS Code already comes with an extension for git, so that you can do most of the basic git commands (push, pull, add, commit, ...) directly via the graphical interface of VS Code. Everything is in "Source Control" in the Activity bar on the left. You can also access it via *View > Source Control*.

- `Changes <https://code.visualstudio.com/docs/sourcecontrol/overview#_working-in-a-git-repository>`_: you can find an overview of all the changes, and if you click on a modified file, it will display the modifications of the file.
- `Commit <https://code.visualstudio.com/docs/sourcecontrol/overview#_commit>`_: you can select the changes you want to add, write a commit message and commit.
- etc.

VS Code will also display information directly in the editor.

- `Gutter indicators <https://code.visualstudio.com/docs/sourcecontrol/overview#_gutter-indicators>`_: when opening modified in files in the editor, VS Code will add an indicator on the left to the modified lines.
- `Merge conflics <https://code.visualstudio.com/docs/sourcecontrol/overview#_merge-conflicts>`_: it will add colours to merge conflicts, and buttons to accept either one or both change.

You can find the documentation `here <https://code.visualstudio.com/docs/sourcecontrol/overview>`__ with all the features. But git integration in VS Code can go even further with additional extensions.

- `GitLens <https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens>`_ adds an enormous amount of git-related features, among which, 

  - `Enriched Source controle view <https://github.com/gitkraken/vscode-gitlens#source-control>`_ with a list of all the commits of the current branch and provide quick access to the modified files in each commit (and show the modifications when clicking on it).
  - `Information <https://github.com/gitkraken/vscode-gitlens#blame-codelens-and-hovers>`_ directly to the editor, with for example, blame annotations (author, date and message from the current line's most recent commit) at the end of the current line, and much more
  - And a lot more!

- `Git Graph <https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph>`_ displays a graphical representation of the repository, from which you can also do most the git commands.


.. _git_ref:

References
-------------

.. rubric:: General presentations

-  `Pro Git book <https://git-scm.com/book/en/v2>`__ by Scott Chacon and Ben Straub, free and available in several languages.
-  `Introduction to Git with Scott Chacon of GitHub <https://www.youtube.com/watch?v=ZDR433b0HJY>`__ on YouTube.
-  An interesting discussion on Quora: `What is git and why should I use it? <https://www.quora.com/What-is-Git-and-why-should-I-use-it>`__.

.. _git_references_specific_discussions:

.. rubric:: Specific discussions

-  Discussions on why you need to add and commit `here <https://stackoverflow.com/questions/49228209/whats-the-use-of-the-staging-area-in-git>`__ and `there <https://stackoverflow.com/questions/4878358/why-would-i-want-stage-before-committing-in-git>`__.
-  Several possible workflows for teams are described `here <https://www.atlassian.com/git/tutorials/comparing-workflows>`__ by Atlassian.
-  Lists of GUIs `here <https://git-scm.com/downloads/guis>`__.

.. rubric:: Other references

-  `Tutorial <https://infomath.pages.math.cnrs.fr/tutorial/git/>`__ of Infomath
-  multilingual interactive `git cheatsheet <http://ndpsoftware.com/git-cheatsheet.html>`_ 
- open source game `Oh My Git! <https://ohmygit.org>`_ 

.. rubric:: To go further

-  `Stashing <https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning>`__
-  `Submodules <https://git-scm.com/book/en/v2/Git-Tools-Submodules>`__
-  `Branches <https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell>`__

.. [#]
   The current default is ``master``, but git shows a message, when creating a repository, explaining this is subject to change, and it recommands to set the default name using ``git config --global init.defaultBranch <name>`` where ``<name>`` will be the new default name. I chose to use ``main``.
