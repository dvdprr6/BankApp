#
# install python3
#

class python3{
	exec{"untar-python":
		command => 'tar xJf Python-3.4.2.tar.xz',
		cwd => '/home/vagrant',
		creates => '/home/vagrant/Python-3.4.2',
		user => vagrant
	}->
	exec{"configure-python":
		command => 'sh configure --prefix=/opt/python3.4',
		cwd => '/home/vagrant/Python-3.4.2',
		user => vagrant
	}->
	exec{"install-python":
		command => 'make && make install',
		cwd => '/home/vagrant/Python-3.4.2',
		user => root
	}
}