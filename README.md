# debian-ujcv-assets
UJCV Debian distro assets and configuration files.

To install manually:
- wget
- git
- papirus-icon-theme
- adw-gtk3
- python3
- bleachbit
- python3-tk
- gnome-tweaks
- ttf-mscorefonts-installer
- cmus
- gdu
- timeshift
- dconf-editor
- htop
- celluloid
- rar
- unrar
- firejail
- gparted
- gnome-disk-utility
- speedtest

But first:
```bash
sudo apt-add-repository contrib non-free -y
```
then:

```bash
sudo apt update && sudo apt upgrade
```

`nano .bashrc`:
```bash
# Fix PATH
PATH=$PATH:/home/pi/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/pi/.local/bin:
```

Command:
```sh
sudo apt install wget git papirus-icon-theme python3 bleachbit python3-tk gnome-tweaks ttf-mscorefonts-installer cmus gdu timeshift dconf-editor htop celluloid rar unrar firejail gparted gnome-disk-utility speedtest-cli
```
