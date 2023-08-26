This challenge required uploading a `GIF` file to the website's backend in order to later be able to view it.
Here's the PHP code for the backend of the website:

```php
<?php
$files = $_FILES["fileToUpload"];
$uploadOk = true;
if($files["name"] != ""){
    $target_dir = urldecode("images/" . $files["name"]);
    if(strpos($target_dir,"..") !== false){
        $uploadOk = false;
    }
    if(filesize($files["tmp_name"]) > 1*1000){
        $uploadOk = false;
        echo "too big!!!";
    }
    $extension = strtolower(pathinfo($target_dir,PATHINFO_EXTENSION));
    $finfo = finfo_open(FILEINFO_MIME_TYPE);
    $type = finfo_file($finfo,$files["tmp_name"]);
    finfo_close($finfo);
    if($extension != "gif" || strpos($type,"image/gif") === false){
        echo " Sorry, only gif files are accepted";
        $uploadOk = false;
    }
    $target_dir = strtok($target_dir,chr(0));
    if($uploadOk && move_uploaded_file($files["tmp_name"],$target_dir)){
        echo "<a href='$target_dir'>uploaded gif here go see it!</a>";
    }
}
?>
```
After a few attempts, I noticed that the backend was checking certain parameters of the file, such as not being too memory-intensive, not having a traversal path in its name, having a `.gif` extension, and having the correct magic numbers for a valid `GIF` file.<br>
I also observed how it used `strtok()` between the file name and a null byte, taking the first part of the string as the actual file name. Following this observation, I was able to write a PHP reverse shell (which is in my [GitHub](https://github.com/AlBovo/CTF-Writeups/tree/main/nullcon%20CTF%202023) repository) named `rev.php%00.gif`. This file name successfully bypassed all the checks, and after the function execution, the actual file name would become `rev.php`.<br>
As soon as I opened the file at the URL `images/rev.php`, I could execute commands in the shell as `www-data`.
