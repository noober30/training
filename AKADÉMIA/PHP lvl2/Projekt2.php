<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Login</title>
</head>
<body> 
    
    <?php 
            date_default_timezone_set("Pacific/Midway");
            echo "Datum a cas:  ".displayDateTime()."<br>";
    ?>
    
    <form action="Projekt1.php" method="post">
    Meno: <input type="text", name="name">
    <input type="submit">
    </form> 

    Vitaj, <?php echo $_REQUEST["name"]."!"."<br>"; ?><br>


    <?php

        function displayDateTime()
        {
            return date("d.m.Y H:i:s");
        }
    
        function writeTimeName($logDateTime) 
        {   
            $arriveTime = strtotime($logDateTime);
            $timeStart = strtotime(date("d.m.Y 0:00:00"));
            $timeOk = strtotime(date("d.m.Y 07:59:59"));
            $timeEnd = strtotime(date("d.m.Y 19:59:59"));

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

            $name = isset($_REQUEST["name"]) ? ($_REQUEST["name"]) : "";
            
            if (empty($name))
            {
                echo strtoupper("Zadaj svoje meno!!!"."<br>"."<br>");
            } else
            {
                file_put_contents("loginTime.txt",$_REQUEST["name"]." - ". $logDateTime."\n", FILE_APPEND); 
               
            }
        } 
 //       $nameJSON = array($name=> writeTimeName($logDateTime));
 //       echo json_encode($nameJSON);
        
        $fileName = "studenti.json";
        function loadCreateJsonFile($fileName)
        {
            if(file_exists($fileName))
            {
                $jsonContent = file_get_contents($fileName);
                return json_decode($jsonContent);
            } else
            {
                return [];
            }
        }

        function addStudent($fileName,$student)
        {
            $existingStudents = loadCreateJsonFile($fileName);
            $existingStudents[] = $student;
            $jsonData = json_encode($existingStudents, JSON_PRETTY_PRINT);
            file_put_contents($fileName, $jsonData);

        }


        $newStudent = ["meno"=>$_REQUEST["name"]];
        addStudent($fileName, $newStudent);



        function getLogs()
        {
            $fileContents = file_get_contents("loginTime.txt");
            return nl2br($fileContents);
        }

        writeTimeName(displayDateTime());
        echo getLogs();
        
    ?>

</body>
</html>