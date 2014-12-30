class nginx{
	file{"/etc/nginx":
		ensure => 'directory'
	}->
	file{"/etc/nginx/conf.d/bank.conf":
		ensure => 'link',
		target => '/vagrant/server/conf/dev/nginx.conf',
		owner => root
	}->
	exec{"restart-nginx":
		command => 'service nginx start',
		cwd => '/home/vagrant',
		user => root
	}
}