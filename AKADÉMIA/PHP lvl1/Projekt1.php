<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Login</title>
</head>
<body>  
    <?php

        $pozdrav = "Ahoj";
        echo $pozdrav. "<br>";

        function displayDateTime()
        {
            date_default_timezone_set("Europe/Bratislava");
            return date("Y-m-d H:i:s");
        }

        function writeTime($logDateTime) 
        {   
            $arriveTime = strtotime($logDateTime);
            $timeStart = strtotime(date("Y-m-d 0:00:00"));
            $timeOk = strtotime(date("Y-m-d 07:59:59"));
            $timeEnd = strtotime(date("Y-m-d 19:59:59"));

            if ($arriveTime>$timeStart && $arriveTime<$timeOk)
            {
                $logDateTime = $logDateTime;
            } elseif ($arriveTime> $timeEnd)
            {
                die("neda sa zapisat");   
            } else
            {
                $logDateTime = $logDateTime." meskanie";
            }
            file_put_contents("loginTime.txt",$logDateTime."\n", FILE_APPEND); 
        } 

        function getLogs()
        {
            $fileContents = file_get_contents("loginTime.txt");
            return str_replace("\n", "<br>", $fileContents);
        }

        echo "Datum a cas:  ".displayDateTime()."<br>" ;
        writeTime(displayDateTime());
        echo getLogs();
        
    ?>

</body>
</html>