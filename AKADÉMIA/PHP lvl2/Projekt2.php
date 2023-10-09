<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student login</title>
</head>
<body>
    <?php 
        date_default_timezone_set("Pacific/Midway");
        echo "Datum a cas:  ".displayDateTime()."<br>";
    ?>

    <form action="Projekt2.php" method="post">
    Meno: <input type="text", name="name">
    <input type="submit">
    </form> 

    Vitaj, <?php echo htmlspecialchars($_REQUEST["name"])."!"."<br>"; ?><br>

    <?php 
    $fileName = "studenti2.json";
    $student = $_REQUEST["name"];
    $lastId = 1;
    $newStudent = ["meno"=>$_REQUEST["name"], "id"=>$lastId];


    function displayDateTime()
        {
            return date("d.m.Y H:i:s");
        };

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

            $name = isset($_REQUEST["name"]) ? htmlspecialchars($_REQUEST["name"]) : "";
            
            if (empty($name))
            {
                echo strtoupper("Zadaj svoje meno!!!"."<br>"."<br>");
            } else
            {
                file_put_contents("loginTime2.txt",$_REQUEST["name"]." - ". $logDateTime."\n", FILE_APPEND); 
               
            }
        } 

    function getLogs()
        {
            $fileContents = file_get_contents("loginTime2.txt");
            return nl2br($fileContents);
        }


    function loadCreateJsonFile($fileName)
    {
        if (file_exists($fileName))
        {
        $jsonContent = file_get_contents($fileName);
        $jsonData = json_decode($jsonContent, True);

        return $jsonData;
        }else
        {
            file_put_contents($fileName, "[]");
            return[];
        }
    }

    function addStudent($fileName, $student)
    {
        $existingStudents = loadCreateJsonFile($fileName);
        if (!is_array($existingStudents))
        {
            $existingStudents=[];
        }
        $highestId = 0;
        foreach ($existingStudents as $existingStudent) {
            if(isset($existingStudent["id"]) && $existingStudent["id"]>$highestId)
            {
                $highestId=$existingStudent["id"];
            }
        }
        $student["id"] = $highestId+1;
        $existingStudents[] = $student;
        $lastID = $student["id"];

        $jsonData = json_encode($existingStudents, JSON_PRETTY_PRINT);
        file_put_contents($fileName, $jsonData);
        print_r($jsonData."<br>");

    }


    writeTimeName(displayDateTime());
    addStudent($fileName, $newStudent, $lastId);
    echo getLogs();
    ?>

    
</body>
</html>
