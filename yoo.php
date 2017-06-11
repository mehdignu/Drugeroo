<?php
  require('Pusher.php');

  $options = array(
    'cluster' => 'eu',
    'encrypted' => true
  );
  $pusher = new Pusher(
    'b91115f15fb79204ed0d',
    '1267c358e31740c55933',
    '351287',
    $options
  );

  $data['message'] = 'hello world';
  $pusher->trigger('my-channel', 'my-event', $data);
?>
