FROM dorowu/ubuntu-desktop-lxde-vnc:latest

RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 78BD65473CB3BD13
# Download all proyects
RUN apt-get update && apt-get install -y \
git \
make \
build-essential

RUN git clone https://github.com/pablobn/minishell.git
