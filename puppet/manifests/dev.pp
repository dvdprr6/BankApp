Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] }

class bankwebapp{
	file{"/etc/rc.d/init.d/bankwebapp":
		ensure => 'link',
		target => '/vagrant/bankwebapp',
		owner => root,
		mode => '755'
	} ->
	file{"/etc/bank/":
		ensure => 'directory'
	} ->
	file{"/home/vagrant/Python-3.3.5.tar.xz":
		ensure => 'file',
		source => 'file:///mnt/python/Python-3.3.5.tar.xz',
		owner => vagrant
	} ->
	file{"/home/vagrant/setuptools-7.0.tar.gz":
		ensure => 'file',
		source => 'file:///mnt/python/setuptools-7.0.tar.gz',
		owner => vagrant
	}
}

include bankwebapp
include system-update
include python3