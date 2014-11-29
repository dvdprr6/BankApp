##Puppet Provisioning##
In order to provision the database, these packages are needed
1. puppetlabs-postgres-4.1.0
2. puppetlabs-stdlib-4.4.0
3. puppetlabs-apt-1.7.0
4. puppetlabs-concat-1.1.2

You can get these using `wget` as such:
`wget http://forge.puppetlabs.com/system/releases/p/puppetlabs/puppetlabs-postgresql-4.1.0.tar.gz`
`wget http://forge.puppetlabs.com/system/releases/p/puppetlabs/puppetlabs-stdlib-4.4.0.tar.gz`
`wget http://forge.puppetlabs.com/system/releases/p/puppetlabs/puppetlabs-apt-1.7.0.tar.gz`
`wget http://forge.puppetlabs.com/system/releases/p/puppetlabs/puppetlabs-concat-1.1.2.tar.gz`

Untar each of these packages and copy them to puppet/modules/ with the names `postgresql`, `stdlib`, `apt`, and `concat`, respectively. This naming convention is important so each packages can find each others classes.