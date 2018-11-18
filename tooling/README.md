# How to use this environment.yml with Anaconda.
## A conda environnment for Udacity's PyTorch Challenge.

Install [Anaconda](https://www.anaconda.com/download/) for your OS if you don't already have it installed.

Download the environment.yml in this folder. You can clone it from this repo or copy it into a text file and save it where you know you can find it.
Open a terminal and navigate to where you saved the file.

Run the command `conda env create -f environment.yml`

This should download some packages. 

You should now be able to `conda activate udacity` (or the [appropriate command](https://conda.io/docs/user-guide/tasks/manage-environments.html?highlight=environment%20yml#activating-an-environment) for your OS) and have a fully loaded environment with PyTorch and Jupyter Notebooks.

I recomment running `jupyter notebook` to ensure the above was successful.

If you run into any problems please open an issue here or reach out to me in the course Slack!

More information about managing Anaconda environments [here](https://conda.io/docs/user-guide/tasks/manage-environments.html?highlight=environment%20yml#).
