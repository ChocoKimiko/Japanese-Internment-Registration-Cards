<!DOCTYPE HTML>
<!--
        ZeroFour by HTML5 UP
        html5up.net | @ajlkn
        Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
    <head>
        <title>Japanese occupation of the Dutch East Indie</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="assets/css/main.css" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
            .center {
                text-align: center;
            }

            .pagination {
                display: inline-block;
            }

            .pagination a {
                color: black;
                float: left;
                padding: 8px 16px;
                text-decoration: none;
                transition: background-color .3s;
                border: 1px solid #ddd;
                margin: 0 4px;
            }

            .pagination a.active {
                background-color: #2B2D33;
                color: white;
                border: 1px solid #2B2D33;
            }

            .pagination a:hover:not(.active) {
                background-color: #ddd;
                box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
            }

            form.example input[type=text] {
                padding: 10px;
                font-size: 17px;
                border: 1px solid grey;
                float: left;
                width: 100%;
                background: #f1f1f1;
            }

            form.example input {
                height: 100%;
                margin-top: -20px;
                margin-bottom: 40px;
            }

            form.example::after {
                content: "";
                clear: both;
                display: table;
            }
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script>
            $(document).ready(function () {
                $("#myInput").on("keyup", function () {
                    var value = $(this).val().toLowerCase();
                    $("#myList .major").filter(function () {
                        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
                    });
                });
            });
        </script>
    </head>
    <body class="no-sidebar is-preload">
        <div id="page-wrapper">
            <div id="header-wrapper">
                <div class="container">
                    <header id="header">
                        <div class="inner">
                            <h1><a href="index.php" id="logo">Second World War</a></h1>
                            <nav id="nav">
                                <ul>
                                    <li><a href="index.php">Home</a></li>
                                    <li class="current_page_item"><a href="japanese_internment_cards.php">JAPANESE INTERNMENT CARDS</a></li>
                                </ul>
                            </nav>
                        </div>
                    </header>
                </div>
            </div>

            <div id="main-wrapper">
                <div class="wrapper style2">
                    <div class="inner">
                        <section class="container box feature1">
                            <div class="row">
                                <div class="col-12">
                                    <header class="first major">
                                        <h2 class="icon fa-file-alt">JAPANESE INTERNMENT CARDS</h2>
                                        <p>Here you can find the <strong>prisoners of war</strong> who are held captive in the Internment Camps.</br>
                                            You can search on the name, place of birth or date of birth.</p>
                                        <form id="my-form" class="example" style="margin:auto;max-width:700px;">
                                            <input id="myInput" myInput="myInput" type="text" placeholder="Search..">
                                        </form>
                                        <p>For more details, click on a specific name.</p>
                                    </header>
                                    <?php
                                    $starttime = microtime(true);
                                    $row = 1;
                                    if (($handle = fopen("complete_data.csv", "r")) !== FALSE) {
                                        while (($data = fgetcsv($handle, 10000, ",")) !== FALSE) {
                                            $num = count($data);
                                            ini_set('max_execution_time', 300); //600 seconds = 10 minutes
                                            ?>
                                            <span id="myList">
                                                <header class="major">
                                                    <article class="box excerpt">
                                                        <div>
                                                            <header>
                                                                <h3><a href="japanese_internment_cards_person.php?id=<?php echo $data[0] ?>">
                                                                        <?php
                                                                        if ($data[1] != "" && $data[40] != "" && $data[5] != "") {
                                                                            echo "$data[1] ($data[40], $data[5])";
                                                                        } elseif ($data[1] != "" && $data[40] == "" && $data[5] != "") {
                                                                            echo "$data[1] ($data[5])";
                                                                        } elseif ($data[1] != "" && $data[40] == "" && $data[5] == "") {
                                                                            echo "$data[1]";
                                                                        } else {
                                                                            echo "$data[1] ($data[40], $data[5])";
                                                                        }
                                                                        $row++;
                                                                        ?>
                                                                    </a></h3>
                                                            </header>
                                                        </div>
                                                    </article>
                                                </header>
                                            </span>
                                            <?php
                                        }
                                        $endtime = microtime(true);
                                        fclose($handle);
                                    }
                                    ?>
                                </div>
                        </section>
                    </div>
                </div>
            </div>

            <div id="footer-wrapper">
                <footer id="footer" class="container">
                    <div class="row">
                        <div class="col-12">
                            <div id="copyright">
                                <ul class="menu">
                                    <li>&copy; Vrije Universiteit Amsterdam. All rights reserved</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </footer>
            </div>

        </div>

        <script src="assets/js/jquery.min.js"></script>
        <script src="assets/js/jquery.dropotron.min.js"></script>
        <script src="assets/js/browser.min.js"></script>
        <script src="assets/js/breakpoints.min.js"></script>
        <script src="assets/js/util.js"></script>
        <script src="assets/js/main.js"></script>

    </body>
</html>