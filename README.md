# Visual Studio Code .env file does not provide access to PYTHONPATH

## Update

I have updated my test source `test_PYTHONPATH.py` to allow it to trap library and environment access exceptions.

Please note the difference between the vscode 'run' and 'debug' results. You may see different effects depending on history of establishing the content of the `.env` file.
I don't think there is an automatic update of the environment when .env is edited. I have seen it scanned when I changed the python environment to another and back again, otherwise the edits dont seem to have an effect.

## Links

https://github.com/microsoft/vscode/issues/94338

files are in github repository https://github.com/pjgoodall/test_vscode_env

## Problem

I expect to be able to import from modules with subdirectories of the vscode `workplaceFolder`. 
If I try to append to PYTHONPATH using the environment file: `${workspaceFolder}/.env`, I get an empty reference to PYTHONPATH within that file. I therefore cannot add the path to my modules to PYTHONPATH from `${workspaceFolder}/.env`

I do not want to hard-code a manipulation of the environment into my python source.

This may be an interaction complexity between vscode and conda virtual environments

## References

* [conda - Creating an environment from a yml file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
* [How do I find out my python path using python?](https://stackoverflow.com/questions/1489599/how-do-i-find-out-my-python-path-using-python)
* [Setting the Python path for local project in VS Code without using the settings.json file](https://stackoverflow.com/questions/56825741/setting-the-python-path-for-local-project-in-vs-code-without-using-the-settings)

### vscode documentation
* [Where the extension looks for environments](https://code.visualstudio.com/docs/python/environments#_where-the-extension-looks-for-environments)
* [Environment variable definitions file](https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file)
* 

## Files:

1. `test_PYTHONPATH.py` python code which tests access to environment variables - particularly PYTHONPATH altered in `${workspaceFolder}/.env` 
2. `environment.yml` used to create working [conda virtual python environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
4. `python_modules` - a directory I want to be on my PYTHONPATH so I can import modules from within it.
5. `README.md` - this file
6. `Screenshot from 2020-04-03 15-34-53.png` -  vscode screenshot showing settings related to `${workspaceFolder}/.env`