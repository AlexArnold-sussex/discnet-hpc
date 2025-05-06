<div align="center">
  <a href="https://github.com/jschewts/discnet-hpc">
    <img src="images/discnet-logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">HPC Exercises #1</h3>
  <p align="center">
    This first set of exercise will get you logged into Artemis
  </p>
</div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Exercises</summary>
  <ol>
    <li><a href="#login">Login</a></li>
    <li><a href="#ssh-key">Create/Deploy SSH key</a></li>
    <li><a href="#ssh-fingerprint">Verify Server</a></li>
    <li><a href="#summary">Summary</a></li>
  </ol>
</details>

<p align="right">(<a href="#top">back to top</a>)</p>

# Login

## Background
<p>
Access to the Artemis Hybrid Research Cluster (HRC) is expected to be primarily be via your browser or ssh client, and if off campus, using the VPN. If you currently do not have access to the VPN - you will need to request as such, and to be added to the relevant departmental group in Palo Alto. It is assumed you either have access now, or are on campus.
</p>

<p>
On Artemis, there is one URL for both the webfrontend as well as the SSH server: ood.artemis.hrc.sussex.ac.uk
</p>

## Exercises

- Log into Artemis via both your webbrowser (via the Open OnDemand Web Portal) & familiarize yourself with the landing page (check <a href="https://artemis-docs.hpc.sussex.ac.uk/artemis/access.html#open-ondemand">HERE</a> for additional information)
      - upload a file via the *Files* tab to your home directory
      - open a Jupyter notebook server
      - check the *Jobs* tab to find your running jupyter notebook server and terminate it there again

- Log successfully into Artemis via your SSH client (via *ssh* command on terminal in Linux/Unix/macOS or PuTTY on Windows)
      - find the file you uploaded via the web interface and delete it again

