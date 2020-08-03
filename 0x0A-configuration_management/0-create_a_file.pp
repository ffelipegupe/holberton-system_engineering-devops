# Creates a file in /tmp
file { 'holberton':
  ensure  => file,
  path    => '/tmp/holberton',
  content => 'I love Puppet',
  owner   => 'www-data',
  mode    => '0744',
  group   => 'www-data',
}