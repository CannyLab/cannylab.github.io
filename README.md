Cannylab Website Portal
=========================

[![Build Status](https://travis-ci.org/CannyLab/cannylab.github.io.svg?branch=master)](https://travis-ci.org/cannylab/cannylab.github.io)

Simple website portal based on https://github.com/square/square.github.io

Development
-----------

### Run the site locally
```bash
gem install bundler # first time only
bundle install # first time only
bundle exec jekyll serve
```

Adding a Project
-----------

Here are the steps to add projects, datasets or other content:

1. Open the index.html file. There are two clearly marked sections for adding list items for datasets and projects
2. Fill out the template:
```html
<div class="menu-item-info">
  <h4 class="menu-item-name"> PROJECT NAME </h4>
  <span class="menu-item-price"><a href="https://github.com/cannylab/project_github_link"
      target="_blank">GitHub</a></span>
  <p class="menu-item-description" style="height:auto"> PROJECT NAME </p>
  <img src="/repo_images/project_image.png" style="width: 100%;">
</div>
```
3. Add any required images to the `repo_images` folder.