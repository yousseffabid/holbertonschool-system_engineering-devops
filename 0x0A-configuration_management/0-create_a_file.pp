#create file in /tmp

file { 'school':
    ensure      => present,
    mode        => '0744',
    content     => 'I love Puppet',
    path        => '/tmp/school',
    owner       => 'www-data',
    group       => 'www-data',
}
