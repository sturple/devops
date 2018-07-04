# Devops Docker

## Setup
* git clone https://github.com/sturple/devops.git
* ln -s /my-directory/devops/.dockerfunc ~/.dockerfunc
* add to .bashrc or .bash_profile

```bash
if [ -f ~/.dockerfunc ] ; then
	. ~/.dockerfunc
fi
```
* ``source ~/.bashrc`` or `` source ~/.bash_profile``

## Commands
### Reverse proxy
* Start reverse proxy ```rev_porxy```
### Mysql
* Start /restart mysql ```mysql_start``` user ``root`` password ``r@nD0m7772``
* Stop mysql ```mysql_stop```
* start mysql command line server ``mysql``

### Phpmyadmin
* starts phpmyadmin ``phpmyadmin``

### Wordpress
* starts/creates wordpress multi site ```wordpress_multisite [sitename]```
* starts/creates wordpress site ```wordpress [sitename]```