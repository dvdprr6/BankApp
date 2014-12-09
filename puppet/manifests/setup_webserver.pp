#
# setup the webserver
#

class setup_bank_webapp{
	$bank_path = '/usr/local/bin/:/usr/local/:/usr/bin/:/bin/:/opt/python3.3/bin'
	exec{"python-env":
		command => '/opt/python3.3/bin/python3.3 -m venv /home/vagrant/bankEnv',
		cwd => '/home/vagrant',
		path => $bank_path,
		user => vagrant,
	}->
	exec{"install-setuptools":
		command => 'curl https://bootstrap.pypa.io/ez_setup.py -o - | /home/vagrant/bankEnv/bin/python',
		cwd => '/home/vagrant/',
		path => $bank_path,
		user => vagrant,
		timeout => 0
	}->
	exec{"install-pip":
		command => '/home/vagrant/bankEnv/bin/easy_install pip',
		cwd => '/home/vagrant/',
		path => $bank_path,
		user => vagrant,
		timeout => 0
	}->
	exec{"install-requirements":
		command => '/home/vagrant/bankEnv/bin/pip install -r requirements.txt',
		cwd => '/vagrant/server',
		path => $bank_path,
		user => vagrant,
		timeout => 0
	}->
	exec{"setup":
		command => '/home/vagrant/bankEnv/bin/python setup.py develop',
		cwd => '/vagrant/server',
		path => $bank_path,
		user => vagrant,
		timeout => 0
	}->
	file{"/etc/bank/bank.conf":
		ensure => "file",
		source => "file:///vagrant/server/conf/dev/bank.conf"
	}->
	exec{"init-database":
		command => '/home/vagrant/bankEnv/bin/python scripts/initdb.py --config=/etc/bank/bank.conf',
		cwd => '/vagrant/server',
		path => $bank_path,
		user => vagrant
	}->
	exec{"python-at-startup":
		command => 'echo ". /home/vagrant/bankEnv/bin/activate" >> /home/vagrant/.bashrc',
		cwd => '/home/vagrant/',
		path => $bank_path,
		user => vagrant
	}
}

include setup_bank_webapp