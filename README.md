# Heroku - Nmap

Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

- What is [Heroku]
- Heroku [filesystem]

## Features

- Get output from nmap as html report 

## Tech

Heroku nmap deployed with a following tools:

- [flask] - Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

- [Python] - Python is a programming language that lets you work quickly
and integrate systems more effectively.

- [xsltproc] - Command line tool for applying XSLT stylesheets to XML documents.

- [nmap] - free and open source utility for network discovery and security auditing.

## Installation

#### Git clone
 - Clone project from git repository
```bash
git clone https://github.com/NikitaKovaljov/Heroku-Nmap.git
```

#### Heroku init
- Inside cloned project folder, type:

```bash
heroku login -i
1. cd myapp
2. heroku init
3. git add .
4. git commit -m "test"
```
### Buildpacks
Heroku - nmap requires several buildpacks:
- heroku/python
- heroku-community/apt
- heroku-buildpack-nmap

### Install buildpacks:

- Login to heroku if you are not. 
- and in your open session in cli, copy&paste following lines, where [app_name] is the name of your app.

#### heroku/python

```bash
heroku buildpacks:set heroku/python -a app_name
```

#### heroku-community/apt

```bash
heroku buildpacks:add --index 1 heroku-community/apt -a app_name
```

#### heroku-buildpack-nmap

```bash
heroku buildpacks:add --index 1 https://github.com/socialpaymentsbv/heroku-buildpack-nmap.git -a app_name
```

## explanation

| buildpack | Why |
| ------ | ------ |
| heroku/python | Specify, that our app is written on a python |
| heroku-community/apt | To be able, to download additional tools, with aptfile |
| heroku-buildpack-nmap | To be able, to scan targets |

## End

- After buildpacks installation, code changes - save everything and push:

```bash
git add .
git commit -m "test"
git push heroku master
```
- Now everything is ready for usage, welcome :)

## POC 

- link: https://dixin-cider.herokuapp.com/

> index.html page, button redirects to /nmap form 
![](https://github.com/NikitaKovaljov/Heroku-Nmap/blob/main/POC/index.png?raw=true)

> /nmap form, which sends params to our script
![](https://github.com/NikitaKovaljov/Heroku-Nmap/blob/main/POC/:nmap.png?raw=true)

> output from our requrest as html report
![](https://github.com/NikitaKovaljov/Heroku-Nmap/blob/main/POC/result.png?raw=true)

## Limitations

- Heroku using containers to build apps, thus using sudo arguments for nmap is not allowed, but you always can try to escalate privileges and get root shell. 

## License
MIT

   [flask]: <https://palletsprojects.com/p/flask/>
   [Python]: <https://www.python.org/>
   [xsltproc]: <https://linux.die.net/man/1/xsltproc>
   [nmap]: <https://nmap.org/>
   [Heroku]: <https://www.heroku.com/what>
   [filesystem]: <https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem>

