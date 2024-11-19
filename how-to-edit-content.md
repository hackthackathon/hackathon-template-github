# How to Edit Content

All of the content for this template is built from markdown, a plain text format that is used to build the web content!

For more on markdown, please see this [markdown tutorial](https://www.markdowntutorial.com/)

## Editing Content on Github

If you are interested in editing the content directly on the github website, please see [this tutorial](https://docs.github.com/en/get-started/start-your-journey/hello-world) that walks through Github

## Editing Content Locally

If you are interested in editing/rendering this content locally, please follow these steps:

1. Move into your directory of the content

```bash
cd hackathon-template-github
```

2. Install a conda environment using the environment file*

* if you are new to conda environments, please see this [getting started with conda content from the software carpentries](https://edcarp.github.io/introduction-to-conda-for-data-scientists/02-working-with-environments/index.html)

```bash
conda env create -f environment.yml
conda activate hackathon-template-github-dev
```

3. Build your content locally using myst (and open the link returned)

```bash
myst start
```

Running this command will start up your website, which should look something like:
```👉  http://localhost:3000  👈```

4. Edit your content

Now, you can open your README.md in your editor of choice, and add/remove/change the content, which will render immediately within your browser.
