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
    echo "Datum a cas:  ".timeDateNow()."<br>";

    ?>

    <form action="ProjektNew.php" method="post">
        Meno: <input type="text" name="name">
        <input type="submit" value="Zapisat prichod">
    </form> 

    Vitaj, <?php echo (!empty($_REQUEST["name"]) ? htmlspecialchars($_REQUEST["name"]) : "host") . "!<br>"; ?>

    <?php 

    const TEXT_FILE = "loginTimeNew.txt";
    const JSON_FILE = "studentiNew.json";
    const JSON_FILE2 = "prichodyNew.json";

    $studentName = !empty($_REQUEST["name"]) ? htmlspecialchars($_REQUEST["name"]) : "host";
    $newStudent = ["meno" => $_REQUEST["name"]];

    function timeDateNow()
    {
        return date("d.m.Y H:i:s");
    }

    function writeTimeName($logDateTime, $jsonFile, $textFile, $studentName, $jsonFile2)
    {   
        $arriveTime = strtotime($logDateTime);
        define("TIME_START", mktime(0, 0, 0));
        define("TIME_OK", mktime(8, 0, 0));
        $timeEnd = mktime(20, 0, 0);

        if (!file_exists($textFile)) {
            if ($arriveTime > TIME_START && $arriveTime <= TIME_OK) {
                $logDateTime = $logDateTime;
            } elseif ($arriveTime >= $timeEnd) {
                die("<br>Neda sa zapisat");
            } else {
                $logDateTime = $logDateTime . " meskanie";
            }
    
            if (empty($studentName)) {
                echo strtoupper("Zadaj svoje meno!!!" . "<br>" . "<br>");
                $studentName = "host";
            }
        } else {
            if ($arriveTime > TIME_START && $arriveTime < TIME_OK) {
                $logDateTime = $logDateTime;
            } elseif ($arriveTime > $timeEnd) {
                die("<br>Neda sa zapisat");
            } else {
                $logDateTime = $logDateTime . " meskanie";
            }
    
            if (empty($studentName)) {
                echo strtoupper("Zadaj svoje meno!!!" . "<br>" . "<br>");
                $studentName = "host";
            }
        }
        if (!empty($studentName)) {
            file_put_contents($textFile, $studentName . " - " . $logDateTime . "\n", FILE_APPEND);
        }

        $totalArrivals = Students::addStudent($jsonFile, $studentName);
        Arrivals::addArrival($jsonFile2, timeDateNow());
        $data = Students::loadCreateJsonFile($jsonFile); 
        echo "Total Arrivals for $studentName: $totalArrivals<br><br>";
        print_r($data);
        echo "<br><br>";
        echo getLogs($textFile);
    } 

    function getLogs($textFile)
    {       
        $fileContents = file_get_contents($textFile);
        return nl2br($fileContents."<br>");
    }
     
    class Students {
        private $jsonFile;

        public function __construct($jsonFile)
        {
            $this->jsonFile = $jsonFile;
        }

        private static function checkLateArrival($logDateTime)
        {
            $time = strtotime($logDateTime);
            $timeOk = mktime(8, 0, 0);
            return $time > $timeOk;
        }

        public static function loadCreateJsonFile($jsonFile)
        {   
            if (file_exists($jsonFile))
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
            $late = self::checkLateArrival(timeDateNow());
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

        public function __construct($jsonFile2)
        {
            $this->jsonFile2 = $jsonFile2;
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

    $students = new Students(JSON_FILE);
    $arrivals = new Arrivals(JSON_FILE2);

    writeTimeName(timeDateNow(), JSON_FILE, TEXT_FILE, $studentName, JSON_FILE2);

    ?>
</body>
</html>
