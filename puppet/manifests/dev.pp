#
# Setup the dev environment
#


Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] }

class bank-webapp{
	file{"/etc/rc.d/init.d/bankwebapp":
		ensure => 'link',
		target => '/vagrant/server/conf/bankwebapp',
		owner => root,
		mode => '755'
	}->
	file{"/etc/bank/":
		ensure => 'directory'
	}
}
include bank-webapp
include python3
include system-update
include nginx