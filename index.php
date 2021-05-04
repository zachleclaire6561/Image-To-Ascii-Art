<!DOCTYPE html>
<style>
.font1{
    font-family: monospace;
}
</style>

<html>
<body>
<form action="toascii.php" method="post" enctype="multipart/form-data">
    Please Select your image: </br>
    <input type="file" name="select_file" id="select_file">
    </br> </br>
    <input type="checkbox" name="background" value="white", id="background">
    <label for="background" name="backgroundlabel"> Black or White Background </label>
    </br> </br>
    <label for="scale" name="header-label">    Image Scale   </label> 
    <br>
    <input type="range" min="1" max="30" value="15" class="slider" name="scale" id="scale">
    <label for="scale" name="scale_label" id="scale_label"> 50 </label>
    </br>
    <input type="submit" value="Upload Image" name="submit">
</form>

<script>
    // update scale_label when scale value is changed
    var scaler = document.getElementById("scale");
    var scale_label = document.getElementById("scale_label");
    scale_label.innerHTML = Math.trunc(scaler.value/30*100);
    scaler.oninput = function() {
        scale_label.innerHTML = Math.trunc(this.value/30*100);
    }
</script>

</body>
</html>