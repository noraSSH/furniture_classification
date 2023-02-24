# Simple Flask application for furniture image classfication using CNN model

Created on: 2023.02.22

**Background:**
This project aims at performing classification tasks on furniture images with target classes of [bed, chair, sofa] using a given dataset of 300 images, as well as implementing a user-friendly API for users to access this prediction functionality.  

## Table of Contents

- [Sections] (#sections)
- [Description] (#description)
- [Installation](#installation)
  - [Docker](#Docker)
  - [Anaconda](#Anaconda)
  - [requirements.txt](#requirements.txt)
- [Usage](#usage)

## Sections

## Description

The application deploys a Deep Learning model which utilizes the transfer learning functionality of PyTorch framework. It combines the feature extrator of ResNet50 from torch.models with a customized fully-connected layer to perform the final classification. The model achieves a high validation accuracy of 97.78% on the validation set.

To provide users access to the model, the application provides two API: 1. users can get prediction result by running a Python script; 2. users can run a Flask application, upload an image and then get the predict result. Detailed instructions could be found in [Installation](#installation)

The project implements CI/CD pipeline using Github Action which enables the building of Docker images everytime a push or pull request happens. This effectively increases the working efficiency for this project.

 - app.py: the Flask application
 - Dockerfile: Docker config file
 - model.ipynb: the jupyter notebook to train & output the CNN model
 - model_resnet50.pt: the CNN model used for image classification
 - predict.py: the Python script used for predicting the class of given image
 - requirements.txt: records of dependencies
 - templates/: stores the html files for rendering in the Flask application
 - static/uploads: stores the uploaded images

## Installation
### Docker
_Note: the stable version of Docker image is: norassh98/norarepo:v0.6
To run the application through Docker, you can run the following commands on your terminal:
```markdown
  docker image pull norassh98/norarepo:v0.6
  docker run -it -p 5000:5000 norassh98/norarepo:v0.6
```
Make sure Docker is installed on your machine.

### terminal
You can also run python app.py to start the application if your environment satisfies the dependencies in requirements.txt.

To run predict.py, make sure that your environment satisfies the dependencies in requirements.txt. This script outputs prediction on a single image in the terminal with the following command:
```markdown
  python predict.py *path_to_image*
```

## Usage
_Note: as the CNN model is quite large (exceeding 90M), the setup and running speed might be slow. Please be patient with the application.

The main page of the Flask application has an upload input form and a submit button. Click on "Choose File" to choose the image you want to test:
![Alt text](img/First.PNG?raw=true "main page")

![Alt text](img/Second.PNG?raw=true "upload image")

After the image is uploaded, click on "Submit" and wait for the application to analyze the results.
![Alt text](img/Third.PNG?raw=true "submit the image for analysis")

Here comes the result!
![Alt text](img/Four.PNG?raw=true "Result!")









**Suggestions:**
- Use [gh-description](https://github.com/RichardLitt/gh-description) to set and get GitHub description.
- Use `npm show . description` to show the description from a local [npm](https://npmjs.com) package.

### Long Description
**Status:** Optional.

**Requirements:**
- Must not have its own title.
- If any of the folder, repository, or package manager names do not match, there must be a note here as to why. See [Title section](#title).

**Suggestions:**
- If too long, consider moving to the [Background](#background) section.
- Cover the main reasons for building the repository.
- "This should describe your module in broad terms,
generally in just a few paragraphs; more detail of the module's
routines or methods, lengthy code examples, or other in-depth
material should be given in subsequent sections.

  Ideally, someone who's slightly familiar with your module should be
able to refresh their memory without hitting "page down". As your
reader continues through the document, they should receive a
progressively greater amount of knowledge."

  ~ [Kirrily "Skud" Robert, perlmodstyle](http://perldoc.perl.org/perlmodstyle.html)

### Table of Contents
**Status:** Required; optional for READMEs shorter than 100 lines.

**Requirements:**
- Must link to all Markdown sections in the file.
- Must start with the next section; do not include the title or Table of Contents headings.
- Must be at least one-depth: must capture all `##` headings.

**Suggestions:**
- May capture third and fourth depth headings. If it is a long ToC, these are optional.

### Security
**Status**: Optional.

**Requirements:**
- May go here if it is important to highlight security concerns. Otherwise, it should be in [Extra Sections](#extra-sections).

### Background
**Status:** Optional.

**Requirements:**
- Cover motivation.
- Cover abstract dependencies.
- Cover intellectual provenance: A `See Also` section is also fitting.

### Install
**Status:** Required by default, optional for [documentation repositories](#definitions).

**Requirements:**
- Code block illustrating how to install.

**Subsections:**
- `Dependencies`. Required if there are unusual dependencies or dependencies that must be manually installed.

**Suggestions:**
- Link to prerequisite sites for programming language: [npmjs](https://npmjs.com), [godocs](https://godoc.org), etc.
- Include any system-specific information needed for installation.
- An `Updating` section would be useful for most packages, if there are multiple versions which the user may interface with.

### Usage
**Status:** Required by default, optional for [documentation repositories](#definitions).

**Requirements:**
- Code block illustrating common usage.
- If CLI compatible, code block indicating common usage.
- If importable, code block indicating both import functionality and usage.

**Subsections:**
- `CLI`. Required if CLI functionality exists.

**Suggestions:**
- Cover basic choices that may affect usage: for instance, if JavaScript, cover promises/callbacks, ES6 here.
- If relevant, point to a runnable file for the usage code.

### Extra Sections
**Status**: Optional.

**Requirements:**
- None.

**Suggestions:**
- This should not be called `Extra Sections`. This is a space for 0 or more sections to be included, each of which must have their own titles.
- This should contain any other sections that are relevant, placed after [Usage](#usage) and before [API](#api).
- Specifically, the [Security](#security) section should be here if it wasn't important enough to be placed above.

### API
**Status:** Optional.

**Requirements:**
- Describe exported functions and objects.

**Suggestions:**
- Describe signatures, return types, callbacks, and events.
- Cover types covered where not obvious.
- Describe caveats.
- If using an external API generator (like go-doc, js-doc, or so on), point to an external `API.md` file. This can be the only item in the section, if present.

### Maintainer(s)
**Status**: Optional.

**Requirements:**
- Must be called `Maintainer` or `Maintainers`.
- List maintainer(s) for a repository, along with one way of contacting them (e.g. GitHub link or email).

**Suggestions:**
- This should be a small list of people in charge of the repo. This should not be everyone with access rights, such as an entire organization, but the people who should be pinged and who are in charge of the direction and maintenance of the repository.
- Listing past maintainers is good for attribution, and kind.

### Thanks
**Status**: Optional.

**Requirements:**
- Must be called `Thanks`, `Credits` or `Acknowledgements`.

**Suggestions:**
- State anyone or anything that significantly helped with the development of your project.
- State public contact hyper-links if applicable.

### Contributing
**Status**: Required.

**Requirements:**
- State where users can ask questions.
- State whether PRs are accepted.
- List any requirements for contributing; for instance, having a sign-off on commits.

**Suggestions:**
- Link to a CONTRIBUTING file -- if there is one.
- Be as friendly as possible.
- Link to the GitHub issues.
- Link to a Code of Conduct. A CoC is often in the Contributing section or document, or set elsewhere for an entire organization, so it may not be necessary to include the entire file in each repository. However, it is highly recommended to always link to the code, wherever it lives.
- A subsection for listing contributors is also welcome here.

### License
**Status:** Required.

**Requirements:**
- State license full name or identifier, as listed on the  [SPDX](https://spdx.org/licenses/) license list. For unlicensed repositories, add `UNLICENSED`. For more details, add `SEE LICENSE IN <filename>` and link to the license file. (These requirements were adapted from [npm](https://docs.npmjs.com/files/package.json#license)).
- State license owner.
- Must be last section.

**Suggestions:**
- Link to longer License file in local repository.

## Definitions

_These definitions are provided to clarify any terms used above._

- **Documentation repositories**: Repositories without any functional code. For instance, [RichardLitt/knowledge](https://github.com/RichardLitt/knowledge).