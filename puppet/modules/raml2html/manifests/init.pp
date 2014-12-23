#
#	install raml2html
#

class raml2html{
	$bank_path = '/usr/local/bin/:/usr/local/:/usr/bin/:/bin/:/opt/python3.4/bin'
	exec{"install-raml2html":
		command => 'npm install -g raml2html',
		cwd => '/home/vagrant',
		path => $bank_path,
		user => root
	}
}