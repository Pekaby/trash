<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>This is Local Host!</title>
    <link rel="stylesheet" href="src/css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;900&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="logo">localhost</div>
        <div class="loader">
            <div class="lds-heart"><div></div></div>
        </div>
    </header>
    <body>
        <div class="all">
            <div class="h1-center">
                <h1>It's working!</h1>
            </div>
            <div class="btns">
                <button class="btn1" onclick="redirect_to('/phpmyadmin')">phpmyadmin</button>
                <button class="btn2" onclick="php_info()">phpinfo</button>
            </div>
            <div class="info">
                <div id="php" style=""></div>
                <div class="system">
                    <?
system('service apache2 status', $var);
echo $var;
system('service mysql status', $var);
echo $var
                    ?>
                </div>
            </div>
        </div>
    </body>
    <script type="text/javascript">
        function redirect_to(url) {
            window.location.href = url;
        }
        // let test = document.getElementById('php')
        // test.innerHTML = "TEST"
        function php_info(){
            let info = document.getElementById('php')
            let xhr = new XMLHttpRequest()
            xhr.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    info.innerHTML = this.responseText;
                }
            }
            xhr.open("GET", '/info.php', true)
            xhr.send()
        }
        
    </script>
</body>
</html>