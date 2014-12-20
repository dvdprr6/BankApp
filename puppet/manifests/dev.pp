#
# Setup the dev environment
#


Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] }

class bankwebapp{
	file{"/etc/rc.d/init.d/bankwebapp":
		ensure => 'link',
		target => '/vagrant/server/conf/bankwebapp',
		owner => root,
		mode => '755'
	}->
	file{"/etc/bank/":
		ensure => 'directory'
	}->
	exec{"download-python3":
		command => 'wget -q http://www.python.org/ftp/python/3.4.2/Python-3.4.2.tar.xz --no-check-certificate',
		cwd => '/home/vagrant/',
		creates => '/home/vagrant/Python-3.4.2.tar.xz',
		user => vagrant,
		timeout => 0
	}
}

include bankwebapp
include system-update
include python3