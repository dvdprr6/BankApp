##Oracle Enterprise Linux##
To add the Oracle Enterprise Linux vagrant box run 
`vagrant box add oel65-64 https://storage.us2.oraclecloud.com/v1/istoilis-istoilis/vagrant/oel65-64.box`

##Puppet Provisioning##
In order to provision the postgresql database run 
`git submodule init ; git submodule update`

References:
1. puppetlabs-stdlib `https://github.com/puppetlabs/puppetlabs-stdlib.git`
2. puppetlabs-postgresql `https://github.com/puppetlabs/puppetlabs-postgresql.git`
3. puppetlabs-apt `https://github.com/puppetlabs/puppetlabs-apt.git`
4. puppetlabs-concat `https://github.com/puppetlabs/puppetlabs-concat.git`

##Local Host File##
Edit `/etc/hosts/` by adding the line `127.0.0.1 	bank-dev`.

##Running The Virtual Machine##
In your working directory `BankApp/` run `vagrant up`. This will run the puppet provising which will install the required packages and dependencies to run the bank application