FROM dorowu/ubuntu-desktop-lxde-vnc:focal

# Configure apt
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 78BD65473CB3BD13
# Install dependencies
RUN apt-get update && apt-get install -y \
git \
make \
build-essential \
libreadline8 libreadline-dev \
libglfw3 libglfw3-dev \
python3 \
python3-pip \
python3-tk \
gnome-terminal \
netcat

# Launcher
COPY Portfolio.py /root/Desktop/Portfolio.py
ENV DISPLAY=:1.0

# Download all proyects
RUN git clone https://github.com/pablobn/minishell.git Desktop/minishell && \
	git clone https://github.com/SergioDiazDev/So_long.git Desktop/so_long  && \
	git clone https://github.com/SergioDiazDev/cube.git Desktop/cube  

# Definimos el comando por defecto
COPY start.sh /root/Desktop/start.sh
RUN chmod +x /root/Desktop/start.sh
CMD ["./root/Desktop/start.sh"]
