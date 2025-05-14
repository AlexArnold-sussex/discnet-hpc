<div align="center">
  <a href="https://github.com/jschewts/discnet-hpc">
    <img src=".images/discnet-logo.png" alt="Logo" height="100">
  </a>

  <h3 align="center">HPC Exercises</h3>
  <p align="center">
    This set of exercises covers all the essential skills needed to work with an HPC system hence I like to call them the 12 labours that turn you into a HPCules with the divine IT powers of a well-trained HPC user.
  </p>
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Exercises</summary>
  <ol>
    <li><a href="#logging-in">Logging In</a></li>
    <li><a href="#verify-server">Verify Server</a></li>
    <li><a href="#ssh-key-authentication">SSH Key Authentication</a></li>
    <li><a href="#edit-a-simple-textfile">Edit a simple textfile</a></li>
    <li><a href="#modules">Modules</a></li>
    <li><a href="#examine-job-queues">Examine job queues</a></li>
    <li><a href="#run-an-interactive-job">Run an interactive job</a></li>
    <li><a href="#submit-a-batch-jobs">Submit a batch job</a></li>
    <li><a href="#advanced-batch-jobs">Advanced batch jobs</a></li>
    <li><a href="#first-openmp-program">First OpenMP Programm</a></li>
    <li><a href="#first-mpi-program">First MPI Programm</a></li>
    <li><a href="#final-challenge">Final challenge</a></li>
  </ol>
</details>

<p align="right">(<a href="#top">back to top</a>)</p>

# ACCESSING THE SYSTEM

