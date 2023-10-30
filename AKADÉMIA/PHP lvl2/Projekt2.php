<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
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

    Vitaj, <?php echo (!empty($_REQUEST["name"]) ? htmlspecialchars($_REQUEST["name"]) : "host") . "!<br>"; ?>

    <?php 
    $textFile = "loginTimeNew.txt";
    $jsonFile = "studentiNew.json";
    $jsonFile2 = "prichodyNew.json";
    $studentName = !empty($_REQUEST["name"]) ? htmlspecialchars($_REQUEST["name"]) : "host";
    $newStudent = ["meno"=>$_REQUEST["name"]];

    function display()
    {
        return date("d.m.Y H:i:s");
    }

    function writeTimeName($logDateTime)
    {   
        global $textFile; 
        global $jsonFile; 
        global $studentName; 
        global $jsonFile2;
        $arriveTime = strtotime($logDateTime);
        $timeStart = strtotime(date("d.m.Y 0:00:00"));
        $timeOk = strtotime(date("d.m.Y 07:59:59"));
        $timeEnd = strtotime(date("d.m.Y 19:59:59"));

        if (file_exists($textFile)) {
            if ($arriveTime > $timeStart && $arriveTime < $timeOk) {
                $logDateTime = $logDateTime;
            } elseif ($arriveTime > $timeEnd) {
                die("neda sa zapisat");
            } else {
                $logDateTime = $logDateTime . " meskanie";
            }
    
            if (!empty($studentName)) {
                file_put_contents($textFile, $studentName . " - " . $logDateTime . "\n", FILE_APPEND);
            }
    
            if (empty($studentName)) {
                echo strtoupper("Zadaj svoje meno!!!" . "<br>" . "<br>");
                $studentName = "host";
            }
        } else {
            if ($arriveTime > $timeStart && $arriveTime > $timeOk) {
                file_put_contents($textFile, $studentName . " - " . $logDateTime . " meskanie" . "\n", FILE_APPEND);
            }
        }

        $totalArrivals = Students::addStudent($jsonFile, $studentName);
        Arrivals::addArrival($jsonFile2, display());
        $data = Students::loadCreateJsonFile($jsonFile); 
        echo "Total Arrivals for $studentName: $totalArrivals<br><br>";
        print_r($data);
        echo "<br><br>";
        echo getLogs();
    } 

    function getLogs()
    {
        global $textFile;
        $fileContents = file_get_contents($textFile);
        return nl2br($fileContents."<br>");
    }
     
    class Students {
        private $jsonFile;
        public function __construct($jsonFile)
        {
            $this->jsonFile = $jsonFile;
        }
        public static function loadCreateJsonFile($jsonFile)
        {   
            if (!file_exists($jsonFile))
            {
                file_put_contents($jsonFile, "");
            }
            else if (file_exists($jsonFile))
            {
                $jsonContent = file_get_contents($jsonFile);
                $jsonData = json_decode($jsonContent, True);
            } 
            else
            {   
                $jsonData = [];
                file_put_contents($jsonFile, json_encode($jsonData)); 
            }
            return $jsonData;
        }

        public static function addStudent($jsonFile, $studentName)
        {
            $existingStudents = self::loadCreateJsonFile($jsonFile);
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
    }

class Arrivals{
    private $jsonFile2;

    public function __construct()
    {
        
    }
    public static function addArrival($jsonFile2, $logDateTime)
    {
        $existingArrivals = Students::loadCreateJsonFile($jsonFile2);
        $existingArrivals[] = $logDateTime;
        $jsonData = json_encode($existingArrivals, JSON_PRETTY_PRINT);
        file_put_contents($jsonFile2, $jsonData);
        $jsonArray = json_decode(file_get_contents($jsonFile2, True));
        $newArray = [];
        foreach ($jsonArray as $timestamp)  
        {
            $time = strtotime($timestamp);
            $timeOk = strtotime(date("d.n.Y 8:00:00"));
            if ($time > $timeOk)
            {
                $timestamp .= " meskanie";
            }
            $newArray[] = $timestamp;
        }   
        file_put_contents($jsonFile2, json_encode($newArray, JSON_PRETTY_PRINT));
    }
}

writeTimeName(display());

?>
</body>
</html>

