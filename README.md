##Oracle Enterprise Linux##
To add the Oracle Enterprise Linux vagrant box run `vagrant box add oel65-64 https://storage.us2.oraclecloud.com/v1/istoilis-istoilis/vagrant/oel65-64.box`

##Puppet Provisioning##
In order to provision the database run 'git submodule init ; git submodule update'


Untar each of these packages and copy them to puppet/modules/ with the names `postgresql`, `stdlib`, `apt`, and `concat`, respectively. This naming convention is important so each packages can find each others classes.