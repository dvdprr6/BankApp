#
# system related libraries
#

class system-update{
	exec{'yum update':
		command => 'yum update -y',
		timeout => 0
	}
	$sysPackages = [
		"curl",
		"wget",
		"openssl-devel",
		"nodejs",
		"nodejs-devel",
		"npm",
		"sqlite-devel",
		"sqlite",
		"postgresql",
		"postgresql-devel"
	]
	package{$sysPackages:
		ensure => "latest",
		require => Exec['yum update']
	}
}