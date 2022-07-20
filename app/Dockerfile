# syntax=docker/dockerfile:1
#FROM node:12-alpine
#RUN apk add --no-cache python2 g++ make
#WORKDIR /app
#COPY . .
#RUN yarn install --production
#CMD ["node", "src/index.js"]
#EXPOSE 3000

# docker build -t getting-started .
# docker run -dp 3000:3000 getting-started

FROM nvidia/cuda:11.7.0-devel-ubuntu22.04

# FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

# docker pull nvidia/cuda:11.7.0-devel-ubuntu22.04

# https://hub.docker.com/layers/cuda/nvidia/cuda/11.7.0-devel-ubuntu22.04/images/sha256-16c790bc3349d70a0416cf8bf1eef9b40433ee907018b5ea32bdbddf75433a9d?context=explore

# old
# RUN apt-get update -y && apt install -y python3 git && wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && pip install jupyter

# new w/ wget
#RUN apt-get update -y && apt-get install -y wget && apt install -y python3 git && wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && pip install jupyter

# new w/ wget & disutils
RUN apt-get update -y && apt-get install -y wget && apt install -y python3 git && apt-get install -y python3-distutils && wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && pip install jupyter

# and then you could clone the github repo in question and `pip install -r requirements.txt' from there

# NO WGET ERROR
#8 27.77 Setting up openssh-client (1:8.9p1-3) ...
#8 27.81 update-alternatives: using /usr/bin/ssh to provide /usr/bin/rsh (rsh) in auto mode
#8 27.81 update-alternatives: warning: skip creation of /usr/share/man/man1/rsh.1.gz because associated file /usr/share/man/man1/ssh.1.gz (of link group rsh) doesn't exist
#8 27.81 update-alternatives: using /usr/bin/slogin to provide /usr/bin/rlogin (rlogin) in auto mode
#8 27.81 update-alternatives: warning: skip creation of /usr/share/man/man1/rlogin.1.gz because associated file /usr/share/man/man1/slogin.1.gz (of link group rlogin) doesn't exist
#8 27.81 update-alternatives: using /usr/bin/scp to provide /usr/bin/rcp (rcp) in auto mode
#8 27.81 update-alternatives: warning: skip creation of /usr/share/man/man1/rcp.1.gz because associated file /usr/share/man/man1/scp.1.gz (of link group rcp) doesn't exist
#8 27.82 Setting up libxext6:amd64 (2:1.3.4-1build1) ...
#8 27.83 Setting up python3 (3.10.4-0ubuntu2) ...
#8 27.83 running python rtupdate hooks for python3.10...
#8 27.83 running python post-rtupdate hooks for python3.10...
#8 27.89 Setting up xauth (1:1.1-1build2) ...
#8 27.90 Processing triggers for libc-bin (2.35-0ubuntu3) ...
#8 27.93 /bin/sh: 1: wget: not found
#------

# NEW ERROR AFTER INSTALLING WGET
#8 43.97 2022-07-14 16:51:43 (5.74 MB/s) - 'get-pip.py' saved [2680354/2680354]
#8 43.97
#8 44.89 Traceback (most recent call last):
#8 44.89   File "//get-pip.py", line 33593, in <module>
#8 44.89     main()
#8 44.89   File "//get-pip.py", line 135, in main
#8 44.89     bootstrap(tmpdir=tmpdir)
#8 44.89   File "//get-pip.py", line 111, in bootstrap
#8 44.89     monkeypatch_for_cert(tmpdir)
#8 44.89   File "//get-pip.py", line 92, in monkeypatch_for_cert
#8 44.89     from pip._internal.commands.install import InstallCommand
#8 44.89   File "/tmp/tmpctgs0zwy/pip.zip/pip/_internal/commands/__init__.py", line 9, in <module>
#8 44.89   File "/tmp/tmpctgs0zwy/pip.zip/pip/_internal/cli/base_command.py", line 15, in <module>
#8 44.89   File "/tmp/tmpctgs0zwy/pip.zip/pip/_internal/cli/cmdoptions.py", line 24, in <module>
#8 44.89   File "/tmp/tmpctgs0zwy/pip.zip/pip/_internal/cli/parser.py", line 12, in <module>
#8 44.89   File "/tmp/tmpctgs0zwy/pip.zip/pip/_internal/configuration.py", line 26, in <module>
#8 44.89   File "/tmp/tmpctgs0zwy/pip.zip/pip/_internal/utils/logging.py", line 29, in <module>
#8 44.89   File "/tmp/tmpctgs0zwy/pip.zip/pip/_internal/utils/misc.py", line 42, in <module>
#8 44.89   File "/tmp/tmpctgs0zwy/pip.zip/pip/_internal/locations/__init__.py", line 14, in <module>
#8 44.89   File "/tmp/tmpctgs0zwy/pip.zip/pip/_internal/locations/_distutils.py", line 9, in <module>
#8 44.89 ModuleNotFoundError: No module named 'distutils.cmd'
#------

# disutils?
#8 89.54 The following additional packages will be installed:
#8 89.54   python3-lib2to3
#8 89.55 The following NEW packages will be installed:
#8 89.55   python3-distutils python3-lib2to3
#8 89.56 0 upgraded, 2 newly installed, 0 to remove and 28 not upgraded.
#8 89.56 Need to get 214 kB of archives.
#8 89.56 After this operation, 1067 kB of additional disk space will be used.
#8 89.56 Do you want to continue? [Y/n] Abort.
#------
