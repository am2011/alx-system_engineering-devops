# file without errors
 file { 'loginFile':
     ensure  => present,
     path    => '/etc/security/limits.conf',
     content => '#File erased'
 }
