<div align="center">
  <a href="https://github.com/jschewts/discnet-hpc">
    <img src="images/discnet-logo.png" alt="Logo" height="100">
  </a>

  <h3 align="center">HPC Exercises</h3>
  <p align="center">
    This set of exercise will ...
  </p>
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Sections</summary>
  <ol>
    <li><a href="#accessing-the-system">Accessing the system</a></li>
    <li><a href="#software">Software</a></li>
    <li><a href="#job-handling">Job Handling</a></li>
    <li><a href="#summary">Summary</a></li>
  </ol>
</details>

<p align="right">(<a href="#top">back to top</a>)</p>

# ACCESSING THE SYSTEM

## Login

<p>
Access to the Artemis Hybrid Research Cluster (HRC) is expected to be primarily be via your browser or ssh client, and if off campus, using the VPN.
On Artemis, there is one URL for both the webfrontend as well as the SSH server: 
```
ood.artemis.hrc.sussex.ac.uk
```
</p>

### Exercises

- Log into Artemis via both your webbrowser (via the Open OnDemand Web Portal) & familiarize yourself with the landing page (check <a href="https://artemis-docs.hpc.sussex.ac.uk/artemis/access.html#open-ondemand">HERE</a> for additional information)
  - upload a file via the *Files* tab to your home directory
  - open a Jupyter notebook server
  - check the *Jobs* tab to find your running jupyter notebook server and terminate it there again

- Log successfully into Artemis via your SSH client (via *ssh* command on terminal in Linux/Unix/macOS or PuTTY on Windows)
  - find the file you uploaded via the web interface and download it (hint: you can use e.g. *scp*, *sftp* or a graphical FTP client that you run on your own computer. Try various ways and find out which one works best for you.)

|  ⚠️ Notice ⚠️  |
| :-----------: |
| **IMPORTANT:** While access via a remote CLI shell (e.g. via *ssh*/*sftp*) is quite common for HPC systems, web interfaces like Open OnDemand are still far less common.|
| Hence, for all the following exercises, try to find the solution using just *ssh* as well, even if the GUI provides you with it in a more convenient way here |
| on Artemis. |


## Verify Server

### Background
<p>
When connecting to a remote server, there is always the chance that your connection gets intercepted and listened upon despite the connection being encrypted (''man-in-the-middle'' attack). In this exercise, we will guide you through the steps to verify that the connection is indeed secure.
</p>


### Exercises



## Create/Deploy/Use SSH keys

### Background


### Exercises


## Edit a simple text file

### Background
While more complex coding usually happens off the HPC systems, you will often have to make final tweaks to some code or configuration files. There are a number of different text editors usually available on most HPC systems.

### SSH

From the command line you can use *vim*, *nano* or *emacs* (in non-window mode). All of them are very powerful but there is a bit of a learning curve. The man pages, “cheat sheets” and youtube videos can be used to find more details, in particular on commands and keyboard shortcuts.

```
$ vim
```

### Remote Desktop

In windows mode you can use the terminal mode editors or you can use editors that have a GUI. Besides emacs in its (default) window mode, other more “notepad-like” editors like gedit are also available on Artemis. You can invoke these editors from the command line within the remote desktop environment e.g.

```
$ gedit
```

### Exercise

Linux applications often use (hidden) dot files. These are files located in your $HOME that start with a dot, eg: .bashrc. These are sometimes referred to as startup files which contain information used by a particular application when its starts.

- Use an editor of your choice to edit the file $HOME/.bashrc.
  Add the following line:

  ```
  PS1="(Training)[\u@\h\[\e[1;34m\](artemis)\[\e[0m\] \W]\$"
  ```

- once added execute the following:
  ```
  source $HOME/.bashrc
  ls
  ```
  Do you see a difference in your prompt?

  NB: The cd command by itself returns you to $HOME (i.e. home directory). 


# SOFTWARE

## Modules

There are a large number of pre-installed applications, libraries and compilers on Artemis. Access to these packages is via a tool called *module*. More information on Artemis modules can be found <a href="">here</a>. You can also use the help page:

module help

To see all available modules or packages try:
module av

### Exercises

- Try running the statistical computing environment called “R” . Type the following on the command line:
  ```
  $ R
  ```
  An error message will be displayed:
  ```
  bash: R: command not found
  ```

- Now find the correct module name for the latest version of R available on Artemis (hint: use *module spider*) and load it.
  ```
  module load <name>
  ```
  where you replace the name of the module. This loads the module for R which adds the respective application folder containing the binary of the application to the search path of your shell ($PATH).
  ```
  echo $PATH
  ```
  Check this before and after loading/unloading the module.
- Now try running R from the command line again. This time the “R” environment should start. Use quit() to close it and to return to your shell.
- Log out and log back in. Trying running R again. You will notice that R is missing from your $PATH again.
- Check the module man page (man module) or help page (module help) to find the command that will save your current collection as a default and makes it available again every time you log in (hint: you will have to add the command to restore it to your *.bash_profile* to trigger it)


# JOB HANDLING

## Examine the job queues

The login servers are configured to run relatively small programs. These include editors, browsers, small compilations etc. Larger programs must be executed on a compute node (or compute server). Work is submitted to the compute nodes as a "job" via a "queue". Once a job is submitted the "scheduler" and "resource" managers will start the job on the most suitable compute node(s) when appropriate. Often this is immediate but if the load is heavy the job will be "queued" to be executed at a later time when the required resources become available. Each partition has its own queue.

### Exercises

The commands to examine the partitions and associated job queues are called *sinfo* and *squeue*. Additionally, *sstat* can be used to display various status information of a running job. Use their man pages to find out how to do the following:

- Find out the state of the nodes in each partition (are there any dysfunctional nodes? If so, what are the reasons?)
- Show all running jobs.
- Show all queued jobs just for a specific user.
- Show the nodes being currently used by (any) specific running job.
- Show a summary of each of the queues.
- Show all running & queued jobs for a (any) specific queue.




