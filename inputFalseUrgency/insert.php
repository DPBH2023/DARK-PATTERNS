<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $keywords = $_POST['keywords'];
    // SQLite database connection
    $conn = mysqli_connect('localhost', 'root', '', 'DPBH');
    if (!$conn) {
        die('Connection Failed : ' . mysqli_connect_error());
    } else {
        echo "Connection created<br>";
        //insert keywords in sql table
        $stmt = $conn->prepare("INSERT INTO `falseUrgency` (`Keywords`) VALUES (?)");
        $stmt->bind_param("s", $keywords);
        if ($stmt->execute()) {
            echo "Words recieved succesfully";
        } else {
            echo "Words not recieved succesfully";
        }
        $stmt->close();
    }
    $conn->close();
}
// echo "Hello";

?>