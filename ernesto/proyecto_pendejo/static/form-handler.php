<?php
 $name = $_POST['nombre'];
 $visitor_email = $_POST['email'];
 $subject = $_POST['asunto'];
 $message = $_POST['mensaje'];

$email_from = 'https://xsarscov-code50-110932159-pj5x4r6prfr4wp-5000.preview.app.github.dev/';

$email_subject = 'New form submission';

$email_body = "Usuario: $name.\n".
                    "Email: $visitor_email.\n".
                    "Asunto: $subject.\n".
                    "Mensaje: $message.\n";

$to = 'alexanderjosue998@gmail.com';

$headers = "From: $email_from \r\n";

$headers .= "Reply-to: $visitor_email \r\n";

mail($to, $email_subject, $email_body, $headers);

header("Location: index.html");

?>