# Increase the limit of file descriptors for nginx

exec { 'increase-fd':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => '/usr/sbin/:/usr/bin/'
}