## Logging in

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
| **IMPORTANT:** While access via a remote CLI shell (e.g. via *ssh*/*sftp*) is quite common for HPC systems, web interfaces like Open OnDemand are still far less common. Hence, for all the following exercises, try to find the solution using just *ssh* as well, even if the GUI provides you with it in a more convenient way here on Artemis. |

<p align="right">(<a href="#top">back to top</a>)</p>

## Verify Server

Artemis like most other servers uses the S(ecure)SH(ell) protocol to allow users to work on it from a remote computer. The connection is encrypted to ensure that nobody can intercept and alter the commands sent to Artemis or the output sent back to the user once the connection is established. But one of the weak spots in the system is to ensure that you are actually connected to the right server. So-called 'Man-in-the-middle' attacks can reroute your connection through a third server which then works as a relay between you and your target, but listens and potentially alters data exchanged between the user and Artemis.

This is why a digital fingerprint is provided when you log into a server. If you haven't logged on to the server before from your current computer, this fingerprint will be presented to you and you need to confirm its authenticity.
```
The authenticity of host 'ood.artemis.hrc.sussex.ac.uk (139.184.83.139)' can't be established.
ED25519 key fingerprint is SHA256:PKwtJhSEWIKR6BpymogIcfp6TQGlItVUNqu9DeK7Ssw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? 
```

Confirm this to complete the log-in. Now we have to verify that the presented fingerprint actually belongs to the target server we wanted to log into (and not to some 'man-in-the-middle' relay eavesdropping on our connection). To do so, simply type into the command line on the login server :-
```
[artemis]$ ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

It should present you an output like
```
256 SHA256:PKwtJhSEWIKR6BpymogIcfp6TQGlItVUNqu9DeK7Ssw root@artemis-login-0.local (ED25519)
```

In case that the server uses a different key type (e.g. created with another cryptographic algorithm like RSA or ECDSA), check the */etc/ssh* on the host for a public key with that algorithm in the name.

Once you have logged in for the first time, this fingerprint will be stored on your local computer and you should never be asked about it again as long as the login server does not change (e.g. by reinstallation). If you want to display the fingerprint of the key used in a connection after your first login, you can simply add the option *-o VisualHostKey=yes* to your ssh call (on Linux/Unix) or use
```
ssh-keygen -l -F ood.artemis.hrc.sussex.ac.uk
```
to extract the fingerprint from your local known_host file.

If the locally stored key differs with the one provided by the server on a login, you may see an error message like this:
```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
SHA256:zELprgvBZmyQRQ5/6/a58e3e660bR3lJZItu18pnZcg.
Please contact your system administrator.
Add correct host key in $HOME/.ssh/known_hosts to get rid of this message.
Offending RSA key in $HOME/.ssh/known_hosts:24
RSA host key for ood.artemis.hrc.sussex.ac.uk has changed and you have requested strict checking.
Host key verification failed.
```
If you are not aware of any reinstallation of the login servers that may have triggered this change of fingerprint, please be VERY cautious here and contact the support team of the system in question immediately. If you happen to know that the fingerprint has changed then follow the instructions and remove the fingerprint in question from the $HOME/.ssh/known_hosts file on your computer. When you log in know, the login server should be treated as a previously unknown server and you will be presented with the new fingerprint that you can then verify as described above. 

### Exercises

- check that the ssh key for Artemis stored in your system / returned by ssh on login matches the key on the Artemis login server

<p align="right">(<a href="#top">back to top</a>)</p>

## SSH key authentication

This exercise covers how to generate an SSH key on your own machine that can then be used to authenticate your connection to a target machine like the Artemis login node. While SSH key generation does not require you to set a passphrase, for important security reason most HPC systems do require its users to only use keys protected with a reasonably strong passphrase. Users who are not obeying this may be held responsible for any damage caused as a result.

### Windows

If you are using a Windows desktop, you can use tools like PuTTygen, which is part of the PuTTY software package.

Instructions for using PuTTygen can be found here.

### Linux / macOS

If you are using a Linux or macOS desktop then use the command
```
$ ssh-keygen -t rsa -b 4096
```
Try not to use less than 4096 bits to ensure that your key is strong enough.

When prompted make sure you use a secure pass phrase. You should see output similar to:-

```
Generating public/private rsa key pair.
Enter file in which to save the key ($HOME/.ssh/id_rsa):
Created directory ‘$HOME/.ssh’.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in $HOME/.ssh/id_rsa.
Your public key has been saved in $HOME/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:2MTKd1MxNd40BLd8yY5HQrZJ/YgVBVMkL48b/Wp1A/w juser@server
The key’s randomart image is:
+—[RSA 2048]—-+
| o*@X=|
| . ++BO+|
| o o*oB=|
| . = ..o*=o|
| + S o .=oo|
| . . . .E+|
| ..+|
| .. |
| .. |
+—-[SHA256]—–+
```
You can find the private/public key pair at the location you defined at its creation. You can identify the public key by its suffix ‘.pub’. 


### Exercises

- Generate a new ssh key pair that is protected by a passphrase
- Find out how to use that keypair to log into Artemis instead of using your password (hint: there is a ''manual'' way, but also a useful command that you can run on your own machine to perform this more conveniently)
- Find out how to add the ssh key to a key agent on your machine to avoid having to unlock it every time with the passphrase (many OS and their ssh clients already support that feature by default, so check if you can actually skip this step)

<p align="right">(<a href="#top">back to top</a>)</p>

## Edit a simple text file

While more complex coding usually happens off the HPC systems, you will often have to make final tweaks to some code or configuration files. There are a number of different text editors usually available on most HPC systems.

### SSH

From the command line you can use *vim*, *nano* or *emacs* (in non-window mode). All of them are very powerful but there is a bit of a learning curve. The man pages, “cheat sheets” and youtube videos can be used to find more details, in particular on commands and keyboard shortcuts.

```
$ vim
```

### Remote Desktop

In windows mode you can use the terminal mode editors or you can use editors that have a GUI. Besides emacs in its (default) window mode, other more “notepad-like” editors like gedit are also available on Artemis. You can invoke these editors from the terminal within the remote desktop environment e.g.

```
$ gedit
```

### Exercise

Linux applications often use (hidden) dot files. These are files located in your $HOME that start with a dot, eg: .bashrc. These are sometimes referred to as startup files which contain information used by a particular application when its starts.

- Use an editor of your choice to edit the file $HOME/.bashrc.
  Modify the following line:

  ```
  PS1="(HPC Training)[\u@\h\[\e[1;34m\](artemis)\[\e[0m\] \W]\$"
  ```

- once added execute the following:
  ```
  $ source $HOME/.bashrc
  $ ls
  ```
  Do you see a difference in your prompt?

- log out and in again. Do you see the same changes now? Why not and how can you make sure that these changes are applied on log in as well (hint: check for a second hidden bashrc config file in your home directory and find out what it is for)?

<p align="right">(<a href="#top">back to top</a>)</p>

# SOFTWARE

## Modules

There are a large number of pre-installed applications, libraries and compilers on Artemis. Access to these packages is via a tool called *module*. More information on Artemis modules can be found <a href="">here</a>. You can also use the help page:

module help

To see all available modules or packages try:
module av

### Exercise

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
  $ module load <name>
  ```
  where you replace the name of the module. This loads the module for R which adds the respective application folder containing the binary of the application to the search path of your shell ($PATH).
  ```
  $ echo $PATH
  ```
  Check this before and after loading/unloading the module.
- Now try running R from the command line again. This time the “R” environment should start. Use quit() to close it and to return to your shell.
- Log out and log back in. Trying running R again. You will notice that R is missing from your $PATH again.
- Check the module man page (man module) or help page (module help) to find the command that will save your current collection as a default and makes it available again to be restored every time you log in (hint: check a previous exercise on where to make those changes)

<p align="right">(<a href="#top">back to top</a>)</p>


# JOB HANDLING

## Examine job queues

The login servers are configured to run relatively small programs. These include editors, browsers, small compilations etc. Larger programs must be executed on a compute node (or compute server). Work is submitted to the compute nodes as a "job" via a "queue". Once a job is submitted the "scheduler" and "resource" managers will start the job on the most suitable compute node(s) when appropriate. Often this is immediate but if the load is heavy the job will be "queued" to be executed at a later time when the required resources become available. Each partition has its own queue.

### Exercise

The commands to examine the partitions and associated job queues are called *sinfo* and *squeue* (hint: <a href="https://curc.readthedocs.io/en/latest/running-jobs/squeue-status-codes.html">this page here</a> summarizes all Job States and Reasons and may be very useful)<a. Additionally, *sstat* can be used to display various status information of a running job and *sacct* to inspect any jobs that finished in the past. Use their man pages to find out how to do the following:

- Find out the state of the nodes in each partition (are there any dysfunctional nodes? If so, what are the reasons?)
- Show all running jobs
- Show all queued jobs just for a specific user (e.g. you)
- Show all past jobs run on Artemis by a specific user and check whether they completed successfully, the walltime and the maximum amount of memory used by that job. Your output should look like this:
  ```
  JobID           JobName      User  Partition     MaxRSS MaxRSSNode    Elapsed    CPUTime      State 
  ------------ ---------- --------- ---------- ---------- ---------- ---------- ---------- ---------- 
  1061361            bash    js2347    general                         00:02:01   00:04:02  COMPLETED 
  1061361.ext+     extern                               0 artemis-a+   00:02:01   00:04:02  COMPLETED 
  1061361.0          bash                          81372K artemis-a+   00:01:59   00:03:58  COMPLETED
  ```
- Show the nodes being currently used by (any) specific running job
- Show a summary of each of the queues
- Show all running & queued jobs for a (any) specific queue

*Remark*: Some of these task can also be done on Artemis using the OpenOnDemand web portal (so try to use for this as well), But in general, you won't have such GUIs available, henceit is important to know how to use these CLI tools.  

<p align="right">(<a href="#top">back to top</a>)</p>

## Run an interactive job

In this exercise we will run some simple “R” commands interactively on a compute node.

### Exercises
- First we need to allocate resources (here 1 task/core by default) on a compute node and run a shell on it:
  ```
  $ srun -p discnet --pty bash
  ```
  The terminal should respond similar to:
  ```
  srun: job 1060981 queued and waiting for resources
  srun: job 1060981 has been allocated resources
  ```
  Your terminal is blocked until the resources become available. Use the squeue command in another terminal/ssh login and identify your interactive job and verify the partition it is queued for.
  Once the requested resources are available, a new shell opens on one of the requested node.

- Ensure you have the “R” module loaded in this shell. If not, then load it as you have learned in a previous exercise.

- In the terminal run the R program. Execute the following commands (a file with these command can be found in the training/scripts directory):
  ```
  Square <- function(x)
  { return(x^2) }
  print(Square(4))
  print(Square(x=4)) # same thing
  quit()
  ```
- Confirm that you see output similar to:

  ```
  R version 3.4.1 (2017-06-30) — “Single Candle”
  Copyright (C) 2017 The R Foundation for Statistical Computing
  Platform: x86_64-pc-linux-gnu (64-bit)

  R is free software and comes with ABSOLUTELY NO WARRANTY.
  You are welcome to redistribute it under certain conditions.
  Type ‘license()’ or ‘licence()’ for distribution details.

  R is a collaborative project with many contributors.
  Type ‘contributors()’ for more information and
  ‘citation()’ on how to cite R or R packages in publications.

  Type ‘demo()’ for some demos, ‘help()’ for on-line help, or
  ‘help.start()’ for an HTML browser interface to help.
  Type ‘q()’ to quit R.

  [Previously saved workspace restored]

  Square <- function(x)
  + { return(x^2) }
  > print(Square(4))
  [1] 16
  > print(Square(x=4)) # same thing
  [1] 16
  > quit()
  Save workspace image? [y/n/c]: n
  ```

- Exit from the interactive shell by typing exit or EOF/EOT interrupt via CTRL-D.

- Repeat requesting an interactive shell, but this time use *screen* to keep the request open while you clone the terminal you are logged in with, log back in again and recover that screen (hint: instead of simply closing the shell, you can also log out properly, but you have to make sure to *detach*, **NOT** terminate the screen then)

<p align="right">(<a href="#top">back to top</a>)</p>

## Submit a batch job

In this exercise we will run our simple R commands as a batch job. As with the interactive job in the previous exercise we use the sbatch command. Full documentation on sbatch can be found in the system’s man pages (man sbatch) or its online documentation. The usual way to submit a batch job is to create a job script. The lines starting with “#SBATCH” are called directives and map to the sbatch arguments that could be used on the command line. Here is an example job script:
```
#!/usr/bin/env bash
#
#SBATCH --job-name=training_batch
#SBATCH --partition=discnet
#SBATCH --ntasks=1
#SBATCH --time=1:00

echo $SLURM_JOB_NAME
echo "Current working directory is `pwd`"
echo "Starting run at: `date`"

module purge
module load R

srun R -f training/src/square.r

# output how and when job finished
echo "Program finished with exit code $? at: `date`"
# wait for a few more seconds before closing this job (to make it easier for you to observe it; do not use in production)
sleep 10
# end of jobscript
```
The job will create an output file and an error file. These will be created in the working directory by default.

### Exercise

- Cut and paste the above example into a file called “batch-job.sh” in your $HOME . Submit the job:

- cd $HOME; sbatch batch-job.sh

- Use the squeue command to confirm the status of the job.

- Look for and examine the output file and check its content. Try to modify your submission script to tell SLURM to write the output and errors (technically, the stdout & stderr streams) into separate files and to store it into the training/logs folder.

- Look in the sbatch documentation to find out how to resubmit the job on hold. The job will appear in the queue with status PD and the reason (JobHeldUser).

- Release the job (hint: *scontrol*) and confirm it runs.

<p align="right">(<a href="#top">back to top</a>)</p>

## Advanced batch jobs

### Arrays

The best and recommended way to submit many jobs (>100) is using SLURM’s jobs array feature. The job arrays allow managing big number of jobs more effectively and faster. To specify job array use --array as follows:

Tell SLURM how many jobs you will have in array:

  --array=0-9. There are 10 jobs in array. The first job has index 0, and the last job has index 9.
  --array=5-8. There are 4 jobs in array. The first job has index 5, and the last job has index 8.
  --array=2,4,6. There are 3 jobs in array with indices 2, 4 and 6.

Now you can write a job submission script that looks like:
```
#!/usr/bin/env bash
#
#SBATCH --job-name=training_batch
#SBATCH --partition=discnet
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00
#SBATCH --output=test_%A_%a.out
#SBATCH --array=1-3

echo $SLURM_JOB_NAME
echo $SLURM_ARRAY_TASK_ID
# wait for a random amount of time up to 10 seconds
sleep $((RANDOM % 10))
```

### Dependencies

Often we develop pipelines where a particular job must be launched only after previous jobs were successully completed. SLURM provides a way to implement such pipelines with its --dependency option:

  --dependency=afterok:<job_id>. Submitted job will be launched if and only if job with job_id identifier was successfully completed. If job_id is a job array, then all jobs in that job array must be successfully completed.
  --dependency=afternotok:<job_id>. Submitted job will be launched if and only if job with job_id identifier failed. If job_id is a job array, then at least one job in that array failed. This option may be useful for cleanup step.
  --dependency=afterany:<job_id>. Submitted job wil be launched after job with job_id identifier terminated i.e. completed successfully or failed.

### Exercise

- Copy and paste the above example into a file called “array-job.sh” in your $HOME. Submit the job:
  ```
  $ cd $HOME; sbatch array-job.sh
  ```

- Look for and examine the output files to check the content. Modify the script to run 6 array jobs and check the status on the queue. (squeue -r or scontrol show job jobid)

- The output should be similar to:

- Now submit the script to run 20 array jobs but with only 5 at a time.
  ```
  sbatch --array [1-20]%5 array-job.sh
  ```
  Check the status of your job. If some of your jobs are still queued cancel the remainder. Check the output files to see how many of the array jobs ran.
  ```
  scancel <job_id>
  ```

- Finally, submit a batch job to run an array of 1-10 and submit another batch job of array 11-20 which will only run if the first array jobs complete successfully.
  ```
  sbatch --array [1-10] array-job.sh
  sbatch --dependency=afterok:jobid --array [11-20] array-job.sh
  ```
  Check the status of your job on the queue. Did the first array of jobs work and has the second array run?

<p align="right">(<a href="#top">back to top</a>)</p>


## First OpenMP Program

In this example we will compile an OpenMP executable in an interactive shell and then submit a job to the batch queue.

### Exercise

- Create an interactive jobs with 6 cores allocated on the same node by executing the following command:
  ```
  srun -p discnet --ntasks=1 --cpus-per-task=6 --pty bash
  ```
- Now select the modules you will need for this exercise:-
  ```
  $ module purge; module load system/intel64 intel_comp/2019.2
  ```
  From the command line check which modules this has loaded (*module list*). Now change into the “$HOME/training/src” directory and look at the file “openmp.c” . Try to understand the structure of the code.

- Compile this file and create an executable to be stored in the “bin” directory:
  ```
  $ icc -fopenmp -o ../bin/openmp.exe openmp.c
  ```
  Check that you now have an openmp.exe in the bin directory.

- Try to the program using the 6 cores we have allocated:
  ```
  cd $HOME/training/bin; ./openmp.exe
  ```
  The output should be similar to:

  ```
  Hello World from thread = 0
  Hello World from thread = 2
  Number of threads = 16
  Hello World from thread = 5
  Hello World from thread = 13
  Hello World from thread = 1
  Hello World from thread = 4
  Hello World from thread = 6
  Hello World from thread = 8
  Hello World from thread = 9
  Hello World from thread = 12
  Hello World from thread = 10
  Hello World from thread = 11
  Hello World from thread = 14
  Hello World from thread = 3

  All threads finished. Back to single thread.
  ```

- Notice that the program actually used more than 6 cores. By default, OpenMP is trying to use all cores available on the same node. Thus we need to be able to limit the number of cores used. Set the following environmental variable and rerun the program:
  ```
  $ export OMP_NUM_THREADS=6; ./openmp.exe
  ```
  The output should now be something like:
  ```
  Hello World from thread = 0
  Number of threads = 6
  Hello World from thread = 5
  Hello World from thread = 3
  Hello World from thread = 2
  Hello World from thread = 1
  Hello World from thread = 4

  All threads finished. Back to single thread.
  ```
  Exit from the interactive shell back onto the login node. Check that you are in your home directory ( cd ).

- Submit the same program as a batch job. Using the knowledge from the previous exercises, try to write your own batch script to do so and store it in “training/scripts/” (hint: if you get stuck, you can find a commented solution in “training/scripts/openmp-job.sh.solution“). Now submit the job:
  ```
  $ sbatch training/scripts/openmp-job.sh
  ```

- Use *squeue* to monitor the job. When the job has completed locate and examine the output file(s). The contents of the output files should be similar to the interactive output.

<p align="right">(<a href="#top">back to top</a>)</p>

## First MPI Program

In this example we will compile an MPI executable in an interactive shell and then submit a job to the batch queue.

### Exercise

- Create an interactive shell with 6 cores, but instead of *srun* use *salloc* (this allows us to then use srun to bootstrap the mpi processes on the allocated nodes; notice that the new shell is still running on the login node, but anything you start with the *srun* command will run on the compute nodes!)
  ```
  $ salloc --ntasks=6 -p discnet
  ```
  All allocated cores are not necessary on the same node as the shell you are provided with now. Try to find out if/which other nodes are used as well (hint: squeue).

- Now select the modules you will need for this exercise:
  ```
  module purge; module load intel OpenMPI
  ```
  From the command line confirm that all the requested modules have been successfully loaded (hint: module list).

- Now change into the “$HOME/training/src” directory and look at the file "mpi.c" . Try to understand the structure of the code.
  We will now compile this file and create an executable to be stored in the "bin" directory:
  ```
  $ mpicc mpi.c -o ../bin/mpi.exe
  ```
  Ignore any warnings. Check that you now have an mpi.exe in the bin directory.

- We will now run the program using all 6 cores we have allocated:
  ```
  $ cd $HOME/training/bin; srun --mpi=pmi2 mpi.exe
  ```
  On slurm, srun should be used instead of mpirun that usually does the bootstrapping of the processes across the allocated nodes. Also notice that we haven’t told srun explicitly to use our 6 cores. If no number of tasks is specified, it uses all allocated cores automatically.

  The output should be similar to:
  ```
  Hello world from process 0 of 6
  Hello world from process 1 of 6
  Hello world from process 2 of 6
  Hello world from process 3 of 6
  Hello world from process 4 of 6
  Hello world from process 5 of 6
  ```
  Once finished, exit from the interactive job back onto the login node. Check that you are in your home directory (cd).

- We will now submit the same program as a batch job. Again, using the knowledge from the previous exercises, try to write your own batch script to do so and store it in "training/scripts/" (hint: if you get stuck, you can find a commented solution in "training/scripts/mpi-job.sh.solution"). Then submit the job:
  ```
  $ sbatch training/scripts/mpi-job.sh
  ```
  Use squeue to check the status of the job. When the job has completed locate and examine the output file.
  The contents of the output file should be similar to the interactive output.

<p align="right">(<a href="#top">back to top</a>)</p>

# FINAL CHALLENGE

## Your first HPC simulation

With all what you learned so far, you should be now able to compile, set up and run your first HPC simulation. We have picked GADGET-4, an N-Body cosmological simulation code.

## Exercise

1. Download the latest version of GADGET-4 from <a href="https://wwwmpa.mpa-garching.mpg.de/gadget4/">here</a> onto Artemis (Tip: *git* is your friend ;))
2. Locate the source code folder with the Makefile/Config template, adapt the Makefile for the Artemis environment as use the Config template as it is.
3. Identify all required modules and load them
4. Successfully compile the GADGET-4 binary
5. You can find a parameter file for running a simulation in the tutorial folder: Exercises/HPC/Gadget-4
6. Write your own submission script for a 64 core MPI run of your compiled GADGET-4 binary (don’t forget to load the modules here as well; hint: best store them in a configuration for that)
7. Check if your simulations started successfully
8. Now kill your simulation again (Do **NOT** skip this step!)
9. ????
10. Profit!!! (well, you may not have achieved demi-godhood now, but mastered the content of the first day successfully. Congratulation :))

<p align="right">(<a href="#top">back to top</a>)</p>
