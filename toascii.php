<!DOCTYPE html>

<html>
<body>

<style>
.font1{
    font-family: monospace;
}
</style>

<?php
$directory = "images/";

$target_file = $directory.basename($_FILES["select_file"]["name"]);

if(isset($_POST["submit"])) {      
    if (move_uploaded_file($_FILES["select_file"]["tmp_name"], $target_file)) {
        $name = $_FILES["select_file"]["name"];
        $scale = $_POST["scale"];
        if(isset($_POST["background"])){
            $background = $_POST["background"];
        }
        else{
          $background = "black";
        }

        
        $to_ascii = shell_exec("python toAscii.py False $name $background $scale");

        //filter out everything at the start until we meet one of these characters: '@', '%', '#', '&', '=', '+', '-', ':', ',', '.'
        $to_ascii = preg_replace("/^shape: [^\@\%\&\=\+\-\:\.\#]*/", "", $to_ascii);
        $result = preg_replace("/>/", "<br>", $to_ascii);
        
        echo "<label for='result' class='font1'> $result </label>";
    }
}
else{
  echo "Did not submit. Please attempt again";
}
?>

</body>
</html>