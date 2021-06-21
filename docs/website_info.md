---
layout: default
title: Website Info
description: Why a website?
---

# Why a project website?

## Motivation

One of the core ideas around a project website was to gradually expose complexity to the reader (if that succeeded... I'm less sure).
That is to say, the front-page should contain ideally roughly the information / information density as found on a project poster. Casual readers
will then go no further than this page and should be left with enough information to get a full idea of the project. The next layer of complexity
is then the hyper-links present on the index page. These allow for ideally limitless if needed more detailed / nuanced discussions about certain details.
Especially in a project like this one which covers a relatively wide span of different complex ideas, and given the fundamental restriction that all readers will be
coming in which different backgrounds and interests, this format offers an optional more detailed look into any specific piece. The next release of complexity beyond this would
be hyper-links from hyper-links, where at this stage the level of detail starts to get closer and closer to code-level detail. 

A good example of this principle is perhaps the page on [resampling parcellations](./resample_parcellations.html),
which goes into about as much detail as possible without sharing actual code, and then also links to the actual code.
On the other hand, as the details around how parcellations were resampled will not be of interest to most readers,
this advanced topic will only be stumbled upon by someone first interested
on the [index page](.index.html) in learning more about the [different parcellations used](./parcellations.md)
and then from that page, someone interested in how existing parcellations were re-sampled
(then onto either the specific project code or links to external tools used here).
In this way complexity can still exist and be easily accessible
(versus in maybe a traditional publication where you have to download some supplementary materials pdf
50 pages long and scroll down to a section which may or may not include the details you are interested in).

## Drawbacks

One of the biggest drawbacks to creating a format like this is the extra work involved. As the website
is a collection of different distributed pages, it can contain a huge amount of text and therefore require a huge
amount of work to generate. The tension here is that some of these pages may never even be seen by another human... 


## How this site was created

Another seeming drawback is the technical skill / savvy-ness required to make a website. I'd argue this point
isn't actually a weakness though, and note the hosting and generation of pages for this website is actually quite simple.
The whole process can be done through github and through github's new modern UI nonetheless. Now there are
plenty of tutorials online for how to host sites through github pages and jekyll, but I'll share below briefly how
I did it. The process below assumes you have a github account and a repository already setup.

![tutorial](https://raw.githubusercontent.com/sahahn/parc_scaling/master/extra/Figures/tutorial.png)

First, just navigate to the settings pages of your github, then to the pages dropdown. From here,
select a github branch (typically master), then on the next tab the folder 'docs/'. Next, select a theme
from the Theme Chooser (I chose 'Cayman') - which will then take you to a file editor generating the index.md page,
but you can just commit this default for now without any changes.

This process with automatically generate for you the [docs/](https://github.com/sahahn/parc_scaling/tree/main/docs) folder,
and two files, [index.md](https://github.com/sahahn/parc_scaling/blob/main/docs/index.md) and
[_config.yml](https://github.com/sahahn/parc_scaling/blob/main/docs/_config.yml).

You can next customize the _config.yml file, for example for this page it looks like this:

```
    title: Performance Scaling for Structural MRI Surface Parcellations
    email: sahahn@uvm.edu
    description: A Machine Learning Analysis in the ABCD Study
    source: docs/
    markdown: kramdown
    permalink: /:year/:title:output_ext
    theme: jekyll-theme-cayman
```

You can edit files directly from github, for example:

![tutorial](https://raw.githubusercontent.com/sahahn/parc_scaling/master/extra/Figures/tutorial2.png)

Next, you can begin generating you website by changing the index.md page and optionally adding other pages
in the [docs/](https://github.com/sahahn/parc_scaling/tree/main/docs) folder. Feel free to view the code for
this project, (e.g., [index.md](https://raw.githubusercontent.com/sahahn/parc_scaling/main/docs/index.md)) as
an example.

Your project site will be updated every time you push a new commit to the master branch. To find
the url generated for your site, check the page where you setup the pages earlier (Settings/ -> Pages/) or
just try https://YOUR_GITHUB_USERNAME.io/YOUR_GITHUB_REPO_NAME/.

That's about it, as page content can be written just in markup. I will share a few last tips though:

- To host and then share images, one easy way is to just upload the image you want to display anywhere
  in your github repository. Then you can find a link to this image under:
   
  https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_GITHUB_REPO_NAME/master/FILE_PATH

  For example, the screenshot above was uploaded under extra/Figure/tutorial2.png, so the file path for the
  image itself is: https://raw.githubusercontent.com/sahahn/parc_scaling/master/extra/Figures/tutorial2.png which can then be displayed via the markdown image syntax as:

  ```
  [image label](https://raw.githubusercontent.com/sahahn/parc_scaling/master/extra/Figures/tutorial2.png)
  ```

- HTML can be used directly in the markdown documents for advanced users, also pages written in HTML can be placed in
  under a folder called [docs/_includes/](https://github.com/sahahn/parc_scaling/tree/main/docs/_includes) and then be
  inserted into a page!
   
  For example I auto-generate an html table of statistics and save it to
  [docs/_includes/stats_example.html](https://github.com/sahahn/parc_scaling/tree/main/docs/_includes/stats_example.html).
  Then with code:

  \{% include stats_example.html %}

  That table can be inserted directly into the current page.