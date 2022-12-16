.. _sec-ssh:

SSH
###

The Secure Shell (SSH) protocol is a network protocol that allows secure access to systems running an SSH server over a network (e.g. the Internet). All the communications from the client (e.g. your workstation for example) to the server (e.g. a remote workstation) are encrypted.

SSH is widely used, examples of applications are 

- accessing severs remotely (student workspace hosted by the school, supercomputers, :ref:`sec-git` servers, remote workstation, ...) with or without password,
- transferring or syncing files,
- mounting a directory on a remote server as a local filesystem.

SSH client and server are present on most operating systems, including macOS, most distributions of Linux, and even (recent) versions of Windows.

Access to a remote computer
---------------------------

To access a remote computer via ssh, the administrator of the server needs to set up your account. You should have a username and a password.

.. _sec-ssh-password:

Password-based authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SSH command to access a remote server with a password is as follows

.. code-block:: bash
    
    ssh username@hostname

where ``username`` is the username associated with your account on the remote computer and ``hostname`` is the name associated with the remote computer. The latter can be an IP address or a domain name.

This command will prompt you for your password (associated to your account on the remote computer), and will then open a terminal session on the remote computer.

.. note:: The first time you connect to a remote computer, it will ask you if you want to add the host to ``known_hosts``, which is a file you can find in ``~/.ssh``

.. only:: not latex
    
    .. asciinema:: ../_static/asciicast/ssh/password_output.cast
        :rows: 30

    In this example, ``hostname`` is used to get the current IP address. We log from ``172.17.0.3`` to ``172.17.0.2`` for the first time.

Key-based authentication
~~~~~~~~~~~~~~~~~~~~~~~~

Using SSH, there is an alternative to password-based authentication which uses a public key and a private key. More precisely, it uses an asymmetric encryption algorithm where the public key is used for encryption, and the private key is used for decryption.

The idea is that the user generates both keys, and send the *public* key to the remote computer. Then, each time the user wants to connect to the remote computer, the remote computer will "challenge" the user sending a message encrypted using the public key. The user will send back the decrypted message, which can only be done with the private key. Note this is done automatically behind the scenes using the same command as before.

This approach is usually considered safer than password-based authentication, mainly because the private key never leaves the user's workstation. But remark that if the private key is stolen (by someone accessing your workstation for example), then the remote computer is compromised (as compromised as if your password was stolen). That is why it is advised to add a layer of security by encrypting the private key itself with a passphrase, which is suggested when creating the keys.

Finally, this approach provides passwordless access to the remote computer, meaning you can access several times to the remote computer, without having to type your password each time.


.. rubric:: Creating private and public keys

To create a pair of public/private keys, you need to use the following command

.. code-block:: bash

    ssh-keygen


It will first ask you about the name of the file (default to ``~/.ssh/id_rsa``), and for a passphrase. Note that the latter is optional, if given, it is used to encrypt the private key adding a new layer of security. It will then create two files: ``~/.ssh/id_rsa`` and ``~/.ssh/id_rsa.pub`` by default, the first is the private key, and the second the public key.

.. only:: not latex

    .. asciinema:: ../_static/asciicast/ssh/create_key_output.cast

.. rubric:: Sending a public key to a remote computer

Once the pair of public and private keys is created, you need to send the *public* key to the remote computer. It can be done with the following command

.. code-block:: bash

    ssh-copy-id username@hostname

If the public key name differs from the default, add the flag ``-i path/to/my_id_rsa.pub``.

.. only:: not latex

    .. asciinema:: ../_static/asciicast/ssh/copy_key_output.cast

.. rubric:: Accessing a remote computer with key-based authentication

If the private key is not encrypted, in other words, if there is no passphrase, then you can connect to the remote computer using the same command as in :ref:`sec-ssh-password`, and it will not prompt you for your password.

If the private key is encrypted, each time you will try to connect, it will prompt you for the passphrase to use the private key. To avoid this and still have passwordless access to the remote computer, you can use ``ssh-agent`` that will cache the decrypted key for the rest of your terminal session.

You first need to call this command to set up ``ssh-agent``

.. code-block:: bash

    eval $(ssh-agent)

and then, you can cache a key using ``ssh-add``

.. code-block:: bash

    ssh-add ~/.ssh/id_rsa

In this manner, you can access the remote computer using ``ssh`` as before.

.. only:: not latex

    .. asciinema:: ../_static/asciicast/ssh/access_key_output.cast

.. _sec-ssh-configuration-file:

Configuration file
~~~~~~~~~~~~~~~~~~

If you want to avoid remembering all the usernames, domain names, and command-line options, you can set up a configuration file where you can write everything once.

This file does not exist by default, so first you need to create it

.. code-block:: bash

    touch ~/.ssh/config

The format of the configuration file is as follows

.. sourcecode:: 

    Host hostname1
        Option1 value
        Option2 value

    Host hostname2
        Option1 value

