<p align="center">
  <img src="https://github.com/hi-cli/hi-cli/blob/master/hi-cli.png?raw=true" alt="hi-cli">
</p>

# hi-cli
hi-cli is an open source, community-driven framework for managing your script...

### Prerequisite
hi-cli is running on bash (v3.0 or higher), for Windows user, please install [MSYS2](http://www.msys2.org/) or [Git for Windows (v2.13.0 or higher)](https://git-scm.com/download/win)

For Chinese users, please download Git for Windows form [here](https://npm.taobao.org/mirrors/git-for-windows/2.13.0.windows.1/Git-2.13.0-64-bit.exe)

### Basic Installation

hi-cli is installed by running one of the following commands in your terminal. You can install this via the command-line with either `curl` or `wget`.

#### via curl

```shell
bash -c "$(curl -fsSL bash -c "$(curl -fsSL https://raw.githubusercontent.com/hi-cli/hi-cli/master/bin/install)"
```

#### via wget

```shell
bash -c "$(wget https://raw.githubusercontent.com/hi-cli/hi-cli/master/bin/install -O -)"
```

## Using hi-cli

```
hi [module] [command] [options]
```

## Examples

### Update hi-cli
```bash
hi update
```

### Install hi-cli package [cicd](https://github.com/hi-cli/hi-cicd)
```bash
hi package install cicd
```

### Update hi-cli package [cicd](https://github.com/hi-cli/hi-cicd)
```bash
hi package update cicd
```
(for more available packages, please find out [here](https://github.com/hi-cli?tab=repositories))
