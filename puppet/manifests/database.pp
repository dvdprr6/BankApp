#
# Database setup
#
class psql_db{
	class{'postgresql::globals':
		manage_package_repo => trye,
		encoding => 'UTF8',
		version => '9.3'
	} ->
	class{'postgresql::server':
		listen_addresses => '*',
		postgres_password => 'bot'
	} ->
	postgresql::server::db{'bank':
		user => 'postgres',
		password => postgresql_password('postgres', 'bot'),
		encoding => 'UTF8'
	}
}

include psql_db