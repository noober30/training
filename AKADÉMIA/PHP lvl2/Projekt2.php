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
    
    $textFile = "loginTimeNew.txt";
    $jsonFile = "studentiNew.json";
    $jsonFile2 = "prichodyNew.json";
    $studentName = !empty($_REQUEST["name"]) ? htmlspecialchars($_REQUEST["name"]) : "host";
    $newStudent = ["meno"=>$_REQUEST["name"]];

    function timeDateNow()
    {
        return date("d.m.Y H:i:s");
    }

    function writeTimeName($logDateTime, $jsonFile, $textFile, $studentName, $jsonFile2)
//checks if txt file does exists, if so, writes time and name. If it doesn't, creates and writes txt file
    {   
        $arriveTime = strtotime($logDateTime);
        $timeStart = mktime(00,00,00);
        $timeOk = mktime(7,59,59);
        $timeEnd = mktime(19,59,59);

        if (!file_exists($textFile)) {
            if ($arriveTime > $timeStart && $arriveTime < $timeOk) {
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
        } else {
            if ($arriveTime > $timeStart && $arriveTime < $timeOk) {
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
    //reads txt File
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
        //checks if student was late
        private static function checkLateArrival($logDateTime)
        {
            $time = strtotime($logDateTime);
            $timeOk = mktime(8,0,0);
            return $time > $timeOk;
        }

        public static function loadCreateJsonFile($jsonFile)
        //load or create studenti.json
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
        //if file exists, iterates throught studenti.json and increments num of student's arrivals 
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
        //updates json file
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
    //writes time of arrival to json file
    {
        $existingArrivals = Students::loadCreateJsonFile($jsonFile2);
        $existingArrivals[] = $logDateTime;
        $jsonData = json_encode($existingArrivals, JSON_PRETTY_PRINT);
        file_put_contents($jsonFile2, $jsonData);
        $jsonArray = json_decode(file_get_contents($jsonFile2, True));
        $newArray = [];
    //iterates through json file and writes .meskanie to the late arrival
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


$students = new Students($jsonFile);
$arrivals = new Arrivals($jsonFile2);


writeTimeName(timeDateNow(), $jsonFile, $textFile, $studentName, $jsonFile2,);

?>
</body>
</html>