A minimal configuration file using our previous example with ``hostname`` as the host and ``username`` as the username gives 

.. sourcecode:: 

    Host my_host
        HostName hostname
        User username

With this configuration file, one can use ``ssh MyHost`` instead of ``ssh username@hostname``. Here we do not gain a lot since this is a simple example, but a configuration file can quickly be useful.

.. only:: not latex

    .. asciinema:: ../_static/asciicast/ssh/config_file_output.cast

Transferring files
------------------

Several file transfer mechanisms based on SSH exist. You can always use either password or key-base authentication, 

Secured copy protocol
~~~~~~~~~~~~~~~~~~~~~

``scp`` simply reads the source file and writes it to destination.

.. code-block:: bash

    scp local_file host:local_file_sent_to_remote
    scp host:remote_file remote_file_sent_to_local 

.. only:: not latex

    .. asciinema:: ../_static/asciicast/ssh/copy_output.cast

rsync
~~~~~

``rsync`` is highly configurable tool for copying files. It can be used locally, or over a network with SSH. One difference with ``scp`` is that it uses a "delta transfer algorithm", meaning in particular that only the difference between the source and target files will be sent.

It has many flags allowing for fine-tuning of its behaviour. Here are some:

- ``-a`` to keep almost [#]_ everything the same recursively.
- ``-u`` to *not* update if files at destination are newer.
- ``--progress`` to show the progress of the transfer


.. only:: not latex

    .. asciinema:: ../_static/asciicast/ssh/rsync_output.cast

    .. note:: Remark that when we try to send ``local_file.txt`` the second time, nothing is sent. This is because there is no difference between the local and remote versions of ``local_file.txt``.

SSH Bastion
-----------

Usually remote computers are not directly accessible from the Internet. You first need to access to a remote server (called "Bastion") from which you can access to a remote computer. It allows isolating a private network (where the remote computer is) from the Internet, making it only accessible via the Bastion.

To automate the process of first connecting to the bastion, and then to the remote computer, you can use the following command 

.. code-block:: bash

    ssh -J username@bastionname username@hostname

where ``bastion`` is the domain name of the SSH bastion. You can also use the following configuration file that defines the bastion host and the remote computer 

.. sourcecode:: 

    Host my_bastion
        HostName bastionname
        User username

    Host my_host
        HostName hostname
        User username
        ProxyJump my_bastion

You can then connect to the bastion using ``ssh my_bastion``, or directly to the remote computer with ``ssh my_host``. It will prompt you for your password twice if you use a password-based authentication, or you can send your public key to both remote servers to use key-based authentication.

.. only:: not latex

    .. asciinema:: ../_static/asciicast/ssh/bastion_output.cast

    In this example, we log from ``172.17.0.3`` to ``172.17.0.2`` via ``172.17.0.4`` usung key-based authentication.

Notes for VS Code users
-----------------------

VS Code has useful extensions to work on a remote computer.

- `Remote - SSH <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh>`_ can be used to open a folder on a remote computer running an SSH server. In practice, this will open a new VS Code window (workspace in VS Code jargon) where you can interact with the remote files and folders, open a terminal on the remote computer, and even install extensions. This way, one can work on this remote folder using all the usual VS Code features (intellisense, code navigation, debugging, and so on) as if it was local. I refer to its `documentation <https://code.visualstudio.com/docs/remote/ssh#_working-with-local-tools>`_, but note that it will find SSH targets defined in :ref:`sec-ssh-configuration-file`.
- `SSH FS <https://marketplace.visualstudio.com/items?itemName=Kelvin.vscode-sshfs>`_ is another alternative I use when the previous extension is not available, which can happen if the operating system on the remote computer is not supported. It mounts a remote filesystem as a local workspace folder. The integration with VS Code is not as advanced as with the previous extension since the workspace is local. Features like intellisense, code navigation, debugging will not work since it does not have access the remote environment, but basic features such as syntax highlighting should work and this is often enough.

References
----------

- Wikipedia for `Secure Shell <https://en.wikipedia.org/wiki/Secure_Shell>`_, `Secured copy protocol <https://en.wikipedia.org/wiki/Secure_copy_protocol>`_ and `rsync <https://en.wikipedia.org/wiki/Rsync>`_
- `Article <https://wiki.archlinux.org/title/SSH_keys>`_ on SSH keys from ArchWiki 
- StackExchange discussions on the subject can be found `here <https://security.stackexchange.com/questions/69407/why-is-using-an-ssh-key-more-secure-than-using-passwords>`_ and `here <https://security.stackexchange.com/questions/3887/is-using-a-public-key-for-logging-in-to-ssh-any-better-than-saving-a-password>`_ 
- StackOverflow discussion on `ssh vs rsync <https://stackoverflow.com/questions/20244585/how-does-scp-differ-from-rsync>`_ 

.. [#] The main exception concerns `hard links <https://en.wikipedia.org/wiki/Hard_link>`_, see documentation for more information.
