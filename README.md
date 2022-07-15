# Verificate Backend

> ## Table of contents

- [Technologies](#technologies)
- [Repo Setup](#repo-setup)
- [Setting up the project](#setting-up-the-project)
- [Run the FastAPI server](#run-the-fastapi-server)
- [Pre-commit and lint the Backend](#pre-commit-and-lint-the-backend)
- [Status](#status)
- [Contributors](#contributors)
- [Contributing to the project](#contributing-to-the-project)

#

> ## Technologies

<p align="justify">
*Note: This project was setup and developed on a system running Windows 10. The stacks used for the project include:
</p>

| <b><u>Stack</u></b> | <b><u>Usage</u></b>   |
| :------------------ | :-------------------- |
| **`Python 3.10`**   | Programming language. |
| **`FastAPI`**       | APIs                  |
| **`MongoDB`**       | External Database     |

#

> ## Repo Setup

<p align="justify">
To setup the repo, first fork the verificate-BE repo, then clone the forked repository to create a copy on the local machine.
</p>

    $ git clone https://github.com/{github-username}/verificate-BE.git

<p align="justify">
Change directory to the cloned repo and set the original verificate repository as the "upstream" and your forked repository as the "origin" using your terminal.
</p>

    $ git remote add upstream https://github.com/NestDevs/verificate-BE.git

#

> ## Setting up the project

<p align="justify">
The first step requires the download and installation of Python 3.10 and a check to confirm that pip and the necessary dependencies are properly installed.
</p>

<p align="justify">
After the installation of the Python program, setup the project environment with pip and virtualenv in the command prompt, powershell or  terminal. Virtualenv creates an isolated Python environment containing all the packages necessary for the project.
</p>

\*Note:

- This project was setup using the gitbash terminal. Some of the commands used may not
  work with command prompt or powershell.

* If a "pip command not found error" is encountered, download get-pip.py and run
  `phython get-pip.py` to install it.

###

    $ pip install virtualenv

Navigate to the cloned local project folder. Create a virtual environment folder and
activate the environment by running the following commands in the terminal.

###

    $ python -m venv venv
    $ source venv/scripts/activate

<p align="justify">
After cloning the forked repository, the project is now ready to be installed. Install the dependencies using pip.
</p>

###

    $ (venv) pip install -r requirements.txt

Install all the necessary dependencies for the project. A couple of them are listed
below.

| <b><u>Modules</u></b> | <b><u>Usage</u></b>            |
| :-------------------- | :----------------------------- |
| **`motor`**           | Connection to mongodb database |
| **`coverage`**        | Testing code coverage          |

An exhaustive list can be found in the requirements.txt file included in this project.

#

> ## Run the FastAPI server

- Change directory to the project folder.

      $ cd verificate-BE (Backend folder)

- Create a .env file in config and specify variables for system environment using the
  sample.env file.

- Run the server using the following command.

      $ uvicorn main:app --reload

> ## Pre-commit and lint the Backend

Pre-commit hook is used to lint the code before every commit. Please fix the linting
errors before pushing to the repository.

- Change directory to the project folder.

      $ cd verificate-BE (Backend folder)

- Install the pre-commit hook using the following command.

      $ pre-commit install

- Run the pre-commit hook using the following command.

      $ pre-commit run

#

> ## Status

- This project is a work in progress and is currently under development.

#

> ## Contributors

This Project was created by the members of NestDevs for the Nestcoin Hackaton.

#

> ## Contributing to the project

If you find something worth contributing, please fork the repo, make a pull request and
add valid and well-reasoned explanations about your changes or comments.

Before adding a pull request, please note:

- It should be inviting and clear.
- Any additions should be relevant.
- It should be easy to contribute to.
- Urls marked **\*** are temporarily unavailable. Don't delete it from your code without
  confirming that it has permanently expired.

This repository is not meant to contain everything. Only good quality verified
information.

All **`suggestions`** are welcome!

> ##### Readme created by **`Pauline Banye`**
