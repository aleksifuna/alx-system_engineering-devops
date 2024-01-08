# installs and configures a nginx server

exec { 'update_package_list':
  command  => 'apt-get update',
  provider => 'shell',
}

package { 'nginx':
  ensure => present,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  content => "
  server {
  listen 80;
  listen [::]:80 default_server;
  root /var/www/html;
  index  index.html index.htm;
  location / {
      try_files \$uri \$uri/ =404;
      add_header X-Served-By \${hostname};
    }
  }",
}

exec { 'restart service':
  command  => 'service nginx restart',
  provider => shell,
}
