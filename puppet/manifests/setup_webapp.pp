#
# setup the webapp
#

class setup_webapp{
	$bank_path = '/usr/local/bin/:/usr/local/:/usr/bin/:/bin/:/opt/python3.4/bin'
	exec{"install-grunt-cli":
		command => 'npm install -g grunt-cli',
		cwd => '/home/vagrant',
		path => $bank_path,
		user => root
	}->
	exec{"install-bower":
		command => 'npm install -g bower',
		cwd => '/home/vagrant/',
		path => $bank_path,
		user => root
	}->
	exec{"install-nodemodules":
		command => 'npm install',
		cwd => '/vagrant',
		creates => '/vagrant/node_modules',
		path => $bank_path,
		user => root,
		timeout => 0
	}->
	exec{"install-bower_components":
		command => 'bower install',
		cwd => '/vagrant',
		creates => '/vagrant/app/bower_components',
		path => $bank_path,
		user => vagrant,
		timeout => 0
	}
}

include setup_webapp
include raml2html