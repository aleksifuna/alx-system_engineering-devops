# installs flask from pip3

# Install pip
package { 'python3-pip':
  ensure => present,
}
# Install Flask 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
# Install werkzeug 2.1.1
package { 'werkzeug':
ensure   => '2.1.1',
provider => 'pip3'
}
