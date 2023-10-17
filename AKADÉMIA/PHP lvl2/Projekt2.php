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
        echo "Datum a cas:  ".display()."<br>";
    ?>

    <form action="ProjektNew.php" method="post">
    Meno: <input type="text", name="name">
    <input type="submit" value="Zapisat prichod">
    </form> 

    Vitaj, <?php echo htmlspecialchars($_REQUEST["name"])."!"."<br>"; ?><br>

    <?php 

    $textFile = "loginTimeNew.txt";
    $jsonFile = "studentiNew.json";
    $jsonFile2 = "prichodyNew.json";
    $studentName = $_REQUEST["name"];
    $newStudent = ["meno"=>$_REQUEST["name"]];

    function display()
    {
        return date("d.m.Y H:i:s");
    }

    function writeTimeName($logDateTime)
        {   
            global $textFile; 
            $arriveTime = strtotime($logDateTime);
            $timeStart = strtotime(date("d.m.Y 0:00:00"));
            $timeOk = strtotime(date("d.m.Y 07:59:59"));
            $timeEnd = strtotime(date("d.m.Y 19:59:59"));

            if(file_exists($textFile))
            {
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
                    file_put_contents($textFile,$_REQUEST["name"]." - ". $logDateTime."\n", FILE_APPEND); 
                   
                }
            } else
            {
                file_put_contents($textFile,$_REQUEST["name"]." - ". $logDateTime."\n", FILE_APPEND); 
            }
        } 

    function getLogs()
    {
        global $textFile;
        $fileContents = file_get_contents($textFile);
        return nl2br($fileContents."<br>");
    }

    function loadCreateJsonFile($jsonFile)
    {
        if (file_exists($jsonFile))
        {
            $jsonContent = file_get_contents($jsonFile);
            $jsonData = json_decode($jsonContent, True);
            print_r($jsonData)."<br>";
        } else
        {   
            $jsonData = [];
            file_put_contents($jsonFile, json_encode($jsonData)); 
        }
        return $jsonData;
    }

    function addStudent($jsonFile, $studentName)
    {
        $existingStudents = loadCreateJsonFile($jsonFile);
        $totalArrivals = 1;
    
        foreach ($existingStudents as &$existingStudent) 
        {
            if (isset($existingStudent["name"]) && $existingStudent["name"] === $studentName) {
                $totalArrivals++;
            }
        }
    
        $newStudent = ["name" => $studentName, "totalArrivals" => $totalArrivals];
        $existingStudents[] = $newStudent;
        $jsonData = json_encode($existingStudents, JSON_PRETTY_PRINT);
        file_put_contents($jsonFile, $jsonData);
        return $totalArrivals;
    }
    
    function addArrival($jsonFile2, $logDateTime)
    {
        $existingArrivals = loadCreateJsonFile($jsonFile2);
        $existingArrivals[] = $logDateTime;
        $jsonData = json_encode($existingArrivals, JSON_PRETTY_PRINT);
        file_put_contents($jsonFile2,$jsonData);
        $jsonArray = json_decode(file_get_contents($jsonFile2, True));
        $newArray = [];
        foreach ($jsonArray as $timestamp)  
        {
            $time = strtotime($timestamp);
            $timeOk = strtotime(date("d.n.Y 8:00:00"));
            if ($time>$timeOk)
            {
                $timestamp .= " meskanie";
            }
            $newArray[] = $timestamp;
        }   
        file_put_contents($jsonFile2, json_encode($newArray, JSON_PRETTY_PRINT));
    }

    function studentiLate($jsonFile2)
    {
        
    }
    writeTimeName(display());
    $studentName = isset($_REQUEST["name"]) ? htmlspecialchars($_REQUEST["name"]) : "";
    $totalArrivals = addStudent($jsonFile, $studentName);
    addArrival($jsonFile2, display());
    echo "<br><br>Total Arrivals for $studentName: $totalArrivals<br><br>";
    echo getLogs() 
    
    ?>

    
</body>
</html>
